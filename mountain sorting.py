arr=list(map(int,input().split()))
x=arr.index(max(arr))
arr1=arr[0:x]
arr2=arr[x+1:]
s1=0
s2=0
p=[]
q=[]
sorted(arr1)
arr2.sort(reverse=True)
for i in arr1:
    if arr1.count(i)==1:
        p.append(i)
        s1=1
for i in arr2:
    if arr2.count(i)==1:
        q.append(i)
        s2=1
if s1==1 and s2==1:
    print("TRUE")
else:
    print("FALSE")
        
        
        
