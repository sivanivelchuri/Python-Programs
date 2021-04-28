for _ in range(int(input())):
    n=int(input())    
    c=0
    for i in range(1,n//2+1):
        if n%i==0:
            c+=i
    if c==n:
        print("YES")
    else:
        print("NO")
