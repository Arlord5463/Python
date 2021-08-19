lst = input().split()
x = int(input())
m = 0
for i in range(len(lst)):
    lst[i] = int(lst[i])
for j in range(len(lst)):
    if lst[j] == x:
        m += 1
        print(j, end=' ')
if m == 0:
    [print('Отсутствует')]
