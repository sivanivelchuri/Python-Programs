arr=[12,2,3,4,7,6]
t=9
cur_sum=0
j=0
for i in range(len(arr)):
    cur_sum+=arr[i]#5
    while(cur_sum>t):#12>9
        cur_sum-=arr[j]#0
        j+=1
    if cur_sum==t:
        print(arr[j:i+1])
        print('yes')
    
        
