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
    
    ```bash    
  def All_products(self):
        object = Database_OOP()  # object of Database_OOP class
        # cursor runs all queries
        cursor = object.establishing_connection()  # cursor required to run queries in databse
        query_result = "SELECT * FROM products"
        rows = cursor.execute(query_result)
        for row in rows:
            print(row)
  
  def choice(self):
        user_input = int(input("""
             ==========================================================================================
             |Please enter the number for the operation you want to execute::                         |
             |                                                                                        |
             |\n 1. All products \n 2. All customers \n 3. Average unit price \n 4. Fetch Many\n ))   |
             ==========================================================================================
             """
        if user_input == 1: 
            self.All_products()
        elif user_input == 2:
            self.all_customers
        elif user_input == 3:
            self.average_product_price()
        elif user_input == 4:
            self.execute_sql()
        else:
            pass
  
  ```
- #### ```Main```:
    Use of abstraction. The user can't see any of the functionalities behind the code. 




