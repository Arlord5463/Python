a, b, c, d, e = map(int, input().split())
min_a = a
max_a = a

if b < min_a:
    min_a = b
if c < min_a:
    min_a = c
if d < min_a:
    min_a = d
if e < min_a:
    min_a = e

if b > max_a:
    max_a = b
if c > max_a:
    max_a = c
if d > max_a:
    max_a = d
if e > max_a:
    max_a = e

print(min_a, max_a, sep='\n')
