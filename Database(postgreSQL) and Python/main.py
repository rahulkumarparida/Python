import psycopg2
import private as p

conn = psycopg2.connect(dbname=p.dbname, user=p.user , password=p.password,host=p.host,port=p.port)
print("Connection Established") 



def Table():
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE employee(Name text , ID int , age int);''')
    print("Table is created sucessfully")

    conn.commit()
    conn.close()
    
def Data():
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO employee(Name,ID,age) VALUES( 'Situ' , 12354 , 20);''')
    print("Data added successfully")



    conn.commit()
    conn.close()
    
def Extract():
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM employee;''')
    print("Data fetched successfully")
    print(cursor.fetchall())


    conn.commit()
    conn.close()

def GetFromUser():
    cursor = conn.cursor()
    
    name = input("Enter the name: ")
    id = int(input("Enter the ID: "))
    age = int(input("Enter the age: "))
    
    
    query ='''INSERT INTO employee(Name,ID,age) VALUES( %s,%s,%s);'''
    cursor.execute(query,(name,id,age))
    print("Data added successfully")


    conn.commit()
    conn.close()



