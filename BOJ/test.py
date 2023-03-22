res = 0
ajsl = int(input())

while True:
  if ajsl // 50000 > 0:
    ajsl -= 50000
    res += 1

  elif ajsl // 10000 > 0:
    ajsl -= 10000
    res += 1

  elif ajsl // 5000 > 0:
    ajsl -= 5000
    res += 1

  elif ajsl // 1000 > 0:
    ajsl -= 1000
    res += 1

  elif ajsl // 500 > 0:
    ajsl -= 500
    res += 1

  elif ajsl // 100 > 0:
    ajsl -= 100
    res += 1

  elif ajsl // 50 > 0:
    ajsl -= 50
    res += 1

  elif ajsl // 10 > 0:
    ajsl -= 10
    res += 1

  else:
    break

print(res)
