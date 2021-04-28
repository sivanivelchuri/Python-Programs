n=6
m=5
d={}
c=0
seive=[i for i in range(n+1)]
i=2
while i*i<=n:
    for j in range(i*i,n+1,i):
            if seive[j]%i==0:
                seive[j]=i
    i+=1
print(seive)
while m!=1:
    if seive[m] in d:
        d[seive[m]]+=1
    else:
        d[seive[m]]=1
    x=m//seive[m]
    m=x
y=1
print(d)
for i in d.keys():
    print(i,'^',d[i])
