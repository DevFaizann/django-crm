import mysql.connector

try:
    dataBase = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = ' '
    )

    cursorObject = dataBase.cursor()

    cursorObject.execute("CREATE DATABASE IF NOT EXISTS faizancrm")

    print('DATABASE "faizancrm" successfully created.')

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'cursorObject' in locals():
        cursorObject.close()
    
    if 'dataBase' in locals():
        dataBase.close()

print('ALL DONE')