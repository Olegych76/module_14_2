import sqlite3 as sql

connection = sql.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('DELETE FROM users WHERE id = ?', (6,))

cursor.execute('SELECT COUNT(*) FROM users')
total_users = cursor.fetchone()[0]

cursor.execute('SELECT SUM(balance) FROM users')
all_balances = cursor.fetchone()[0]

print(all_balances / total_users)

connection.commit()
connection.close()
