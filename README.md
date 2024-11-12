https://www.bilibili.com/video/BV1Jr4y1771i?p=2

在 VS Code 中初始化存储库并上传到 GitHub 的步骤如下：

### 1. 初始化本地 Git 仓库
如果你还没有初始化 Git 仓库，可以在 VS Code 中打开终端，然后使用以下命令：
```bash
git init
```
这将初始化一个本地 Git 仓库。

### 2. 添加文件到暂存区
将文件添加到 Git 的暂存区：
```bash
git add .
```
这会将所有文件添加到暂存区。如果你只想添加特定文件，可以用 `git add 文件名` 来添加。

### 3. 提交文件
在添加文件之后，提交这些更改：
```bash
git commit -m "Initial commit"
```
这里的 `"Initial commit"` 是提交信息，你可以根据实际情况修改。

### 4. 创建 GitHub 仓库
- 打开 [GitHub](https://github.com/)，登录你的账户。
- 在右上角点击 `+` 号，选择 `New repository`。
- 填写仓库名称，选择是否公开，并点击 `Create repository`。

### 5. 连接本地仓库与 GitHub 仓库
复制 GitHub 上新建仓库的 URL（通常是 `https://github.com/your-username/your-repository.git`）。

然后，在 VS Code 的终端中，使用以下命令将本地仓库与 GitHub 仓库关联：
```bash
git remote add origin https://github.com/your-username/your-repository.git
```

### 6. 推送到 GitHub
使用以下命令将本地仓库的内容推送到 GitHub：
```bash
git push -u origin master
```
如果是 GitHub 新建的仓库，主分支名称可能是 `main` 而不是 `master`，可以根据实际情况调整。

### 7. 输入 GitHub 凭据
如果是首次推送，你需要输入 GitHub 用户名和密码。如果启用了两步验证，则需要使用 GitHub 提供的令牌。

### 8. 完成
此时，你的项目应该已经成功上传到 GitHub 仓库。

之后，只需要使用 `git push` 来推送新的更改，或者使用 `git pull` 来拉取远程仓库的更改。