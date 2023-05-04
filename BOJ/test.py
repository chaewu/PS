t = [list(map(int, input().split())) for _ in range(7)]
v = [[0 for _ in range(7)] for _ in range(7)]

def dfs(x, y, p):  
  if x<0 or x>6 or y<0 or y>6:
    return 0
  if not v[x][y] and t[x][y] == p:
    v[x][y] = t[x][y]
    return 1+dfs(x-1,y,p)+dfs(x+1,y,p)+dfs(x,y-1,p)+dfs(x,y+1,p)
  return 0

s = 0
for i in range(7):
  for j in range(7):
    if dfs(i, j, t[i][j]) >= 3:
      s += 1      
print(s)
