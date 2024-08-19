import psycopg2

foramt =  {
    'hostname' : 'locolhost',
    'username' : 'postgres',
    'pwd' : '',
    'port_id' : 5432,
    'databse' : ''
}

class Db:
    def __init__(self,dataBase:str,requiredData:dict=foramt,dbname:str='postgres'):
        """
    Create a new database connection.
    
    dataBase -- first parameter takes name database like postgresql/mysql,mongodb...
    
    The connection parameters can be specified as a string:

    Or as a mix of both. The basic connection parameters are:

    - *hostname*: database host address (defaults to UNIX socket if not provided)
    - *username*: user name used to authenticate
    - *pwd*: password used to authenticate
    - *port_id*: connection port number (defaults to 5432 if not provided)
    - *databse*: the database name (only as keyword argument)

        """
        if dataBase.lower() == "postgresql":
            if type(requiredData) == dict:
                self.requiredData = requiredData
                self.__conn = None
                try:
                    self.__conn = psycopg2.connect(
                        host = self.requiredData['hostname'],
                        dbname = dbname,
                        user = self.requiredData['username'],
                        password = self.requiredData['pwd'],
                        port = self.requiredData['port_id']
                    )
                    self.__cur= self.__conn.cursor()
                    # remove this just to test the operation
                    print("$ ** proper connection established ")
                except Exception as error:
                    print(error)
            else:
                raise TypeError(f"$ invalid type, need to use list(): {requiredData}")
        else:
            print("$ thanks for waiting, work is still on..")

        return None

    def __str__(self):
        """
        returns databse details ...
        """
        for i in self.requiredData.items():
            print(i)
        return "\n$ *** Db details ***"
    
    def createDatabase(self,database:str):
        """
        creates new database
        *parameters*
        1. new database name -> str()


        """
        self.__conn.autocommit = True
        try:
            __createdatabase = f'''CREATE database {database} '''
            grantPrivilages = f"GRANT ALL PRIVILEGES ON DATABASE {database} TO {self.requiredData['username']}"
            self.__cur.execute(__createdatabase)
            self.__cur.execute(grantPrivilages)
            print(f"$ {database} Successfully created")
            return ""
        except psycopg2.errors.DuplicateDatabase:
            print(f"$ database already created {database}")


    def createTable(self,tableNAME:str = None,attributes:dict = None):
        """
        creates new table
        *parameters*
        1.tablename  -> str()
        2.attributes -> dict()

        ** need to give proper tablename and its attribute ** 
        demo // CreateDataBase(tablename, {"Column name":"Column Type" })
        ex-   CreateDataBase("Books",{"sno": "int","book_name":"VARCHAR(50),..." })


        """

        if (tableNAME or attributes) == None:
            print( """ ** need to give proper tablename and its attribute ** 
 demo // CreateDataBase(tablename, {"Column name":"Column Type" })
   ex-   CreateDataBase("Books",{"sno": "int","book_name":"VARCHAR(50),..." })""")
            return "need to give proper tablename and its attributes"
        self.__attributes = attributes         
        templineJoiner = ',\n'
        try:
            CreateScript = f'''CREATE TABLE IF NOT EXISTS  {tableNAME}(
                {templineJoiner.join(f"{key} {value} " for key,value in self.__attributes.items())}
            )'''
            self.__cur.execute(CreateScript)
            self.__conn.commit()
            
            print(f"$ Attributes created for the table {tableNAME} ")
        except Exception as error:
            print("$ ",error,"not found")

    def tableData(self,tableNAMe:str,condition = False, conditionStatement=None):
        """
        returns table data.
        """
        if condition == False:
            self.__cur.execute(f'''SELECT * from {tableNAMe}''')
            result = self.__cur.fetchall()
        elif condition == True:
            self.__cur.execute(f'''SELECT * from {tableNAMe} {conditionStatement}''')
            result = self.__cur.fetchall()

        # self.__conn.commit()
        return result   

    def updateTableData(self):
        pass
