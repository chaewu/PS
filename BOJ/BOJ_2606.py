# 어우; DFS 어려운거봐
n = int(input())  # 컴퓨터 개수
v = int(input())  # 연결선 개수
graph = [[] for i in range(n + 1)]  # 그래프 2차원 배열로 초기화
visited = [0] * (n + 1)  # 방문한 컴퓨터 표시

for i in range(v):  # 그래프 생성
    a, b = map(int, input().split())
    graph[a] += [b]  # a에 b 연결
    graph[b] += [a]  # b에 a 연결 -> 양방향


def dfs(ver):
    visited[ver] = 1
    for i in graph[ver]:
        if visited[i] == 0:
            dfs(i)


dfs(1)

print(sum(visited) - 1)
