import sys
input = sys.stdin.readline

from collections import defaultdict


count = {i:[] for i in range(1, 100001)}
words = defaultdict(int)
N, M = map(int, input().split())
for _ in range(N):
    word = input().rstrip()
    if len(word) < M:
        continue
    else:
        words[word] += 1

for i in words:
    count[words[i]].append(i)

for j in range(N, 0, -1):
    if count[j]:
        count[j].sort(key=lambda x:(-len(x), x))
        print(*count[j], sep='\n')
