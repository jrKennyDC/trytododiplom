import psycopg2

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
        cursor.execute("SELECT * FROM player")
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


#def update_characteristics_from_db():
 #   conn = connect_to_db()
  #  if conn:
   #     cursor = conn.cursor()
    #    cursor.execute("SELECT * FROM player")
     #   player_characteristics = cursor.fetchall()
#
 #       if player_characteristics:
         #  for player in player_characteristics:
               # Добавьте вашу логику замены характеристик здесь
                # Например, можно изменить какое-то поле характеристики и обновить его в базе данных
                # Например, увеличить значение здоровья или изменить профессию
    #            new_health = player[4]
     #           conn.commit()

      #      print("Characteristics updated successfully")
       # else:
        #    print("No player characteristics found in the database")

        #conn.close()
        def get_characteristics_for_n_players(n):
            conn = connect_to_db()
            if conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM player LIMIT %s", (n,))  # Ограничиваем выборку n числом игроков
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
# Вызов метода для получения и вывода характеристик в консоль

get_characteristics_from_db()
#update_characteristics_from_db()
