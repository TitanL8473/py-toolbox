# Day 6 · 我的提交 main.py（10/14）

import mytools

print(mytools.count_lines('data.txt'))
print(mytools.count_vowels('HelloWorld'))
print(mytools.best_subject({"语文": 70, "数学": 85, "英语": 60}))
print(mytools.average([70, 85, 92.5]))

from mytools import count_vowels

print(count_vowels('HelloWorld'))
