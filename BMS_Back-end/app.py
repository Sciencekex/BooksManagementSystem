from flask import Flask, request, jsonify
from flask_cors import CORS  # 引入 CORS
from flask.views import MethodView
from extension import db
from models import Book

app = Flask(__name__)

# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# 修改 CORS 配置
CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:5173"],  # 允许的源
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # 允许的方法
        "allow_headers": ["Content-Type"],  # 允许的请求头
        "supports_credentials": True  # 支持凭证
    }
})


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/books/', methods=['OPTIONS'])
@app.route('/books/<int:book_id>', methods=['OPTIONS'])
def handle_options(book_id=None):
    response = app.make_default_options_response()
    return response

@app.cli.command()
def create():
    db.drop_all()
    db.create_all()
    Book.init_db()


class BookApi(MethodView):
    def get(self, book_id):
        if not book_id:
            books: [Book] = Book.query.all()
            results = [
                {'id': book.id,
                 'book_name': book.book_name,
                 'book_type': book.book_type,
                 'book_prize': book.book_prize,
                 'book_number': book.book_number,
                 'book_publisher': book.book_publisher,
                 'author': book.author}
                for book in books
            ]
            return {
                'status': 'success',
                'message': '数据查询成功',
                'results': results
            }
        book: Book = Book.query.get(book_id)
        return {
            'status': 'success',
            'message': '数据查询成功',
            'result': {
                'id': book.id,
                'book_name': book.book_name,
                'book_type': book.book_type,
                'book_prize': book.book_prize,
                'book_number': book.book_number,
                'book_publisher': book.book_publisher,
                'author': book.author
            }
        }

    def post(self):
        form = request.json
        book = Book()
        book.book_number = form.get('book_number')
        book.book_name = form.get('book_name')
        book.book_type = form.get('book_type')
        book.book_prize = form.get('book_prize')
        book.author = form.get('author')
        book.book_publisher = form.get('book_publisher')
        db.session.add(book)
        db.session.commit()
        return {
            'status': 'success',
            'message': '数据添加成功'
        }

    def delete(self, book_id):
        book = Book.query.get(book_id)
        db.session.delete(book)
        db.session.commit()
        return {
            'status': 'success',
            'message': '数据删除成功'
        }

    def put(self, book_id):
        book = Book.query.get(book_id)
        book.book_type = request.json.get('book_type')
        book.book_name = request.json.get('book_name')
        book.book_prize = request.json.get('book_prize')
        book.book_number = request.json.get('book_number')
        book.book_publisher = request.json.get('book_publisher')
        book.author = request.json.get('author')
        db.session.commit()
        return {
            'status': 'success',
            'message': '数据修改成功'
        }


book_view = BookApi.as_view('book_api')
app.add_url_rule('/books/', defaults={'book_id': None}, view_func=book_view, methods=['GET'])
app.add_url_rule('/books/', view_func=book_view, methods=['POST'])
app.add_url_rule('/books/<int:book_id>', view_func=book_view, methods=['GET', 'PUT', 'DELETE'])

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)
