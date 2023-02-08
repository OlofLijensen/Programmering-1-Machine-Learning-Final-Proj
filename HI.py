n = int(input("hur många med grönt: "))
m = int(input("hur många utan grönt: "))
gånger = 0


if n == m:
    gånger = 3

elif n % 2 == 0:
    gånger += 2
    while m > 0:
        m = m - n
        gånger += 1
    if m > -2:
        gånger -= 1
else:
    gånger += 3
    while m > 0:
        m = m - n
        gånger += 1
tid = gånger * 10
print(tid)