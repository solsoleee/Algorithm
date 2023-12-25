d=0
mon=["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
date=[31,28,31,30,31,30,31,31,30,31,30,31]
x,y=map(int, input().split())
for i in range(x-1):
    d+=date[i]
d+=y
print(mon[(d%7)])