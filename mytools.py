# mytools.py —— 我的 Python 工具箱
#
# Day 6（10/14）建立：把散落的函数收进一个可复用的模块
# Day 8（10/15）扩充：加入 pathlib 文件遍历工具

from pathlib import Path


# ---------- 基础工具 ----------

def count_vowels(text):
    """统计字符串里元音（a/e/i/o/u）的个数，不区分大小写。"""
    counts_vowels = 0
    for char in text:
        if char.lower() in {'a', 'e', 'i', 'o', 'u'}:
            counts_vowels += 1
    return counts_vowels


def average(number):
    """求一组数字的平均数。

    注意：目前传入空列表会抛 ZeroDivisionError，见 README 的已知问题。
    """
    sums = 0
    counts_numbers = 0
    for data in number:
        sums += data
        counts_numbers += 1
    dividend = sums / counts_numbers
    return dividend


def best_subject(subjects):
    """传入「科目: 分数」字典，返回分数最高的科目名。"""
    subject = None
    score = -999
    for key, value in subjects.items():
        if value > score:
            subject = key
            score = value
    return subject


def count_lines(path):
    """统计文本文件的行数；文件不存在时打印提示并返回 -1。"""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            line = file.readlines()
        return len(line)
    except FileNotFoundError:
        print('文件不存在')
        return -1


# ---------- 文件与目录工具（Day 8 · pathlib）----------

def describe(path):
    """返回 '<文件名> | 后缀 <后缀> | 上级目录 <父目录名>'。"""
    return f"{path.name} | 后缀 {path.suffix} | 上级目录 {path.parent.name}"


def list_py_files(folder):
    """列出文件夹【本层】所有 .py 的文件名，按名字排序。"""
    py_name_list = [p.name for p in Path(folder).glob('*.py')]
    return sorted(py_name_list)


def count_all_py(folder):
    """递归统计文件夹及其所有子文件夹里的 .py 文件总数。"""
    return len(list(Path(folder).rglob("*.py")))


if __name__ == "__main__":
    print(">>> mytools 自测")
    print(">>> count_vowels('Hello world') =", count_vowels("Hello world"))
    print(">>> list_py_files('.') =", len(list_py_files(".")))
    print(">>> count_all_py('.')  =", count_all_py("."))
