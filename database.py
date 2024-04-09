import psycopg2

# Параметры подключения
dbname = "bunker"
user = "postgres"
password = "64701813092001m"
host = "localhost"
port = "5432"

# Подключение к базе данных
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cur = conn.cursor()

# Пример выполнения запроса
cur.execute("SELECT * FROM player")
rows = cur.fetchall()

for row in rows:
    print(row)
cur.execute("SELECT * FROM catastrophe")
rows=cur.fetchall()
for row in rows:
    print(row)
# Не забудь закрыть соединение после использования
cur.close()
conn.close()