def seive_gen():
    seive=[1]*(N)
    seive[0]=0
    seive[1]=0
    i=2
    while i*i<N:
        for j in range(i*i,N,i):
            if seive[i]==1:
                seive[j]=0
        i+=1
    return seive
def prime_seive_gen():
    prime_seive=[]
    for i in range(2,N):
        if seive[i]==1:
            prime_seive.append(i)
    return prime_seive
def check_tprimes(n):
    s1,c,i=0,0,0
    while n>=prime_seive[i]:
        s1=prime_seive[i]+prime_seive[i+1]+1
        if s1 in prime_seive and s1<=n:
            c+=1
        i+=1
    if c<k:
        print("NO")
    else:
        print("YES")
N=10000
seive=seive_gen()
prime_seive=prime_seive_gen()
n,k=map(int,input().split())
check_tprimes(n)
    
