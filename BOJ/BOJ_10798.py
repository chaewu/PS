wordList = [[0] * 15 for i in range(5)]  # 이차원 리스트 생성

for i in range(5):
    word = list(input())
    wordLength = len(word)

    for j in range(wordLength):
       wordList[i][j] = word[j]

for i in range(15):
    for j in range(5):

        ifwordList[j][i] == 0: # 문자열이 없으면 continue
            continue

        else:
            print(wordList[j][i], end='')
