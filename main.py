# main.py —— 演示 mytools 里的每个函数怎么用
#
# 运行：  python main.py

from pathlib import Path

import mytools
from mytools import count_vowels          # from ... import ... 的用法示例

# 用 __file__ 定位，跟"你在哪个目录运行"无关
HERE = Path(__file__).resolve().parent

if __name__ == "__main__":
    print("当前工作目录:", Path.cwd())
    print()

    print("── 基础工具 ──")
    print("count_vowels('HelloWorld')            ->", mytools.count_vowels('HelloWorld'))
    print("average([70, 85, 92.5])               ->", mytools.average([70, 85, 92.5]))
    print("best_subject({语文:70,数学:85,英语:60}) ->",
          mytools.best_subject({"语文": 70, "数学": 85, "英语": 60}))
    print("count_lines(HERE/'data.txt')          ->", mytools.count_lines(HERE / 'data.txt'))
    print("count_lines(不存在的文件)              ->", mytools.count_lines(HERE / '没有这个文件.txt'))
    print()

    print("── 文件与目录工具（Day 8 · pathlib）──")
    print("describe(HERE/'data.txt')             ->", mytools.describe(HERE / 'data.txt'))
    print("list_py_files(HERE) 的前三个           ->", mytools.list_py_files(HERE)[:3])
    print("count_all_py(HERE)                    ->", mytools.count_all_py(HERE))
    print()

    print("── from ... import ... 的用法（不用加前缀）──")
    print("count_vowels('HelloWorld')            ->", count_vowels('HelloWorld'))
