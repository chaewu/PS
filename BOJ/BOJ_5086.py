# 출력 형식
# 각 테스트 케이스마다 첫 번째 숫자가 두 번째 숫자의 약수라면 factor를, 배수라면 multiple을, 둘 다 아니라면 neither를 출력한다.

while True:
  n, m = map(int, input().split())
  if (n == 0 and m == 0):
    break
  if (m % n == 0):
    print("factor")
  elif (n % m == 0):
    print("multiple")
  else:
    print("neither")
