import psycopg2
import random
# Подключение к базе данных
def connect_to_db():
    try:
        conn = psycopg2.connect(dbname='bunker', user='postgres', password='64701813092001m', host='localhost')
        return conn
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL:", e)
        return None
# Метод для получения характеристик из базы данных и вывода их в консоль
def get_characteristics_from_db():
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM player ORDER BY random() LIMIT 10")
        player_characteristics = cursor.fetchall()
        conn.close()

        if player_characteristics:
            for player in player_characteristics:
                print(f"Player ID: {player[0]}")
                print(f"Profession: {player[3]}")
                print(f"Biology: {player[1]}")
                print(f"Age: {player[2]}")
                print(f"Health: {player[4]}")
                print(f"Hobby: {player[5]}")
                print(f"Baggage: {player[6]}")
                print(f"Additional Facts: {player[9]}")
                print(f"Special Condition: {player[7]}")
                print(f"Description: {player[8]}")
                print()
        else:
            print("No player characteristics found in the database")



def get_catastrophe_from_db():
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM catastrophe ORDER BY random() LIMIT 1")
        catastrophe_characteristcs = cursor.fetchall()
        conn.close()
        if catastrophe_characteristcs:
            for catastriphe in catastrophe_characteristcs:
                print(f"Catastrophe ID: {catastriphe[4]}")
                print(f"Catastrophe: {catastriphe[0]}")
                print(f"description: {catastriphe[3]}")
                print(f"bunker: {catastriphe[1]}")
                print(f"THREAT: {catastriphe[2]}")
get_catastrophe_from_db()
def get_additional_bunkers_from_db():
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM catastrophe ORDER BY random() LIMIT 2")  # Выбор 2 случайных катастроф
        catastrophes = cursor.fetchall()
        conn.close()

        if catastrophes:
            print("Additional Catastrophes:")

            for catastrophe in catastrophes:
                print(f"BUNKER CARDS: {catastrophe[1]}")
        else:
            print("No additional bunkers card found in the database")
def get_additional_threat_from_db():
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM catastrophe ORDER BY random() LIMIT 1")  # Выбор 2 случайных катастроф
        catastrophes = cursor.fetchall()
        conn.close()

        if catastrophes:
            print("Additional threat:")

            for catastrophe in catastrophes:
                print(f"threat: {catastrophe[2]}")
        else:
            print("No additional threat card found in the database")
def get_additional_SC_from_db():
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM player ORDER BY random() LIMIT 8")  # Выбор 2 случайных катастроф
        player = cursor.fetchall()
        conn.close()

        if player:
            print("Additional SC:")

            for player in player:
                print(f"SC: {player[7]}")
                print(f"description: {player[8]}")
        else:
            print("No additional threat card found in the database")

# Вызываем метод для вывода дополнительных ID катастроф
get_characteristics_from_db()
get_additional_bunkers_from_db()
# Вызов метода для получения и вывода характеристик в консоль

get_catastrophe_from_db()
get_additional_threat_from_db()
get_additional_SC_from_db()

