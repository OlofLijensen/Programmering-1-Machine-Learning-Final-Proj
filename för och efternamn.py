N = int(input("ange tavlans:"))
table = []
for i in range(N):
    table.append(".")
for J in range(N):
    nyrad = []
    for i in range(N):
        nyrad.append(".")
    table[J] = nyrad

table[2][2] ="M"
for row in table:
   print(row)

