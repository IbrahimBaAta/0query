from zeroQuery import Db
#  DBMS 

# PostgreSQL connection details:
server =  {
    'hostname' : 'localhost',
    'username' : 'postgres',
    'pwd' : '', 
    'port_id' : 5432,
    'databse' : 'user'

}

# sample data for createing the table
attri = {
    "First_Name" : "VARCHAR(255)",
    "Last_Name" :  "VARCHAR(255)",
    "Age": "INT",
    "passcode" : "VARCHAR(30)"

}

# sample Value for the table
columnval = {

    "First_Name":'Xyz', 
    "Last_Name" :'Abs',
    "Age": 23, 
    "passcode":"AbXyzC78987@#" 
}

# Db-class takes two parameters 1. which database like psql,mysql.... 
#                               2. database access credentials 

database = Db("postgresql",server)
print(database)

# creating a New database..  
database.createDatabase("passwords")

# changing database "user" to "password"...
newdatabase = Db("postgresql",server,"passwords")

# creating table in database "password"
newdatabase.createTable("userPasscodes",attri)

# inserting data.
newdatabase.insertData('userPasscodes', columnval)

# passing queries 
condition_data = newdatabase.sqlCommand("select * from userpasscodes where first_name = 'saqlain';")
# print(condition_data)

# lastly closing the connection
newdatabase.closeConnection()
