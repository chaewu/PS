# # 정답 코드 참고 파일
#
# # 1929
# def isPrime(num):
#     if num==1:
#         return False
#     else:
#         for i in range(2, int(num**0.5)+1):
#             if num%i == 0:
#                 return False
#         return True
#
# M, N = map(int, input().split())
#
# for i in range(M, N+1):
#     if isPrime(i):
#         print(i)

n, m = map(int, input().split())

if n <= m:
    n, m = m, n

rsnd = list(range(n, m + 1))

print(*rsnd)
