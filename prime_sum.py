def prime_seive():
    n=100
    prime=[1]*n
    prime[0]=prime[1]=0
    for i in range(2,n):
        if prime[i]==1:
            for j in range(i*i,n,i):
                prime[j]=0
    return prime
prime=prime_seive()
n=int(input())
for i in range(0,n):
    if prime[n-i] and prime[i]:
        print(n-i,i)
        break
