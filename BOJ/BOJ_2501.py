list = []
n, k = map(int,input().split())

for i in range(1,n+1):
    if n % i == 0:
        list.append(i)

list.sort()

if len(list) < k:
    result = 0
else:
    result = list[k-1]

print(result)