name="saeed"
typed="ssaaedd"
d1={}
d2={}
for i in range(len(name)):
    if name[i] in d1:
        d1[name[i]]+=1
    else:
        d1[name[i]]=1
for j in range(len(typed)):
    if typed[j] in d2:
        d2[typed[j]]+=1
    else:
        d2[typed[j]]=1
y=d1.keys()
c=1
for i in y:
    print(i,d1[i],d2[i])
    if d1[i]>d2[i]:
        c=0
if c==0:
    print("false")
else:
    print("true")
