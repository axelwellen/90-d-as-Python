# defaultdict para agrupar
#
# agrupar eventos por usuario

from collections import defaultdict

eventos = [
        ("ana", "login"),
        ("pepe", "logout"),
        ("ana", "download")
        ]

d = defaultdict(list)

for k,v in eventos: 
    d[k].append(v)

print(dict(d))
