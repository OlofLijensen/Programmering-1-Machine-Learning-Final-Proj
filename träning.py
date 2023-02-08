word = input("write a word: ")
print(len(word))
print(word[0: 3])
print(word.find("a"))
print(word.islower())

sentence = input("write a sentence: ")
words = int(sentence.count(" ")) + 1
print(words)
print(sentence.rfind("a"))
print(sentence.endswith("."))
print(sentence.swapcase())


