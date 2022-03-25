### 通过对比Git提交记录，生成升级包

#### 使用
**建立软链接**
```
ln -s ../daily_tools/cmd_tools
```
**执行命令**
```
python cmd_tools/increment.py main git_no1 git_no2
git_no1 git_no2 为两次提交记录ID号
```

**升级包位置会自动生成到当前文件夹下`upgrade.tar`**
```
cli.py: git 操作
conf.py: 配置文件
increment.py: 执行文件
README.md: 阅读文档
upgrade.yml: 配置yml文件
utils.py: 工具文件
```
