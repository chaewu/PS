a, b = map(int, input().split())
c, d = map(int, input().split())

list = []

list.append(a / c + b / d)
list.append(c / d + a / b)
list.append(d / b + c / a)
list.append(b / a + d / c)

list_max = max(list)
print(list.index(list_max))