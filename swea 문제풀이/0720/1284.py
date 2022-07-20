# 테스트 케이스 숫자 표시
test_case = int(input())
for test in range(test_case+1):
# a사 = W리터*p원
# b사 = Q 원(R리터 이하인 경우), 
#       (W-R)*S+Q(R리터 이상인 경우)


# P(A사의 1리터당 요금), Q(B사의 R리터 이하 요금), 
# R(B사의 기준 리터), 
# S(B사의 R리터 이상일때의 1리터당 요금)
# W( 한 달간 사용한 수도의 양) 순으로 INPUT

# PQRSW  입력 받기
    P,Q,R,S,W = map(int, input().split())
# A 계산하기
    A = W * P
# B 계산하기(한달 수도량 R 리터 이하인 경우)
    if R > W:
        B = Q
# B 계산하기(한달 수도량 R 리터 이상인 경우)
    else:
        B = (W -R)*S + Q
#결과 출력하기
print(f'#{test} {min(A, B)}')