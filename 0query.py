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

        return None