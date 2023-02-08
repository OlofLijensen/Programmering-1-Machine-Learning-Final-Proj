ett = int(input("antal 1: "))
två = int(input("antal 2: "))
tre = int(input("antal 3: "))
fyr = int(input("antal 4: "))

ettkraft = ett
tvåkraft = två * 2
trekraft = tre * 3
fyrkraft = fyr * 4

tot = ettkraft + tvåkraft + trekraft + fyrkraft
if tot % 2 == 0 :
    if ett == två == tre == fyr:
        print(ett, "0", "0", fyr)
    elif ett % 2 == 0 and två % 2 == 0 and tre % 2 == 0 and fyr % 2 == 0:
        hälften1 = ett/2
        hälften2 = två / 2
        hälften3 = tre / 2
        hälften4 = fyr/ 2
        hälften1 = int(hälften1)
        hälften2 = int(hälften2)
        hälften3 = int(hälften3)
        hälften4 = int(hälften4)

        print(hälften1, hälften2, hälften3, hälften4)
    elif ettkraft + fyrkraft == trekraft + tvåkraft:
        print(ett, "0", "0", fyr)
    elif ettkraft + tvåkraft + trekraft == fyrkraft:
        print(ett, två, tre, "0")
    elif fyrkraft + tvåkraft + trekraft == ettkraft:
        print(ett, "0", "0", "0")
    elif ettkraft + fyrkraft + trekraft == trekraft:
        print("0", "0", tre, "0")
    elif ettkraft + fyrkraft + trekraft == tvåkraft:
        print("0", "0", tre, "0")
    else:
        if ettkraft == tvåkraft:
            if fyrkraft == trekraft:
                print(ett,"0", tre, "0")
        elif tvåkraft == trekraft and ettkraft == fyrkraft:
            print(ett, "0", "0", fyr )

else:
    print("går inte")