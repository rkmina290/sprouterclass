t = int(input())
x=1
for i in range(t):
    a, b = (list(map(int, input().split())))
    print("\n[ Case #", x, "]", a,"+",b,"=", a+b)
    x= x+1