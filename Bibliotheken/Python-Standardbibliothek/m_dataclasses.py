from dataclasses import dataclass, field

# A1
@dataclass(order=True)
class Book:
	title: str = ""
	authors: list[str] = field(default_factory=list)
	year: int = 0
	isbn: str = ""
	# A8
	language: str = "en"
 

# A2
shelf = [
    	Book(title="Learning Python", year=2013),
        Book(title="Head First Python", year=2010),
        Book(title="Python Crash Course", year=2015)
        ]

# A3
print("\nA3:")
print(shelf[0].title)

# A4
print("\nA4:")
print([x.title for x in shelf])
shelf.sort()
print([x.title for x in shelf])

#A5
print("\nA5:")
print([(x.title, x.year) for x in shelf])
shelf[0].year = 2025
print([(x.title, x.year) for x in shelf])


# A6
@dataclass(frozen=True)
class ArchiveBook:
	title: str = ""
	authors: list[str] = field(default_factory=list)
	year: int = 0
	isbn: str = ""


archive_book = ArchiveBook(title="Head First Python", year=2010)

# A7
print("\nA7")
try:
    archive_book.title="Siuu"
except:
	print("Objekt_Error: Objekt ist unveränderbar.")


# A9
print("\nA9")
eng = Book(title="Duden")
print(f"{eng.title}, {eng.language}")
eng.language = "de"
print(f"{eng.title}, {eng.language}")


#A10
print("\nA10")
invalide_year = Book(title="Head First Python", year="Zweitausendsechzehn")
print(invalide_year)