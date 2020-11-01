t = int(input())

for t in range(t):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    min = 0
    for l in range(n):
        if k%a[l]==0:
            min = int(k/a[l])
            # print (min)
            break
    ans = a[0]
    count = 0
    for j in range(n):
        if(k%a[j]==0):
            if((int(k/a[j]))<=min):
                min = int(k/a[j])
                ans = a[j]
                count = count+1
    if(count>0):
        print (ans)
    else:
        print(-1)
