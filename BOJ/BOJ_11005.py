import string

tmp = string.digits+string.ascii_lowercase  # tmp에 모두 소문자를 넣어 16진법 이상도 가능하게끔 만들어줌


def convert(num, base):  # n진법 -> n진법으로 가는 convert 생성
  q, r = divmod(num, base)
  if q == 0:
    return tmp[r]
  else:
    return convert(q, base) + tmp[r]


N, B = map(str, input().split())  # 10진법 수 N, 진법 수 B

print(convert(int(N), int(B)).upper())  # 아잇 왜 답을 대문자로 출력해야만 하는거야.
