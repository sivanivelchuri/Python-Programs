##USING RECURSION
##def game_coordinate(a,b,x,y):
##    if a>x or b>y:
##        return 0
##    if a==x and b==y:
##        return 1
##    return game_coordinate(a+b,b,x,y) or game_coordinate(a,b+a,x,y)
##a,b=1,1
##x,y=5,4
##if game_coordinate(a,b,x,y):
##    print("Possible")
##else:
##    print("No Path")




##USING EUCLID ALG 
def game_coordinate(x,y):
    while y:
        if x>y:
            temp=x
            x=y
            y=temp
        y=y%x
    return x
for i in range(int(input())):
    x,y=map(int,input().split())           
    gcd=game_coordinate(x,y)
    if gcd==1:
        print("YES")
    else:
        print("NO")




















