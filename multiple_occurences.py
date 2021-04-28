z=[1,2,3,3,2,2]
q={}
s=0
for i in range(len(z)):
    if z[i] not in q:
        q[z[i]]=[i]
    else:
        q[z[i]].append(i)
print("q=",q)
p=q.values()
print(p)
for i in q.values():
    print(i)
    s+=abs(i[0]-i[-1])
print(s)
