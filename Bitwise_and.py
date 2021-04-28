n,m=map(int,input().split())
l=list(map(int,input().split()))
for _ in range(m):
    p=list(map(int,input().split()))
    i=0
    for j in range(p[0],p[1]+1):
        if i<=p[1]:
            l[i]=l[i] & p[-1]
            i+=1
print(l)
