from matplotlib import pyplot as plt
import mysql.connector

mydb= mysql.connector.connect(	
	host="localhost",
	user="Το username μου",
	passwd="Το password μου",
	database="Tourism",
)
mycursor = mydb.cursor()




# Σχεδιάζοντας το πρώτο ερώτημα 

mycursor.execute("SELECT number, year FROM Nights_spent WHERE " )


