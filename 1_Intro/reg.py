import re

# 其中r"\d+"正则表达式表示匹配连续的多个数值
reg=r"\d+"
m=re.search(reg,"abc123cd")
print(m)

# 字符"\d"匹配0-9之间的一个数值
reg=r"\d"
m=re.search(reg,"abc123cd")
print(m)

# 字符"+"重复前面一个匹配字符一次或者多次
reg=r"b\d+"
m=re.search(reg,"a12b123c")
print(m)

# 字符"*"重复前面一个匹配字符零次或者多次
reg=r"ab+"
m=re.search(reg,"acabc")
print(m)
reg=r"ab*"
m=re.search(reg,"acabc")
print(m)

# 字符"?"重复前面一个匹配字符零次或者一次
reg=r"ab?"
m=re.search(reg,"abbcabc")
print(m)

# 字符"."代表任何一个字符，但是没有特别声明时不代表字符"\n"
s="xaxby"
m=re.search(r"a.b",s)
print(m)

# "|"代表把左右分成两个部分,
# 结果匹配"ab"或者"ba"都可以
s="xaabababy"
m=re.search(r"ab|ba",s)
print(m)

# 特殊字符使用反斜线"\"引导，例如"\r"、"\n"、"\t"、"\\"分别表示回车、换行、制表符号与反斜线本身
reg=r"a\nb?"
m=re.search(reg,"ca\nbcabc")
print(m)

# 字符"\b"表示单词结尾，单词结尾包括各种空白字符或者字符串结尾
reg=r"car\b"
m=re.search(reg,"The car is black")
print(m)

# "[]"中的字符表示任意选择一个，如果字符是ASCII码中连续的一组，
# 那么可以使用"-"符号连接，例如[0-9]表示0-9的其中一个数字，[A-Z]表示A-Z的其中一个大写字符，[0-9A-Z]表示0-9的其中一个数字或者是A-Z的其中一个大写字符
reg=r"x[0-9]y"
m=re.search(reg,"xyx2y")
print(m)

# "^"出现在[]的第一个字符位置，就代表取反，例如[^ab0-9]表示不是a、b，也不是0-9的数字
reg=r"x[^ab0-9]y"
m=re.search(reg,"xayx2yxcy")
print(m)

# "\s"匹配任何空白字符，等价"[\r\n\x20\t\f\v]"
s="1aba\tbxy"
m=re.search(r"a\sb",s)
print(m)

# "\w"匹配包括下划线内的单词字符，等价于"[a-zA-Z0-9]"
reg=r"\w+"
m=re.search(reg,"Python is easy")
print(m)

# "^"匹配字符串的开头位置
reg=r"^ab"
m=re.search(reg,"cabcab")
print(m)
# 没有匹配到任何字符，因为"cabcab"中虽然有"ab"，但不是"ab"开头。

# "$"字符匹配字符串的结尾位置
reg=r"ab$"
m=re.search(reg,"abcab")
print(m)

# 使用括号（...）可以把（...）看成一个整体，经常与"+"、"*"、"?"等符号连续使用，对（...）部分进行重复
reg=r"(ab)+"
m=re.search(reg,"ababcab")
print(m)

# 正则表达式库re的search函数使用正则表达式对要匹配的字符串进行匹配，如果匹配不成功就返回None，如果匹配成功就返回一个匹配对象。
# 匹配对象调用start()函数得到匹配字符串的开始位置，匹配对象调用end()函数得到匹配字符串的结束位置。search虽然只返回第一次匹配的结果，
# 但是只要连续使用search函数就可以找到字符串中全部匹配的字符串。

# 例：匹配找出英文句子中所有单词
s="I am testing search function"
reg=r"[A-Za-z]+\b"
m=re.search(reg,s)
while m!=None:
    start=m.start()
    end=m.end()
    print(s[start:end])
    s=s[end:]
    m=re.search(reg,s)