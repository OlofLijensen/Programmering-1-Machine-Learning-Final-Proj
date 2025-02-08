from subprocess import call
import random

#Rätt så simpelt tar in tal till random rangen om talen är mindre än 0 fångas de upp av if 'statment' om de inte är siffror så fångas de upp av try och except
try:
  a = int(input("skriv det lägsta talet som du vill kunna få: "))
  if a < 0:
       print("skriv ett positivt heltal.")
       exit()
  b = int(input("skriv det högsta talet som du vill kunna få: "))
  if b < 0:
       print("skriv ett positivt heltal.")
       exit()

except ValueError:
     print("Du skrev inte in en siffra, skriv in en siffra tack!")

#vi använder de två input till våran range av random sedan skappar vi en ny fil för varje itiration av random talet, filet har samma namn varje gång så det blir inte nya
#Sedan inom filen görs en for looper som skriver 10 'hey' för varje random tall range
#För att sist få med break och inte slösa på datorns krafter för mycket så har jag begränsat for loppen till 10 itirationer

else:
 n = random.randint(a, b)
 for m in range(n):
  with open('bråkta.py', 'w') as f:
     f.write('n = 0\n')
     f.write('while 10 > n:\n')
     f.write('  n += 1\n')
     f.write('  print("hey")\n')
  call(["python", "called.py"])
  if m > 10:
      break
  f.close()


