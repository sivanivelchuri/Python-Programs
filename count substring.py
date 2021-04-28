s="1111"
c=0
for i in range(len(s)):
    if s[i]=='1':
        print(i,s[i])
        c+=1
        print(c)
if c>1:
    print(c*(c+1)//2)
elif c==1:
    print("1")
else:
    print("0")
    
