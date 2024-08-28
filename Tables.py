import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="02121993")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS Library")
mycursor.execute("USE Library")

mycursor.execute("SHOW TABLES LIKE 'BookRecord' ")
result=mycursor.fetchone()
if result : 
    pass
else : #if Table doesn't exists then it will be created
    mycursor.execute("""CREATE TABLE BookRecord(BookID varchar(10) PRIMARY KEY , BookName varchar(35) , Author varchar(30) , Publisher varchar(30)) """)


mycursor.execute("SHOW TABLES LIKE 'UserRecord' ")
result=mycursor.fetchone()
if result : 
    pass
else : #if Table doesn't exists then it will be created
    mycursor.execute("""CREATE TABLE UserRecord(UserID varchar(10) PRIMARY KEY, UserName varchar(20),
                            Password varchar(20), BookID varchar(10),FOREIGN KEY (BookID) REFERENCES BookRecord(BookID))""")
    data1=("1","Sher","123",None)
    data2=("2","Mark","123",None)
    data3=("3","Joseph","123",None)
    query1="INSERT INTO UserRecord VALUES(%s, %s, %s, %s)"
    mycursor.execute(query1,data1)
    mycursor.execute(query1,data2)
    mycursor.execute(query1,data3)
    mydb.commit()
    
mycursor.execute("SHOW TABLES LIKE 'AdminRecord' ")
result=mycursor.fetchone()
if result : 
    pass
else: #if Table doesn't exists then it will be created
    mycursor.execute("""CREATE TABLE AdminRecord(AdminID varchar(10) PRIMARY KEY, Password varchar(20))""")
    data4=("Sher","123")
    data5=("Vicky","123")
    data6=("Mark","123")
    query2="INSERT INTO AdminRecord VALUES(%s, %s)"
    mycursor.execute(query2,data4)
    mycursor.execute(query2,data5)
    mycursor.execute(query2,data6)
    mydb.commit()
    
    
mycursor.execute("SHOW TABLES LIKE 'Feedback' ")
result=mycursor.fetchone()
if result : 
    pass
else : #if Table doesn't exists then it will be created
    mycursor.execute("""CREATE TABLE Feedback(Feedback varchar(100) PRIMARY KEY, Rating varchar(10))""")


    
