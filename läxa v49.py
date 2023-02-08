import random as r


for n in range(10):
    print(r.randint(30, 50))

print("")

for n in range(5):
    print(r.uniform(1, 10))

print("")

for n in range(7):
    print(r.gauss(50, 25))

print("")

list = ['hej', 'nej' , 'ja', 'okej', 'kankse']
for n in range(4):
  print(r.sample(list, 2))

print("")

n = 0
while n <= 100:
    print(n)
    n += 1
    if n > 50:
        break

print("")

age = int(input("write your age: "))
name = input("write your name: ")

try:
 print(age + name)

except:
    print("där blev det lite fel")
    print("skriv istället '(str(age) + name') ")

dela = int(input("Skriv vad du vill dela två med: "))

try:
  print(2/dela)

except ZeroDivisionError:
    print("Även du borde veta att man inte kan dela med noll...")

except ValueError:
    print("Herregud skriv ett tal tack")



