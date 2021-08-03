line = int(input())
column = int(input())
line2 = int(input())
column2 = int(input())
if line - line2 == column - column2 or line - line2 == column2 - column:
    print('YES')
else:
    print('NO')
