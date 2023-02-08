torstid = int(input("Tors tid:"))
Mortstid = int(input("Mors tid"))
max = 38
antal_tors = 1
antal_mors = 1
tid = 0

while max > 0:
    tid += 1
    if tid % torstid == 0 and tid % Mortstid == 0 and max == 1:
        max -= 1
    elif tid % torstid == 0 and tid % Mortstid == 0:
        max -= 2
        antal_mors += 1
        antal_tors += 1
    elif tid % torstid == 0 and tid >= torstid:
        antal_tors += 1
        max -= 1
    elif tid % Mortstid == 0 and tid >= Mortstid:
        antal_mors += 1
        max -= 1

print("antal Tor: ",antal_tors, "," + "antal Mor: ", antal_mors)
#om de inte ska äta samtidigt
torstid = int(input("Tors tid(inte samtidigt):"))
Mortstid = int(input("Mors tid"))
max = 38
antal_tors = 1
antal_mors = 1
tid = 0

while max > 0:
    tid += 1

    if tid % torstid == 0 and tid % Mortstid == 0:
        max += 0
    elif tid % torstid == 0 and tid >= torstid:
        antal_tors += 1
        max -= 1
    elif tid % Mortstid == 0 and tid >= Mortstid:
        antal_mors += 1
        max -= 1

print("antal Tor: ",antal_tors, "," + "antal Mor: ", antal_mors)
