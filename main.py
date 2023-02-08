try:
 firstNumber = float(input("write your first number: "))
 SecondNumber = float(input("write your second number: "))
 mathSymbol = input("write your math symbol + / - *: ")

 if mathSymbol == "+":
    print(firstNumber + SecondNumber)
 elif mathSymbol == "/":
    print(firstNumber/SecondNumber)
 elif mathSymbol == "-":
    print(firstNumber - SecondNumber)
 elif mathSymbol == "*":
    print(firstNumber * SecondNumber)
except ValueError:
  print('Invalid value please write a number!')