a = int(input())
for i in range(a):
    b = int(input())
    sum = 0
    for z in range(1,b+1):
        if z % 2 == 0:
            sum -= z
        else:
            sum += z
    print( f"#{i+1}", sum)