import string  # string에 포함된 메서드 .digits를 사용하기 위해 import 하는 듯?

tmp = string.digits+string.ascii_lowercase  # tmp에 모두 소문자를 넣어 16진법 이상도 가능하게끔 만들어줌


def convert(num, base):  # n진법 -> n진법으로 가는 convert 생성
  q, r = divmod(num, base)
  if q == 0:
    return tmp[r]
  else:
    return convert(q, base) + tmp[r]


N, B = map(str, input().split())  # N 문자열, B 진법 입력

print(convert(int(N, int(B)), 10))  # B 진법 -> 10진법 변환
