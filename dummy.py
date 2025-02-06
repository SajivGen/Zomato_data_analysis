import streamlit as st
import pandas as pd

class CRUDoperation:
    def __init__(self, database):
        self.db = database

    def create_table(self):
        table_name = st.text_input("Enter table name")
        column_definitions = st.text_area(
            "Enter column definition"
        )
        if st.button("Create_table"):
            if not table_name or column_definitions:
                st.error("Table name and column definition required!")
                return
            
            query = f"CREATE TABLE{table_name} ({column_definitions});"
            try:
                self.db.execute_query(query)
                st.success(f"Table {table_name} created successfully")
            except Exception as e:
                st.error(str(e))

    def read_table(self):
        table_name = st.text_input("Enter table name")
        if st.button("Read Table"):
            if not table_name:
                st.error("Table name required!")
                return
            query = f"SELECT * FROM {table_name};"
            try:
                result = self.db.execute_query(query)
                st.write(result)
            except Exception as e:
                st.error(str(e))

    def update_table(self):
        table_name = st.text_input("Enter table name")
        set_clause = st.text_area("Enter SET clause")
        condition = st.text_area("Enter WHERE clause")
        if st.button("Update Table"):
            if not table_name or not set_clause or not condition:
                st.error("Table name, SET clause, and WHERE clause required!")
                return
            query = f"UPDATE {table_name} SET {set_clause} WHERE {condition};"
            try:
                self.db.execute_query(query)
                st.success(f"Table {table_name} updated successfully")
            except Exception as e:
                st.error(str(e))

    def delete_table(self):
        table_name = st.text_input("Enter table name")
        condition = st.text_area("Enter WHERE clause")
        if st.button("Delete Table"):
            if not table_name or not condition:
                st.error("Table name and WHERE clause required!")
                return
            query = f"DELETE FROM {table_name} WHERE {condition};"
            try:
                self.db.execute_query(query)
                st.success(f"Entries from {table_name} deleted successfully")
            except Exception as e:
                st.error(str(e))

    def insert_table(self):
        table_name = st.text_input("Enter table name")
        columns = st.text_area("Enter column names (comma-separated)")
        values = st.text_area("Enter values (comma-separated)")
        if st.button("Insert into Table"):
            if not table_name or not columns or not values:
                st.error("Table name, columns, and values required!")
                return
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
            try:
                self.db.execute_query(query)
                st.success(f"Values inserted into {table_name} successfully")
            except Exception as e:
                st.error(str(e))

    def alter_table(self):
        table_name = st.text_input("Enter table name")
        alteration = st.text_area("Enter table alteration")
        if st.button("Alter Table"):
            if not table_name or not alteration:
                st.error("Table name and alteration required!")
                return
            query = f"ALTER TABLE {table_name} {alteration};"
            try:
                self.db.execute_query(query)
                st.success(f"Table {table_name} altered successfully")
            except Exception as e:
                st.error(str(e))


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
        
import mysql.connector
import streamlit as st
import pandas as pd

connection =mysql.connector(
    host="localhost",
    user="root",
    password="root",
    database="zomato_orders"
)

my_cursor = connection.cursor()

sql_queries =[
    "SELECT * FROM zomato_orders.Customer",
    "SELECT * FROM zomato_orders.Customer WHERE average_rating>3",
    "SELECT * FROM zomato_orders.Restaurant WHERE is_active = TRUE",
    "SELECT o.order_id, o.order_date, o.status, o.total_amount, o.payment_mode, c.name AS customer_name FROM Orders o JOIN customer c ON o.customer_id = c.customer_id",
    "SELECT order_id, order_date, status, total_amount FROM orders WHERE customer_id = 290",
    "SELECT order_id, feedback_rating, total_amount, status FROM orders WHERE feedback_rating>2",
    "SELECT order_id, feedback_rating, total_amount, status FROM orders WHERE feedback_rating<2",
    "SELECT customer_id, name, total_orders FROM customer WHERE is_premium = TRUE AND total_orders > 10",
    "SELECT r.restaurant_id, r.name, AVG(d.delivery_time) AS avg_delivery_time FROM Restaurant r JOIN Orders o ON r.restaurant_id = o.restaurant_id JOIN Deliveries d ON o.order_id = d.order_id GROUP BY r.restaurant_id",
    "SELECT delivery_id, delivery_status, delivery_time, distance FROM Deliveries WHERE delivery_status = Delivered",
    "SELECT order_id, total_amount, discount_applied FROM Orders WHERE discount_applied > 25",
    "SELECT delivery_id, delivery_status, distance, delivery_fee FROM Deliveries d WHERE order_id = 726",
    "SELECT order_id, payment_mode, total_amount, status FROM Orders",
    "SELECT vehicle_type, AVG(delivery_time) AS avg_delivery_time, AVG(delivery_fee) AS avg_delivery_fee FROM Deliveries GROUP BY vehicle_type",
    "SELECT order_id, order_date, total_amount FROM Orders WHERE order_date = 2022-06-05-",
    "SELECT customer_id, name, email FROM Customer WHERE is_premium = TRUE",
    "SELECT COUNT(order_id) AS total_orders FROM Order WHERE restaurant_id = 550",
    "SELECT customer_id, name, total_orders FROM Customer WHERE total_orders > 5",
    "SELECT delivery_status FROM Deliveries WHERE order_id =768",
    "SELECT SUM(discount_applied) AS total_discount FROM Orders WHERE discount_applied > 0"
]
query_title =["Fectching all customers information","Customers with avg_rating above 3","Information of active restuarants","Customer Order details","Specific customers order details",
              "Feedback rating above 2","Feedback rating below 2","Customers Who Are Premium and Have More Than 10 Orders","Restaurant's average delivery time","Deliveries by delivery status","Orders with discounts Applied above 25",
              "Delivery details for a specific Order","Orders with their payment mode","Average delivery time and fee for each delivery vehicle type","Orders placed on specific date",
              "Premium customers details","Specific restaurant id detail","Customer orders above 5","Delvery status of an order","Total discount applied for all orders"]
select_query = st.selectbox("Select a query", query_title)

if select_query== "Fectching all customers information":
    my_cursor.execute(sql_queries[0],connection)
    data = my_cursor.fetchall()
    df = pd.read_sql(sql_queries[0],connection)
    st.dataframe(df)
elif select_query== "Customers with avg_rating above 3":
    my_cursor.execute(sql_queries[1],connection)
    data = my_cursor.fetchall()
    df = pd.read_sql(sql_queries[1],connection)
    st.dataframe(df) 
elif select_query== "Information of active restuarants":
    my_cursor.execute(sql_queries[2],connection)
    data = my_cursor.fetchall()
    df = pd.read_sql(sql_queries[2],connection)
    st.dataframe(df)
elif select_query== "Customer Order details":
    my_cursor.execute(sql_queries[3],connection)
    data = my_cursor.fetchall()
    df = pd.read_sql(sql_queries[3],connection)
    st.dataframe(df)         
elif select_query== "Specific customers order details":
    my_cursor.execute(sql_queries[4],connection)
    data = my_cursor.fetchall()
    df = pd.read_sql(sql_queries[4],connection)
    st.dataframe(df)
elif select_query== "Feedback rating above 2":
    my_cursor.execute(sql_queries[5],connection)
    data = my_cursor.fetchall()
    df = pd.read_sql(sql_queries[5],connection)
    st.dataframe(df)
elif select_query== "Feedback rating below 2":
    my_cursor.execute(sql_queries[6],connection)
    data = my_cursor.fetchall()
    df = pd.read_sql(sql_queries[6],connection)
    st.dataframe(df)
elif select_query== "Customers Who Are Premium and Have More Than 10 Orders":
    my_cursor.execute(sql_queries[7],connection)
    data = my_cursor.fetchall()
    df = pd.read_sql(sql_queries[7],connection)
    st.dataframe(df)
elif select_query== "Restaurant's average delivery time":
    my_cursor.execute(sql_queries[8],connection)
    data = my_cursor.fetchall()
    df = pd.read_sql(sql_queries[8],connection)
    st.dataframe(df)               
elif select_query== "Deliveries by delivery status":
    my_cursor.execute(sql_queries[9],connection)
    data = my_cursor.fetchall()
    df = pd.read_sql(sql_queries[9],connection)
    st.dataframe(df)
elif select_query== "Orders with discounts Applied above 25":
    my_cursor.execute(sql_queries[10],connection)
    data = my_cursor.fetchall()
    df = pd.read_sql(sql_queries[10],connection)
    st.dataframe(df)
elif select_query== "Delivery details for a specific Order":
    my_cursor.execute(sql_queries[11],connection)
    data = my_cursor.fetchall()
    df = pd.read_sql(sql_queries[11],connection)
    st.dataframe(df)             
elif select_query== "Orders with their payment mode":
    my_cursor.execute(sql_queries[12],connection)
    data = my_cursor.fetchall()
    df = pd.read_sql(sql_queries[12],connection)
    st.dataframe(df)
elif select_query== "Average delivery time and fee for each delivery vehicle type":
    my_cursor.execute(sql_queries[13],connection)
    data = my_cursor.fetchall()
    df = pd.read_sql(sql_queries[13],connection)
    st.dataframe(df)        
elif select_query== "Orders placed on specific date":
    my_cursor.execute(sql_queries[14],connection)
    data = my_cursor.fetchall()
    df = pd.read_sql(sql_queries[14],connection)
    st.dataframe(df)    
elif select_query== "Premium customers details":
    my_cursor.execute(sql_queries[15],connection)
    data = my_cursor.fetchall()
    df = pd.read_sql(sql_queries[15],connection)
    st.dataframe(df)
elif select_query== "Specific restaurant id detail":
    my_cursor.execute(sql_queries[16],connection)
    data = my_cursor.fetchall()
    df = pd.read_sql(sql_queries[16],connection)
    st.dataframe(df)    
elif select_query== "Customer orders above 5":
    my_cursor.execute(sql_queries[17],connection)
    data = my_cursor.fetchall()
    df = pd.read_sql(sql_queries[17],connection)
    st.dataframe(df)    
elif select_query== "Delvery status of an order":
    my_cursor.execute(sql_queries[18],connection)
    data = my_cursor.fetchall()
    df = pd.read_sql(sql_queries[18],connection)
    st.dataframe(df)    
elif select_query== "Total discount applied for all orders":
    my_cursor.execute(sql_queries[19],connection)
    data = my_cursor.fetchall()
    df = pd.read_sql(sql_queries[19],connection)
    st.dataframe(df)       
else:
    print("Query not available")                             
        
from class_database import my_database
from class_CRUD import CRUDoperation

import streamlit as st
import pandas as pd

#Initializing database
new_db = my_database(
    host="localhost",
    user="root",
    password="root",
    database="zomato_orders"
)

#Initializing CRUD operation
crud_ops = CRUDoperation(new_db)

#Streamlit
st.sidebar.title("Zomato Data Analysis")
operation = st.sidebar.selectbox("Select Operation", ['Create', 'Read', 'Update', 'Delete', 'Insert','Alter'])

if operation == "Create":
    crud_ops.create_table()
elif operation == "Read":
    crud_ops.read_table()
elif operation == "Update":
    crud_ops.update_table()
elif operation == "Delete":
    crud_ops.delete_table()
elif operation == "Insert":
    crud_ops.insert_table()
elif operation == "Alter":
    crud_ops.alter_table()
else:
    st.warning("Select a valid operation")      



        