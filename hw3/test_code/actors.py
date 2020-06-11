file = open("movie.txt", "r", encoding="utf-8")
data = file.readlines()
content = []
for line in data:
    t = line.replace("\"", "").split(";")
    s = []
    for item in t:
        s.append(item)
    content.append(s)

movie_act = {}

for line in content:
    try:
        actors = line[4].split(",")
    except:
        continue

    movie_act.update({line[1]:actors})

for item in movie_act:
    print(item)