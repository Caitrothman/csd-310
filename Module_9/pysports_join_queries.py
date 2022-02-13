
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

mycursor = db.cursor()

mysql = "SELECT \
     player_id, first_name, last_name, team_name \
     FROM player \
     INNER JOIN team ON player.team_id = team.team_id"

mycursor.execute(mysql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


