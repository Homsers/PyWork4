
import collections



a = ('WWWWWWWBWWWWWWWBBBWWWWWWWWBWWWW')
a = collections.Counter(a)
print(a)

import json 

with open("rle.json", "w", encoding="utf-8") as file:
    json.dump(a, file)



