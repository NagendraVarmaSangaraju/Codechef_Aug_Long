# cook your dish here
t = int(input())

for i in range(t):
    h, p = map(int,input().split())
    if(p*2>h):
        print(1)
    else:
        print(0)
