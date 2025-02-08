# uppgift 1
# 1.1
# Ett borde vara en string men eftersom det inte är inom citat tecken så kommer det inte att fungera
# a är det egentligen samma problem så om man skriver det inom citat tecken så kommer det vara en String
# 4 är en interger
# 3.6 är en float
# True är en Boolean
# 'True' är en string

# 1.2
# variabel1 = 'a,b,c' har datatyp string
# a = 10 är en interger
# alpha = True är boolean
# variabel2 = a är tekniskt sätt inget ( inga '')
# variabel3 = 1 är en interger
# variabel b samt variabel5 = alpha är inget eftersom inget ''
# variabel2 variavel4 samt variabel kommer alla tre att generera fel medelande fast endast variabel2 kommer att printa ut ett fel eftersom det är högst upp

# 1.3
# print(1/3) kommer att skriva float value av 1/3 alltså 10 decimaler av 3
# print('1/3') kommer att printa 1/3
# a = 1/3 print(a) kommer vara dessama som att skriva print(1/3)
# print('a') kommer att skriva ut a

# annaÅlder = 20
# annaSkola = 'inte' eller annaSkola = False
# annaLängd = 160
# t.ex känner det värde löst att skriva 2 till då det är samma fast ändra siffror och true samma ändra namn på variabeln

# 2.1
# funktionen räknar ut hur stor en area mellan sida 1 och sida 2 skulle vara
# den tar int intergers som datatyp
# den returnar en interger
# det här är då funktione BeräknaArea
# däremot alternativBeräknaArea har ingen return statment så man får ingen int tillbaka
# adderar två int som de får i argumentet och sedan retunar summan
# funktion får in två ints och sedan gångrar de två och sedan adderar de andra talet efter.(sedan även returnar)
# den andra funktionen adderar de två intsen och sedan printar det direkt
# sista funktionen tar första inten gånger sig själv plus andra int gånger sig själv och sedan roten ur de talet

# 2.2
# jag täntke de eftersom det är roten ur a**2 + b**2 roten ur
import numpy as np
def vektorLängd(a, b):
 c = np.sqrt(a*a + b*b)
 return c

# tar in argument a, b som ints och returnar c som float
# täntke att den går direkt till print utan att man får någon return
def addDirekt(x, y):
 print(x+y)
# tar in x, y ints strings float
def add(x, y):
 return(x+y)
# tar två arguments returnar strings float ints

# 2.3
# tar in 4 argument 4ints dock en kan vara float a = startlön  b = löneökning i procent c = hur ofta lönen ökas i månader  D = hur länge du jobbar i år z = endast en tickande variabel som ökas med 1 för varje it av loop max = hur mycket tot
def stabilLöneÖke(a, b, c, d,):
 z = 0
 max = 0
# ändars till månader så den hör ihop med resten
 d = d * 12

 while d > z:
  z += 1
# Ökar lönen stegviss beroende på när lönen bör ökas
  if z % c == 0:
   a = a * (1 + b/100)
  max += a
 return max, a
a = int(input("vad är start lönen?"))
b = float(input("hur mycket ökas lönen med"))
c = int(input("hur ofta ökas lönen(månader)"))
d = int(input("hur många år täntke du jobba?"))
print(stabilLöneÖke(a, b, c, d))



# 3.1
a = input()
b = input()
print(a + b)
# det läggs helt eneklt bara bredvid varan b börjar där a slutar

def hälsning(namnen):
 for namn in namnen:
  print("Hej " + namn)

namn = input("Vilka namn ska jag hälsa på: ")
namn = namn.split()
hälsning(namn)

tot = 0
tot = int(input("skriv ett tal:"))
print("möjliga räknesätt +, -, *, /, **, sqrt, %, //, om du vill avsluta skriv End i operator frågan")
while True:
   print(tot)
   operator = input("skriv din operator")
   if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "//" or operator == "%":
      talny = int(input("skriv ett tal2:"))
      if operator == "+":
        tot += talny
      elif operator == "-":
        tot -= talny
      elif operator == "*":
        tot *= talny
      elif operator == "/":
        tot /= talny
      elif operator == "%":
        tot %= talny
      elif operator == "//":
        tot //= talny
   elif operator == "sqrt":
     tot = (tot ** (1 / 2))
   elif operator == "**" or operator == "^":
     a = int(input("hur mycket vill du upphöja tot med"))
     tot = (tot ** a)
   elif operator == "END" or operator == "end" or operator == "End":
      break

# En väldigt dum calc som tar en operator i taget och gör kalken antinge på tot värdet du har eller läger till eller va fan till tot värdet.
# 3.3

# 3.3
print("|._.|\t |._.|\t |._.|\t")
print(" 0-0    (---)   /---/")
print(" | |     | |     | |")

# 3.4
a = input("write a pass")
if len(a) > 8:
    print("the pass is to long")
a = ([*a])

for letters in a:
    if letters == "å" or letters == "ö" or letters == "ä":
        print("not allowed to have swedish letters")
        exit()
print("good no swedish")
for a in a:
  x = a.isdigit()
  if a.isdigit():
     print("yes")
     break
  else:
    print("oh no")

if x == True:
  print("good passowrd")
# 4.1
a = input("skriv")
a = ([*a])
b = 0
c = 0
for elements in a:
    if elements.isdigit():
        c += 1
    elif elements.isalpha():
        b += 1
print("så många bok", b, "så många tal", c)

# 4.2
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

# 6
UserInput = ""
# Try hela är för lat för att gå in i varje del
try:
 while UserInput != "exit": # skapar en loop som avslutar då använderen skriver exit vid meny inputen
    print("Choose a funktion")
    print("Put in the number of the funktion you want to use(write 'exit' if you wanna close this app)")
    print("  1. speedCalc")
    print("  2. areaCalc")
    UserInput = input("  Write here:")
    print("")

    if UserInput == "1": # om dom skriver 1 så kommer de hit en simpel räknare
        def speedCalc(a, b):
            c = a / b
            return (c)


        a = int(input("Write the distance in Meters: "))
        b = int(input("write how long it took in sec: "))

        if a >= 0 and b >= 0: # förhindrande arbete
          print("Your average speed was", speedCalc(a, b))
          print("")
        else:
            print("can not have negative values!")
            exit()

    elif UserInput == "2":
        def areCalc(a, b):
            c = a * b
            return c


        a = float(input("Write how long the first side is? "))
        b = float(input("Write how long the second side is? "))
        if a >= 0 and b >= 0:
          print("Your area size is", areCalc(a, b))
          print("")
        else:
            print("can not have negative values!")
            exit()

    elif UserInput == "exit": #liten trevlig exit på vår loop
      print("  bye!")
      exit()

    else: # Om de skriver något helt annat :)
        print("please read the instructions more carefully bye!!")
        exit()
except ValueError: # förhindrar då det blir annat än siffror vid räknandet
    print("You wrote something dum, dum dum!")

# 7
a = 0
b = 0
elever = ['Axel', 'Johan', 'Johanna', 'Oscar', 'Bill']
nummer = [1, 3, 4, 6, 2, 5]
eleverSorted = sorted(elever)
nummerSorted = sorted(nummer)
print(eleverSorted)
print(nummerSorted)
for elements in eleverSorted:
    a += 1
    print(elements)
    if len(eleverSorted) == a:
        print("inte tom")
for elements in nummerSorted:
    b += 1
    print(elements)
if len(nummerSorted) == b:
    print("inte tom")
else:
    print("något är fel")
eleverKopia = elever.copy()
print(eleverKopia)
basgrupp = []
nybasgrupp = []
print(nummerSorted)
nummerSorted.reverse()
print(nummerSorted)
# Kan inte ändra värden, annars fungerar den som en vanlig lista
