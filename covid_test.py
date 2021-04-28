def result(y):
    for i in range(len(y)):
        if y[i] in x:
            c=1
            del x[:x.index(y[i]):1]
        else:
            return "NEGATIVE"
    if c==1:
        return "POSITIVE"
virus_name=input()
t=int(input())
for _ in range(t):
    n=input()
    x=list(virus_name)
    y=list(n)
    print(result(y))
