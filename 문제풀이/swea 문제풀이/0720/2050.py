alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


n = input()
for i in range(1, len(n)+1):
    print(i, end = ' ')
for z in range(len(alpha)):
    alpha[z] = i
print(alpha[z], end = ' ')