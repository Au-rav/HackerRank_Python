from collections import *

s = input()
Counter = Counter(s)
most_occur = dict(Counter.most_common(4))

for key in sorted(most_occur.keys()) :
    print(key , " " , most_occur[key])