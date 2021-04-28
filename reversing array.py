n=input()
arr=list(map(input().split()))
p=[]
j=0
for i in range(len(arr),0,-1):
    arr[j]=arr[i]
    p.append(arr[j])
    j+=1
print(p)
    
