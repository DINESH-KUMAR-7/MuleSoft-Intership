import sqlite3

#Try-catch : to avoid program crash
try:
	#making connection with datBase
	connection = sqlite3.connect('datBase.db')

	#cursor to make queries,
	cur = connection.cursor()
	cur.execute("SELECT * FROM movies")
	cur.execute("SELECT * FROM movies WHERE actor = 'Keanu Reeves'")

	#func - fetch all the data for us
	#by this we can see my fav movies ^_^
	print(cur.fetchall())
	print("Succesfully Connected")

except Exception as e:
	print("ERROR:",str(e))

#closing our connection
connection.close()