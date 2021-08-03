line = int(input())
column = int(input())
line2 = int(input())
column2 = int(input())
if (line > 0 and line2 > 0 and column > 0 and column2 > 0) or (line < 0 and line2 < 0 and column < 0 and column2 < 0) or (line > 0 and line2 > 0 and column < 0 and column2 < 0) or (line < 0 and line2 < 0 and column > 0 and column2 > 0):
    print('YES')
else:
    print('NO')