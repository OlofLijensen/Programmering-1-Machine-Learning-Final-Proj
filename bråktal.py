from subprocess import call
import random

#Rätt så simpelt tar in tal till random rangen om talen är mindre än 0 fångas de upp av if 'statment' om de inte är siffror så fångas de upp av try och except
try:
  print("antalen du nu skriver kommer komma in i en rand range fast gångras med 10 och skriva antal 'hey'")
  a = int(input("skriv det lägsta talet som du vill kunna få: "))
  if a < 0:
       print("skriv ett positivt heltal.")
       exit()
  b = int(input("skriv det högsta talet som du vill kunna få: "))
  if b < 0:
       print("skriv ett positivt heltal.")
       exit()

except ValueError and TypeError:
     print("Du skrev inte in ett heltal, skriv in en siffra tack!")

#vi använder de två input till våran range av random sedan skappar vi en ny fil för varje itiration av random talet, filet har samma namn varje gång så det blir inte nya
#Sedan inom filen görs en for looper som skriver 10 'hey' för varje random tall range
#För att sist få med break och inte slösa på datorns krafter för mycket så har jag begränsat for loppen till 10 itirationer

else:
 n = random.randint(a, b)
 for m in range(n):
  with open('bråkta.py', 'w') as f:
      f.write('''
hey_count = 0
hey = True
while hey:
  print("hey")
  hey_count += 1
  print(hey_count)
  if hey_count >= 10:
       break
               ''')
  if m >= 10:
    break

  call(["python", "bråkta.py"])

  f.close()

