x, y = map(int, input().split())

value = x*1000 / y
n = int(input())

for i in range(n) :
    A, B = map(int, input().split())
    val2 = A*1000 / B
    if val > val2 :
        val = val2

print(round(val, 2))