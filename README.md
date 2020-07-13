### README Database connection 

#### Files
* Database Connections - establish a connection and read data from the database in the python console
* Queries - Main functions are in this module 
* Main - In real time we see the output in the graphical user interface GUI

- ##### ```Database Connections```: 
    login details are stored on this module. Details including 
    server, database, username, password 
```   
database = ""
username = ""
password = ""
cnxn = ""
cursor = ""
```
- #### ```Queries```: 
    code is hard coded into retrieving: (1) All customers, (2) All products, (3) average product price and choice.
Choice is the user interface that chooses what options to choose.
    - All methods except choice follow a similar structure. A cursor variable is made is an instance of the parent class 
    and of establishing_connection(). This cursor is ran to run queries in the database. "SELECT * FROM products" 
- #### ```Main```:
    Use of abstraction. The user can't see any of the functionalities behind the code. 




