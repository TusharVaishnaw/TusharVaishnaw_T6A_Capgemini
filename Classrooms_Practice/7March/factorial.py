import sys
sys.setrecursionlimit(1030)
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

print(fact(int(input('enter num: '))))
