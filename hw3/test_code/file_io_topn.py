from pathlib import *
import os

# 用path读写,只能转成一维列表
# p = Path('movie.txt')
# content = p.read_text(encoding="utf-8")
# content.split(';')

file = open("movie.txt", "r",encoding="utf-8")
data = file.readlines()
content = []
for line in data:
    t = line.replace("\"","").split(";")
    s = []
    for item in t:
        s.append(item)
    content.append(s)

top = {}
n = 6
maxn = list(range(n-1, -1, -1))
print(maxn)

for line in content:
    for i in range(len(maxn)):
        try:
            t = int(line[6])
        except:
            break
        if(t > maxn[i]):
            if(maxn[i] in top):
                top.pop(maxn[i])

            maxn[i]= t
            top.update({t:line[1]})
            break
print(maxn)
for i in top.items():
    print(i)

