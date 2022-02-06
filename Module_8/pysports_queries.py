import mysql.connector
from mysql.connector import errorcode
db = mysql.connector.connect

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

cursor = db.cursor ()

cursor.execute("SELECT team_id, team_name, mascot FROM team" )

teams = cursor.fetchall()

for team in teams:
    print("Team Name: {}".format(team[1]))

cursor = db.cursor ()

cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player" )

players = cursor.fetchall()

for player in players:
    print("Player: {}".format(player[1]))

