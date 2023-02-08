def fi(num):
   num1 = 1
   num2 = 1
   times = 1
   num -= 1


   while num > times:
      times += 2
      num1 += num2
      num2 += num1

   if num % 2 == 0:
      return num1
   else:
      return num2



deltagare = int(input("deltagare: "))
deltagare = fi(num) - deltagare
print(deltagare)