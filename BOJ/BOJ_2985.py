a, b, c = map(int, input().split())

if a+b == c: # 무슨 이딴 하드코딩 방식의 알고리즘이 다 있을까.. 답을 찾아봤지만 다시 풀어봐야겠다
    print(f"{a}+{b}={c}")
elif a-b == c:
    print(f"{a}-{b}={c}")
elif a*b == c:
    print(f"{a}*{b}={c}")
elif a//b == c:
    print(f"{a}/{b}={c}")
elif a == b+c:
    print(f"{a}={b}+{c}")
elif a == b-c:
    print(f"{a}={b}-{c}")
elif a == b*c:
    print(f"{a}={b}*{c}")
elif a == b//c:
    print(f"{a}={b}/{c}")
