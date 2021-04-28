##BRUTE FORCE METHOD:---->O(n**2)
'''n=list(map(int,input().split()))
sorted(n)
d=int(input())
c=0
for i in range(len(n)-1):
    for j in range(i+1,len(n)):
        if (n[i]+n[j])%d==0:
            print([n[i],n[j]])
            c+=1
if c>0:
    print(c)
else:
    print("0")'''
##O(n) method
n=list(map(int,input().split()))
sorted (n)
d=int(input())
dic={}
for i in n:
    m=i%d
    if m not in dic:
        dic[m]=1
    else:
        dic[m]+=1
p=0
for i in dic:
    diff=d-i
    if diff in dic:
        p+=dic[i]*dic[diff]
        dic[i]=0
print(p)
        
