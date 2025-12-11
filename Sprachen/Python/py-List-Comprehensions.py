
# A1
numbers = [42, 87, 13, 29, 65, 98, 7, 54, 33]
print("ungerade Zahlen:", [i for i in numbers if i % 2 != 0])


# A2
languages = ["Python", "Java", "JavaScript", "C++", "Ruby"]
print("Wortlängen:", [len(lan) for lan in languages])


# A3
words = ["Hallo", "Hello", "Ciao", "Hola", "Bonjour"]
print("Short words:", [word.upper() for word in words if len(word) < 5])


# A4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
collatz = []

for number in numbers:
	if number % 2 == 0:
		collatz.append(number // 2)
	else:
		collatz.append(3 * number + 1)
print(collatz)