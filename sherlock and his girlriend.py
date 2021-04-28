def prime_factors():
    n=25
    seive=[i for i in range(n+1)]
##    print(seive)
    i=2
    while i*i<=n:
        for j in range(i*i,n+1,i):
                if seive[j]%i==0:
                    seive[j]=2
        i+=1
    for k in range(2,n+1):
        if seive[k]==k:
            seive[k]=1
    seive[0]=1
    seive[1]=1
    return seive
seive=prime_factors()
n=int(input())
if n<3:
    print(1)
else:
    print(2)
i=1
c=0
if n!=3:
    for j in range(i,n+1):
        print(seive[j],end=" ")
        
else:
    for j in range(i+1,n+2):
        print(seive[j],end=" ")
