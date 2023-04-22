# 알파벳 튜플 생성
alphabet = {'A', 'B', 'C', 'D', 'E', 'F',
            'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z'}

T = int(input())

# 입력 데이터 수만큼 반복
for _ in range(T):
  s = set(input())  # 입력받은 문자열 set으로 튜플 만들기
  a = alphabet-s  # 차집합 구하기
  res_sum = 0
  for i in a:
    res_sum += ord(i)
  print(res_sum)  # 출력
