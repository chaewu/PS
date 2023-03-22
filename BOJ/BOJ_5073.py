# 왜이리 지저분행 코드가

while True:
  triangle_list = list(map(int, input().split()))
  if triangle_list[0] == 0 and triangle_list[1] == 0 and triangle_list[2] == 0:
    break

  triangle_list.sort()

  if triangle_list[0] == triangle_list[1] and triangle_list[1] == triangle_list[2]:
    print("Equilateral")

  elif triangle_list[0] + triangle_list[1] <= triangle_list[2]:
    print("Invalid")

  elif triangle_list[0] == triangle_list[1] or triangle_list[0] == triangle_list[2] or triangle_list[1] == triangle_list[2]:
    print("Isosceles")

  elif triangle_list[0] != triangle_list[1] and triangle_list[0] != triangle_list[2]:
    print("Scalene")
