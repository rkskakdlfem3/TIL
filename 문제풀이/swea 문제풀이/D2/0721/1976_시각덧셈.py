#테스트케이스 입력받기
t = int(input())
for i in range(1, t+1):
#시각 두개 입력받기
    h1, m1, h2, m2 = map(int, input().split())
#시각 더하기
    h = h1 + h2
    m = m1 + m2
#더한 시각 제한두기(h=1~~12, m= 0~59)
    if m > 60:
        h = h + 1
        m = m - 60
    if h > 12:
        h = h - 12 

#정답 출력하기
    print(f'#{i} {h} {m}')