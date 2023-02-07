p, k = map(int, input().split())

prime = [False, False] + [True] * (k-2)
for i in range(2, int(k**0.5)+1):
    if prime[i]:
        for j in range(i+i, k, i):
            if prime[j]:
                prime[j] = False
                
flag = True
for i in range(2, k):
    if prime[i]:
        if p % i == 0:
            flag = False
            break
            
if flag:
    print('GOOD')
else:
    print('BAD', i)