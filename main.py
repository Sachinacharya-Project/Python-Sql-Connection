from database import connection

verification, dbhand = connection(database='apis')

if verification:
    print("Connection Has been Made Successfully")
    mycursor = dbhand.cursor()
    mycursor.execute("SELECT * FROM userlist")
    print(mycursor.fetchall())
    sql = "INSERT INTO userlist(userid) VALUES (%s)"
    val = ('1222121',)
    mycursor.execute(sql, val)
    print(mycursor.fetchall())
    mycursor.execute("show table userlist")
    print(mycursor.fetchall())
else:
    print("Connection is Dead as HELL")