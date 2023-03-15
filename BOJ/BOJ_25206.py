rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

major = 0 # 학점 총 합
result = 0 # 학점 * 과목 평점

for _ in range(20):
  s, c, g = input().split() # subject (과목) , credit (학점) , grade (등급)
  c = float(c)
  if g != 'P':
    major += c
    result += c * grade[rating.index(g)]

print(result / major)
