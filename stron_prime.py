n=100
primes=[1]*n
strong_prime=[0]*n
def strongs(l,m,h):
    if 2*m>(l+h):
        return True
    return False
def create_seive():
    primes[0]=primes[1]=0
    l=2
    m=3
    for i in range(n):
        if primes[i]==1:
            curr=i
            if i>=5 and strongs(l,m,curr):
                print(l,m,curr)
                strong_prime[i]=1
            for j in range(i*i,n,i):
                primes[j]=0
            l=m
            m=curr
create_seive()
