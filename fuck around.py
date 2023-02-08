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