# 테스트케이스 마다 한줄에 하나씩 출력해야 한다.
#
# n이 완전수라면, n을 n이 아닌 약수들의 합으로 나타내어 출력한다(예제 출력 참고).
#
# 이때, 약수들은 오름차순으로 나열해야 한다.
#
# n이 완전수가 아니라면 n is NOT perfect. 를 출력한다.

while True:
  n = int(input())
  if n == -1:
    break
  arr = []
  for i in range(1, n):
    if n % i == 0:
      arr.append(i)
  if sum(arr) == n:
    print(n, " = ", " + ".join(str(i) for i in arr), sep="")
  else:
    print(n, "is NOT perfect.")
