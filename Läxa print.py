num1 = input("write num1: ")
num2 = input("write num2: ")
num3 = input("write num3: ")
num4 = input("write num4: ")

def hey(num1, num2, num3, num4):
 biggest = num1
 if num1 >= num2:
   if num1 >= num3:
       if num1 >= num4:
           biggest = num1
 elif num2 >= num3:
   if num2 >= num4:
       biggest = num2
 elif num3 >= num4:
   biggest = num3
 else:
   biggest = num4
 print(biggest)

 if biggest == num1:
   mid1 = num2
   mid2 = num3
   mid3 = num4
 elif biggest == num2:
   mid1 = num1
   mid2 = num3
   mid3 = num4
 elif biggest == num3:
   mid1 = num1
   mid2 = num2
   mid3 = num4
 else:
   mid1 = num1
   mid2 = num2
   mid3 = num3
 secBiggest = mid1
 if mid1 >= mid2:
   if mid1 >= mid3:
       secBiggest = mid1
 elif mid2 >= mid3:
   secBiggest = mid2
 else:
   secBiggest = mid3
 print(secBiggest)

