t = int(input())
for i in range(t):
    c, r = map(int, input().split())
    
    if(c%9 == 0):
        c1 = int(c/9)
    else:
        c1 = int(c/9) + 1
    
    if(r%9 == 0):
        r1 = int(r/9)
    else:
        r1 = int(r/9) + 1
    
    # print(c1, r1)
    if (c1==r1):
        # if(c1==0):
        #     print(1, c1+1)
        # else:
        print(1, c1)
    if(c1<r1):
        print(0, c1)
    if(r1<c1):
        print(1, r1)
        
            
        
