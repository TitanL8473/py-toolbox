# py-toolbox

我学习 Python 过程中沉淀的一个小工具箱。每个函数都配了说明和用法，可以直接 import 复用。

## 功能

| 函数 | 作用 |
|---|---|
| `count_vowels(text)` | 统计字符串里元音（a/e/i/o/u）的个数，不区分大小写 |
| `average(numbers)` | 求一组数字的平均数 |
| `best_subject(subjects)` | 传入「科目: 分数」字典，返回分数最高的科目名 |
| `count_lines(path)` | 统计文本文件的行数；文件不存在时返回 -1 |
| `describe(path)` | 返回「文件名 \| 后缀 \| 上级目录名」形式的描述 |
| `list_py_files(folder)` | 列出文件夹本层所有 `.py` 文件名，按名字排序 |
| `count_all_py(folder)` | 递归统计文件夹下所有 `.py` 文件总数 |

## 用法

```python
import mytools

mytools.count_vowels("Hello World")        # 3
mytools.average([70, 85, 92.5])            # 82.5
mytools.best_subject({"语文": 70, "数学": 85, "英语": 60})   # 数学
mytools.count_lines("data.txt")            # 4

# Day 8 新增：文件与目录工具
mytools.describe("data.txt")               # data.txt | 后缀 .txt | 上级目录 ...
mytools.list_py_files(".")                 # ['.py 文件名列表，已排序']
mytools.count_all_py(".")                  # 递归统计 .py 总数
```

也可以直接运行 `main.py` 看全部示例：

```bash
python main.py
```

> `main.py` 用 `Path(__file__).parent` 定位文件，所以在任何目录下运行都能找到 `data.txt`。

## 环境

- Python 3.13
- 无第三方依赖

## 已知问题 / TODO

<!-- 这一栏是真实项目里最重要的部分之一：诚实记录你现在还没解决的问题。
     写清楚，未来的你会感谢现在的你。 -->

- [ ] `average([])` 传空列表时会抛 `ZeroDivisionError`，还没处理
- [ ] 还缺一个 `folder_report(folder)`：递归统计文件数 / 总大小 / 按后缀分组
- [ ] 还没写单元测试
- [ ] `count_lines` 的提示信息没带上具体路径，出问题时不好定位

## 背景

交通（交通运输工程）专业在读硕士，研究方向为隧道抗震与损伤分析。
这是我从零开始补编程基础时做的第一个可复用工具集。
