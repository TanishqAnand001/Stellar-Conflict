f=open("story.txt", "r")
str=" "
s=0
ts=0
while str:
    str=f.readline()
    ts=ts+len(str)
print(ts)
f.close()
