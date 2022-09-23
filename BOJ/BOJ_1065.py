n = int(input()) # 1 ~ n 까지의 한수(양의 정수 x의 각 자리가 등차수열을 이루는 수) 출력
                 # 등차수열 = 연속하는 각 항의 차이가 모두 일정한 수열 ex) 123 = 등차수열, 1과 2의 차이 1 | 2와 3의 차이 1 

han_num = 0 # 한수의 개수를 저장할 변수 초기화
for i in range(1, n + 1):   
    num_lst = list(map(int, str(i))) # i를 str로 바꿔 한자리씩 나눠 리스트에 저장해준다
    if i <= 99: # 2자리수의 경우 10의자리 숫자와 1의자리 숫자의 차이 1개만 존재하므로 어떤 수라도 한수가 된다.
        han_num += 1    # 그러므로 100 미만의 숫자는 모두 한수의 개수에 더해준다.
    elif (num_lst[0] - num_lst[1]) == (num_lst[1] - num_lst[2]):    # 각 항의 차이가 모두 같다면?
        han_num += 1                                                # 한수이므로 한수의 개수 += 1

print(han_num)