from copy import deepcopy
t = int(input())
for _ in range(t):
    s = list(input())
    p = list(input())
    for i in p:
        s.remove(i)
    s.sort()
    r = deepcopy(s)
    r.append(p[0])
    r = sorted(r, reverse= True)
    if p[0] not in s:
        print(''.join(s[0:len(r) - r.index(p[0]) - 1 ]) + ''.join(p) + ''.join(s[len(r) - r.index(p[0]) - 1:]))
    else:
        a = ''.join(s[0:s.index(p[0])]) + ''.join(p) + ''.join(s[s.index(p[0]):])
        print(min(a, ''.join(s[0: len(r) - r.index(p[0]) - 1 ]) + ''.join(p) + ''.join(s[len(r) - r.index(p[0]) - 1:])))
