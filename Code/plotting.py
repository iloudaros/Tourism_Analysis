from matplotlib import pyplot as plt
import mysql.connector

mydb= mysql.connector.connect(	
	host="localhost",
	user="Το username μου",
	passwd="Το Password μου",
	database="Tourism"
)
mycursor = mydb.cursor()


xEL=[]
yEL=[]
xES=[]
yES=[]



########## Σχεδιάζοντας το πρώτο ερώτημα 

# Ελλάδα
mycursor.execute("SELECT number, year FROM Nights_spent WHERE country='EL' AND residency='TOTAL' " )

Data = mycursor.fetchall()


for i in Data:
	yEL.insert(len(yEL), i[0])
	xEL.insert(len(xEL), i[1])
	
	
# Ισπανία
mycursor.execute("SELECT number, year FROM Nights_spent WHERE country='ES' AND residency='TOTAL' " )

Data = mycursor.fetchall()
		
for i in Data:
	yES.insert(len(yES), i[0])
	xES.insert(len(xES), i[1])


# Δημιουργία Γραφημάτων 
plt.plot(xEL,yEL)
plt.plot(xES,yES)
plt.title("Nights spent at tourist accommodation establishments. (Greece and Spain)")

plt.show()















################ Ξαναρχικοποιούμε τις λίστες μας
xEL=[]
yEL=[]
xES=[]
yES=[]




########## Σχεδιάζοντας το δεύτερο ερώτημα 

# Ελλάδα
mycursor.execute("SELECT number, year FROM Nights_spent WHERE country='EL' AND residency='FOR' " )

Data = mycursor.fetchall()


for i in Data:
	yEL.insert(len(yEL), i[0])
	xEL.insert(len(xEL), i[1])
	
	
# Ισπανία
mycursor.execute("SELECT number, year FROM Nights_spent WHERE country='ES' AND residency='FOR' " )

Data = mycursor.fetchall()

for i in Data:
	yES.insert(len(yES), i[0])
	xES.insert(len(xES), i[1])
	
	
# Δημιουργία Γραφημάτων 
plt.plot(xEL,yEL)
plt.plot(xES,yES)
plt.title("Nights spent by non-residents at tourist accommodation establishments. (Greece and Spain)")

plt.show()

















################ Ξαναρχικοποιούμε τις λίστες μας
xEL=[]
yEL=[]
xES=[]
yES=[]




########## Σχεδιάζοντας το τρίτο ερώτημα 

# Ελλάδα
mycursor.execute("SELECT number, year FROM Arrivals WHERE country='EL' AND residency='TOTAL' " )

Data = mycursor.fetchall()


for i in Data:
	yEL.insert(len(yEL), i[0])
	xEL.insert(len(xEL), i[1])
	
	
# Ισπανία
mycursor.execute("SELECT number, year FROM Arrivals WHERE country='ES' AND residency='TOTAL' " )

Data = mycursor.fetchall()

for i in Data:
	yES.insert(len(yES), i[0])
	xES.insert(len(xES), i[1])
	
	
# Δημιουργία Γραφημάτων 
plt.plot(xEL,yEL)
plt.plot(xES,yES)
plt.title("Arrivals at tourist accommodation establishments. (Greece and Spain)")

plt.show()














################ Ξαναρχικοποιούμε τις λίστες μας
xEL=[]
yEL=[]
xES=[]
yES=[]




########## Σχεδιάζοντας το τέταρτο ερώτημα 

# Ελλάδα
mycursor.execute("SELECT number, year FROM Arrivals WHERE country='EL' AND residency='FOR' " )

Data = mycursor.fetchall()


for i in Data:
	yEL.insert(len(yEL), i[0])
	xEL.insert(len(xEL), i[1])
	
	
# Ισπανία
mycursor.execute("SELECT number, year FROM Arrivals WHERE country='ES' AND residency='FOR' " )

Data = mycursor.fetchall()

for i in Data:
	yES.insert(len(yES), i[0])
	xES.insert(len(xES), i[1])
	
	
# Δημιουργία Γραφημάτων 
plt.plot(xEL,yEL)
plt.plot(xES,yES)
plt.title("Arrivals by non-residents at tourist accommodation establishments. (Greece and Spain)")

plt.show()

