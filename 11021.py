t = int(input())
n=1
for i in range(t):
    a, b = (list(map(int, input().split())))
    print("\nCase #", n,":", a+b)
    n= n+1