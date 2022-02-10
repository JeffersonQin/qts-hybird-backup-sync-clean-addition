# QTS Hybird Sync Backup 增量备份清理工具

QTS 的 Hybird Sync Backup 的增量备份会对文件重命名，产生多份副本。本工具用于清理生成的冗余文件。

```
$ python .\main.py clean --help                         
Usage: main.py clean [OPTIONS] PATH

  Clean redundant syncing storage

  Args:         path (click.Path): Path to clean

Options:
  --help  Show this message and exit
```
