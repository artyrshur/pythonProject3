a = int(input())
number = 1
iter = 0
for i in range(a):
    for b in range(i):
        print(i, end=' ')
        iter+=1
        if iter == a:
            break
    if not (iter == a):#прекращает цикл
        continue
    break