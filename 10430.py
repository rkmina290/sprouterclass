a,b,c=(list(map(int, input().split())))

if 2<=a and b and c<=10000:
    print((a+c)%c)
    print(((a%c) + (b%c))%c)
    print((a*b)%c)
    print(((a%c) * (b%c))%c)