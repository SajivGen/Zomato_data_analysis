import mysql.connector

class my_database:
    def __init__(self,host,user,password,database):
        self.connection = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
        )   
        self.cursor = self.connection.cursor()
        
    #Fetching Tables    
        
    def fetch_tables(self):
        self.cursor.execute("SHOW TABLES")
        return [table[0] for table in self.cursor.fetchall()]
    
    #Fetching Table Columns
    
    def fetch_columns(self,table_name):
        self.cursor.execute(f"Describe{table_name}")
        return [row[0] for row in self.cursor.fetchall()]
    
    #Query Execution
    
    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()        
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            cursor.close()
            
        except Exception as e:
            raise e
        
    def fetch_data(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
                print(f"Error fetching data: {e}")
                return None