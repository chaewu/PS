N = int(input())

while True:
  temp = int(input())

  if temp == 0:
    break

  if temp % N == 0:
    print("%s is a multiple of %s." % (temp, N))
  else:
    print("%s is NOT a multiple of %s." % (temp, N))
