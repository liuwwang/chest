### 通过对比Git提交记录，生成升级包

**建立软链接**
```
ln -s ../daily_tools/package_upgrade
```
**执行命令**
```
python package_upgrade/increment.py main git_no1 git_no2
git_no1 git_no2 为两次提交记录ID号
```

**升级包位置会自动生成到当前文件夹下`upgrade.tar`**
