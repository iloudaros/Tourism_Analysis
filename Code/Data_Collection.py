import mysql.connector
import eurostat

data1 = eurostat.get_data('tour_occ_ninat', flags=False)
data2 = eurostat.get_data('tour_occ_arnat', flags=False)

mydb= mysql.connector.connect(	
	host="localhost",
	user="Το username μου",
	passwd="Το password μου",
	database="Tourism",
)
mycursor = mydb.cursor()

mycursor.execute("DROP TABLE IF EXISTS Nights_spent " )
mycursor.execute("DROP TABLE IF EXISTS Arrivals " )








#Εισάγουμε τα απαραίτητα δεδομένα που σχετίζονται με τις διανυκτερεύσεις


mycursor.execute("CREATE TABLE Nights_spent ( country varchar(5), residency varchar(10), number bigint, year int)" ) #Δημιουργούμε τον πίνακα Nights_spent

for i in data1:
	
	if i[1] =='NR' and i[2]=="I551-I553" and (i[3]=="EL" or i[3]=="ES"): #Ελέγχουμε αν η εγγραφή μας ενδιαφέρει (Αν δηλαδή το unit of measure == number, αν περιέχονται όλα τα τουριστικά καταλύματα, αν η εγγραφή έγινε στην Ελλάδα ή στην Ισπανία)
		
		for j in range(4,34): #Δημιουργούμε ξεχωριστές εγγραφές στην βάση για κάθε χρονιά που υπάρχει στην πλειάδα ώστε να είναι τα δεδομένα μας πιο ευανάγνωστα
			year = str(2023 - j) #2023-4=2019 και 2023-33=1990, πιάνουμε δηλαδή όλο το range από ημερομηνίες στην πλειάδα. Επίσης μετατρέπουμε το αποτέλεσμα σε string για να το πάρει κατευθείαν το cursor
			number = str(i[j]) #Mετατρέπουμε το πλήθος σε string για να το πάρει κατευθείαν το cursor
			if number=='None':number=str(0)
			print("INSERT INTO Nights_spent VALUES (" + "\"" +i[3] + "\", \"" + i[0] + "\"," + number + "," + year +")" ) #Testing
			mycursor.execute("INSERT INTO Nights_spent VALUES (" + "\"" +i[3] + "\", \"" + i[0] + "\"," + number + "," + year + ")" )
			mydb.commit()

		



#Εισάγουμε τα απαραίτητα δεδομένα που έχουν να κάνουν με τις αφίξεις

mycursor.execute("CREATE TABLE Arrivals ( country varchar(5), residency varchar(10), number bigint, year int)" ) #Δημιουργούμε τον πίνακα Arrivals

for i in data2:
	
	if i[1] =='NR' and i[2]=="I551-I553" and (i[3]=="EL" or i[3]=="ES"): #Ελέγχουμε αν η εγγραφή μας ενδιαφέρει (Αν δηλαδή το unit of measure == number, αν περιέχονται όλα τα τουριστικά καταλήματα, αν η εγγραφή έγινε στην Ελλάδα ή στην Ισπανία)
		
		for j in range(4,34): #Δημιουργούμε ξεχωριστές εγγραφές στην βάση για κάθε χρονιά που υπάρχει στην πλειάδα ώστε να είναι τα δεδομένα μας πιο ευανάγνωστα
			year = str(2023 - j) #2023-4=2019 και 2023-33=1990, πιάνουμε δηλαδή όλο το range από ημερομηνίες στην πλειάδα. Επίσης μετατρέπουμε το αποτέλεσμα σε string για να το πάρει κατευθείαν το cursor
			number = str(i[j]) #Mετατρέπουμε το πλήθος σε string για να το πάρει κατευθείαν το cursor
			if number=='None':number=str(0)
			print("INSERT INTO Nights_spent VALUES (" + "\"" +i[3] + "\", \"" + i[0] + "\"," + number + "," + year +")" ) #Testing
			mycursor.execute("INSERT INTO Nights_spent VALUES (" + "\"" +i[3] + "\", \"" + i[0] + "\"," + number + "," + year + ")" )
			mydb.commit()

