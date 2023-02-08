

def fi(num):
   if num < 0:
      print("wrong input, should be greater then 0")
      exit()
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


print(fi(4))
