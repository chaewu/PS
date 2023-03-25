N = int(input())
S = input()
moem_list = ['a', 'e', 'i', 'o', 'u']
count = 0


for j in range(len(moem_list)):
  if S.find(moem_list[j]) != -1:
    count += S.count(moem_list[j])


print(count)
