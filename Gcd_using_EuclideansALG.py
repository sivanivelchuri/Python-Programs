def gcd(a,b):
    if a==0:
        return b
    gcd1=gcd(b%a,a)
    return gcd1
a,b=map(int,input().split())
print(gcd(a,b))
