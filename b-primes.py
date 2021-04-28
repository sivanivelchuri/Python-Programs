def seive_gen():
    seive=[1]*n
    i=2
    while (i*i<=n):
        if seive[i]==1:
            for j in range(i*i,n,i):
                seive[j]=0
        i+=1
    seive[0]=0
    seive[1]=0
    return seive
def check(n):
    for i in range(2,n):
        y=i
        z=n-y
        if seive[y]==1 and seive[z]==1:
            print(y, z)
            break
    else:
        print(-1)
n=int(input())
seive=seive_gen()
check(n)
