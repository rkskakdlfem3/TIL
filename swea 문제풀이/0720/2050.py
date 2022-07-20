#문자 입력받기
T = input()
#아스키 코드에서 빼줄 값
a = 64
for i in T :
#출력하기
    print(ord(i)-a, end=' ') 