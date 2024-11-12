<script setup>
import axios from 'axios'
import {reactive, ref, onMounted} from "vue";
import {ElMessage} from "element-plus";

const books = ref([])
const getStudents = () => {
  axios.get("http://localhost:5000/books",).then(res => {
    books.splice(0, books.length)
    books.push(...res.data.results)
    console.log('更新数据')
  })
}

</script>

<template>
  <div style="margin: 0 auto; width: 50%;">
    <h1 style="text-align: center">图书管理系统</h1>
    <!-- 添加图书按钮 -->
    <el-button type="primary" @click="add_dialog_visible = true" size="small">添加图书</el-button>
    <!-- 数据表格 -->
    <el-table :data="books" style="margin: 20px auto;">
      <el-table-column label="编号" prop="book_number"/>
      <el-table-column label="书名" prop="book_name"/>
      <el-table-column label="类型" prop="book_type"/>
      <el-table-column label="价格" prop="book_prize"/>
      <el-table-column label="作者" prop="author"/>
      <el-table-column label="出版社" prop="book_publisher"/>
      <el-table-column align="right" label="操作" width="200px">
        <template #default="scope">
          <el-button size="small" @click="handleEdit(scope.$index, scope.row)">
            编辑
          </el-button>
          <el-button size="small" type="danger" @click="handleDelete(scope.$index, scope.row)">
            删除
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>


<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}

.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}

.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
