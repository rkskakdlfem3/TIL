#테스트 케이스 수 t 받기
T = int(input())
# 테스트 케이스 1번부터 T번까지
for x in range(1, T+1):
    #n 입력받기
    n = int(input()) 
    #0~9까지 중복 방지용 집합 만들기
    s = set()
#양세기(N, 2N, 3N, ...KN)
    while len(s)<11:
        for z in range(1, n+1):
            count = z * n
            for char in str(count):
                s.add(char)
# 볼때 양 세기 멈추기
           
#테스트 케이스 번호, 결과 출력하기
print(f'#{T} {z}')