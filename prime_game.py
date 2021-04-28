def prime():
    n=q
    seive=[1 for i in range(n+1)]
    seive[0]=seive[1]=0
    i=2
    while(i*i<=n+1):
        if seive[i]==1:
            j=i*i
            while j<n+1:
                seive[j]=0
                j+=i
        i+=1
    return seive
t=int(input())
for _ in range(t):
    p,q=map(int,input().split())
    seive=prime()
    k=[]
    for j in range(p,q+1):
        if seive[j]==1:
            k.append(j)
    if len(k)>1:
        print(k[-1]-k[0])
    elif len(k)==1:
        print(0)
    elif len(k)==0:
        print(-1)
