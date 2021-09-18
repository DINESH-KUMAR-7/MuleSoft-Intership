import sqlite3

try:
	#making connection with datBase
	connection = sqlite3.connect('datBase.db')
	cur = connection.cursor()

	#inserting my fav-movies list
	cur.execute("INSERT INTO movies VALUES ('Avengers:Endgame','Chris Evans','Scarlett Johansson',2019,'Anthony Russo')")
	cur.execute("INSERT INTO movies VALUES ('Your Name','Taki Tachibana','Mitsuha Miyamizu',2016,'Makoto Shinkai')")
	cur.execute("INSERT INTO movies VALUES ('The Imitation Game','Benedict Cumberbatch','Keira Knightley',2014,'Morten Tyldum')")
	cur.execute("INSERT INTO movies VALUES ('The Matrix','Keanu Reeves','Carrie-Anne Moss',1999,'Lana Wachowski')")

	print("Data Inserted Successfully")

except Exception as e:
	print("ERROR:",str(e))

#making all changes permanent
connection.commit()

#closing our connection
connection.close()
