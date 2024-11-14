https://www.bilibili.com/video/BV1Jr4y1771i?p=2

***

https://notes.zhengxinonly.com/bilibili/case/vue_book.html

https://gitee.com/nmaptech/flask_vue_demo

https://github.com/guosaike/fvtushu



源码: [flask+图书信息管理系统（flask+vue）.zip](flask+图书信息管理系统（flask+vue）.zip) 

***



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

***
根据你提供的错误信息，问题出在推送命令中的分支名称。在 GitHub 中，默认的主分支名称通常是 `main`，而不是 `master`。因此，出现错误是因为你的本地仓库中没有 `master` 分支。

### 解决步骤：

1. **查看当前分支**
   
   首先，你可以检查当前分支的名称，使用以下命令：
   ```bash
   git branch
   ```
   这会列出所有本地分支，当前所在分支会显示为 `*`。

2. **如果当前分支是 `main`，而不是 `master`**

   在这种情况下，你需要将推送的分支名称更改为 `main`，而不是 `master`：
   ```bash
   git push -u origin main
   ```

3. **如果当前没有分支，或者你刚刚初始化仓库**

   如果你的仓库是刚初始化的，没有提交过文件，Git 会提示没有分支。你可以通过以下命令创建并推送 `main` 分支：
   ```bash
   git checkout -b main
   git push -u origin main
   ```

### 总结：

- 你应该确认你使用的分支名称是 `main`，而不是 `master`，并使用 `git push -u origin main` 来推送更改。
- 如果仓库是全新初始化的，确保至少有一次提交后再推送。

如果按照以上步骤操作仍然出现问题，检查是否已经正确连接到 GitHub 远程仓库，或者你可以尝试重新克隆远程仓库并重新推送。

***

在 Git 中，回滚到之前的状态可以通过以下几种方式实现，具体取决于你想要恢复的内容（如提交、文件、分支等）。

### 1. **使用 `git reset` 回滚到某个提交**
`git reset` 可以用来回滚到之前的提交。它有三个常用模式：`--soft`、`--mixed` 和 `--hard`。

- **`git reset --soft <commit>`**：回滚到指定的提交，并保留暂存区的更改。
- **`git reset --mixed <commit>`**：回滚到指定的提交，保留工作目录中的更改，但清除暂存区的更改。
- **`git reset --hard <commit>`**：彻底回滚到指定的提交，丢弃工作目录和暂存区的更改（危险操作，慎用）。

#### 示例：
```bash
# 回滚到某个提交（例如，`abc1234`）
git reset --hard abc1234
```

### 2. **使用 `git checkout` 恢复文件**
如果你只想恢复某个文件到之前的状态，可以使用 `git checkout`。

#### 示例：
```bash
# 恢复某个文件到上一个提交的状态
git checkout <commit> -- <file>
```

### 3. **使用 `git revert` 撤销某个提交**
如果你想撤销某个提交的影响，但保持提交历史，可以使用 `git revert`。它会创建一个新的提交来撤销指定提交的更改。

#### 示例：
```bash
# 撤销某个提交的更改，并生成新的提交
git revert <commit>
```

### 4. **使用 `git log` 查找提交**
在使用 `reset` 或 `revert` 前，你可能需要查看提交历史以找到目标提交。可以使用 `git log` 查看提交记录。

#### 示例：
```bash
git log --oneline
```

这些方法可以帮助你根据不同的需求回滚到之前的状态。如果不确定该用哪种方法，可以先使用 `git reset --soft` 或 `git checkout` 来避免丢失重要数据。