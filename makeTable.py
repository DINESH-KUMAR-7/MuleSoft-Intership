import sqlite3

try:
	#making connection with datBase
	connection = sqlite3.connect('datBase.db')
	cur = connection.cursor()

	#executing Create table command..
	cur.execute("""CREATE TABLE movies(movie_name text,actor text,actress text,year_of_release int,director_name text)""")
	print("Table Created")

except Exception as e:
	print("ERROR:",str(e))

#making all changes permanent
connection.commit()

#closing our connection
connection.close()