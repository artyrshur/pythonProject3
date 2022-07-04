a = int(input())#input int when sum != 0 than print sqr this int
s = a
b = 1
while True:
    a = int(input())
    s+=a
    b+=a**2
    if s == 0:
        print(b)
        break