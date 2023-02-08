try:
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
except:
    print("fuck you")
