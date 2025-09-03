import argparse
import sqlite3
import pprint
import json

dbName = "m_sqlite3.db"
# A2
con = sqlite3.connect(dbName)
# A3
cur = con.cursor()

def create_db():

	print(f"Datenbank ´{dbName}´ wurde erstellt/verbunden und Cursor angelegt.")

	#A4
	cur.execute("""
		CREATE TABLE IF NOT EXISTS books (
			title TEXT PRIMARY KEY,
			genre TEXT,
			read INTEGER
		)
	""")

	# A5
	buecher = [("The Lord of The Rings", "Fantasy", 1), ("1984", "Fiction", 1), ("The Art of Computer Programming", "Monograph", 0)]
	cur.execute("""INSERT OR IGNORE INTO books VALUES 
					('The Lord of The Rings', 'Fantasy', 1),
					('1984', 'Fiction', 1),
					('The Art of Computer Programming', 'Monograph', 0)
				""")

	# A6
	con.commit()


def query_db():
	
	# A7
	res = cur.execute("SELECT COUNT(*) FROM books")
	count = res.fetchone()
	print("number of entries in 'books':", count[0])

	# A8
	res = cur.execute("SELECT TITLE FROM books WHERE genre = 'Fantasy'")
	fantasy = res.fetchall()
	pp = pprint.PrettyPrinter(indent=2, depth=2, sort_dicts=False)
	print("fantasy books:", end=" ")
	pp.pprint(fantasy)
	
	# A9
	res = cur.execute("SELECT genre, COUNT(genre) FROM books GROUP BY genre ORDER BY COUNT(genre) DESC")
	genre = res.fetchone()
	print("most common genre(s):", genre)


def import_db():

	# A10
	data = []
	with open("ReadingList.json", mode="rb") as fl:
		data = json.load(fl)
	

	# A11
	values = []
	for d in data:
		title = d.get("title")
		genre = d.get("genre")
		read = 1 if d.get("dates_read") else 0
		values.append((title, genre, read))

	cur.executemany("INSERT OR IGNORE INTO books (title, genre, read) VALUES (?, ?, ?)", values)
	con.commit()


	


# A1
def main():
	parser = argparse.ArgumentParser(description="SQLite Testprogramm")
	parser.add_argument("aktion", choices=["create", "query", "import"], 
					help="Bestimme, was gemacht werden soll: create | query | import")

	args = parser.parse_args()

	if args.aktion == "create":
		create_db()

	elif args.aktion == "query":
		query_db()

	elif args.aktion == "import":
		import_db()

	# A12
	con.close()


if __name__ == "__main__":
	main()
