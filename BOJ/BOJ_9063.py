N = int(input())

x_list = []  # 각각 x값과 y값을 저장할 리스트 생성
y_list = []

for i in range(N):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

if max(x_list) == min(x_list) or max(y_list) == min(y_list):
    print(0)
else:
   print((max(x_list) - min(x_list)) * (max(y_list) - min(y_list)))
