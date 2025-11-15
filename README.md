
# 0Query | You're new database buddy

While we know the conventional method for Managing Database, Where the concepts such as query language were used.

With 0Query, I intend to create easier usage for anyone with limited developing Experience, where by improvising User-interface it would manage complex dataset through easy method. reducing time and efforts half it's Duration with the earlier method.


## Get Started

Clone the project

```bash
  git clone https://link-to-project
```

Navigate to the project directory

```bash
  cd zeroQuery
```

Install dependencies

```bash
  pip install psycopg2
```

Run the main file

```bash
  python zeroQuery.py
```


## Usage | Examples

```python
from zeroQuery import Db
```

## PostgreSQL connection details:
```python
server =  {
    'hostname' : 'localhost',
    'username' : 'postgres',
    'pwd' : '******', 
    'port_id' : 5432,
    'databse' : 'user'

}
```

### Initialize the Database


```
database = Db("postgresql",server)
```

### Create a Database


```
database.createDatabase("password")
```

### Switching Databases


```
newdatabase = Db("postgresql",server,"password")
```

### Creating a Table


```
attributes = {
    "First_Name" : "VARCHAR(255)",
    "Last_Name" :  "VARCHAR(255)",
    "Age": "INT",
    "passcode" : "VARCHAR(30)"

}
newdatabase.createTable("userPasscodes",attributes)
```


### Inserting Data


```
data = {
    "First_Name":'ibrahim', 
    "Last_Name" :'Ba Ata',
    "Age": 22, 
    "passcode":"AbXyzC78987@#" 
}
newdatabase.insertData('userPasscodes', data)
```

### Executing Queries


```
condition_data = newdatabase.sqlCommand("select * from userpasscodes where first_name = 'ibrahim';")
```

### Closing the Connection 


```
newdatabase.closeConnection()
```



## Upcoming Updates

Exciting new features and improvements are coming soon! Stay tuned.

### zeroQuery makes database management simple, intuitive, and accessible even for beginners.
