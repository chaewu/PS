N, M = map(int, input().split())

ball_basket = [i + 1 for i in range(N)]

for _ in range(M):
    i, j, k = map(int, input().split())

    ball_basket = ball_basket[:i - 1] + ball_basket[k - 1:j] + ball_basket[i - 1:k - 1] + ball_basket[j:] # 아니 이게 왜 한줄로 되지? 개어이 없다
    # 대충 회전 시작 값 i, 회전 종료 값 j, 회전 중간 값 k를 k ~ j 까지 + i ~ k 까지 붙혀주는 코드 (사실 이해 안됨)
print(*ball_basket)
