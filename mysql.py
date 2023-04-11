import mysql.connector


connection = mysql.connector.connect(user= 'root', database= 'database_name', password= '')


connection.close()
