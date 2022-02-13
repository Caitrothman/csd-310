import mysql.connector

from mysql.connector import errorcode
db = mysql.connector.connect
cursor = db.cursor()

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

print('-- DISPLAYING PlAYER RECORDS --')

cursor = db.cursor()

mysql = "INSERT INTO player\
     player_id, first_name, last_name, team_name \
     VALUES\
     '21', 'Smeagol', 'Shire Folk', 1"

cursor.execute(mysql)

myresult = cursor.fetchall()

for x in myresult:
    print(x)

print('-- DISPLAYING PlAYER RECORDS --')

cursor = db.cursor()

mysql = "SELECT \
     player_id, first_name, last_name, team_name \
     FROM player \
     INNER JOIN team ON player.team_id = team.team_id"

cursor.execute(mysql)

myresult = cursor.fetchall()

for x in myresult:
    print(x)

print('-- DISPLAYING PlAYER RECORDS --')

cursor = db.cursor()

mysql = "UPDATE player \
     SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer'\
     WHERE \
     first_name = 'Smeagol"

cursor.execute(mysql)

myresult = cursor.fetchall()

for x in myresult:
    print(x)

print('-- DISPLAYING PlAYER RECORDS --')

cursor = db.cursor()

mysql = "DELETE FROM player \
     WHERE \
     first_name = 'Gollum'"

cursor.execute(mysql)

myresult = cursor.fetchall()

for x in myresult:
    print(x)

print('-- DISPLAYING PlAYER RECORDS --')

mycursor = db.cursor()

mysql = "SELECT \
     player_id, first_name, last_name, team_name \
     FROM player \
     INNER JOIN team ON player.team_id = team.team_id"

mycursor.execute(mysql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
