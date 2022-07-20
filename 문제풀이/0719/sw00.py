from distutils import bcppcompiler
import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tt in range(T):
    a, b = map(int, input().split())
    print( "#%d %d %d" % (tt+1, a//b, a%b) )