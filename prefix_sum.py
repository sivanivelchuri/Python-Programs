def prefix_sum():
    n=100
    prefix_sum=[i for i in range(n+1)]
    for j in range(1,n):
        prefix_sum[j]=prefix_sum[j-1]+prefix_sum[j]
        print(prefix_sum[j])
    return prefix_sum
prefix_sum()
