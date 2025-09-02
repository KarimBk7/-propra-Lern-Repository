import argparse
import sqlite3
import pprint

dbName = "m_sqlite3.db"

def create_db():

	# A2
	con = sqlite3.connect(dbName)

	# A3 
	cur = con.cursor()
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


def query():
	# Verbinde mit Datenbank
	con = sqlite3.connect(dbName)
	cur = con.cursor()
	
	# A7
	res = cur.execute("SELECT COUNT(*) FROM books")
	count = res.fetchone()
	print("number of entries in 'books':", count[0])

	# A8
	res = cur.execute("SELECT TITLE FROM books WHERE genre = 'Fantasy'")
	fantasy = res.fetchone()
	pp = pprint.PrettyPrinter(indent=2, depth=2, sort_dicts=False)
	print("fantasy books:", end=" ")
	pp.pprint(fantasy)
	
	# A9
	res = cur.execute("SELECT genre, COUNT(genre) FROM books GROUP BY genre ORDER BY COUNT(genre) DESC")
	genre = res.fetchall()
	print("most common genre(s):", end=" ")
	pp.pprint(genre)

# A1
def main():
	parser = argparse.ArgumentParser(description="SQLite Testprogramm")
	parser.add_argument("aktion", choices=["create", "query", "import"], 
					help="Bestimme, was gemacht werden soll: create | query | import")

	args = parser.parse_args()

	if args.aktion == "create":
		create_db()

	elif args.aktion == "query":
		query()

	elif args.aktion == "import":
		print("Daten werden importiert...")


if __name__ == "__main__":
	main()
