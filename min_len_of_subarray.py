n=[2,3,1,2,4,3]
z=[]
s=7
i=0
cur_sum=0
for j in range(0,len(n)):
    cur_sum+=n[j]
    while cur_sum>=s:
        z.append(len(n[i:j+1]))
        cur_sum-=n[i]
        i+=1
print(min(z))
