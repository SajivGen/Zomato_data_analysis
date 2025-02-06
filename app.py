import streamlit as st
import pandas as pd
from class_database import my_database
from class_CRUD import CRUDoperation
from Queries import sql_queries, query_title

# Initialize database
new_db = my_database(
    host="localhost",
    user="root",
    password="root",
    database="zomato_orders"
)

# Initialize CRUD operations
crud_ops = CRUDoperation(new_db)

# Streamlit interface
st.sidebar.title("Zomato Order Analysis")
operation = st.sidebar.radio("Choose an option", ["Tables", "CRUD", "Queries"])

#Display Tables
def display_tables():
    tables = new_db.fetch_tables()  # Get the list of tables from the database
    table_choice = st.selectbox("Select a table", tables)
    
    if table_choice:
        query = f"SELECT * FROM {table_choice};"
        data = new_db.fetch_data(query)
        if data:
            df = pd.DataFrame(data, columns=[col[0] for col in new_db.cursor.description])
            st.write(f"Content of {table_choice} table:")
            st.dataframe(df)
        else:
            st.error(f"No data available for {table_choice}")

# CRUD operations
def perform_crud():
    operation = st.selectbox("Select CRUD operation", ["Create", "Read", "Update", "Delete", "Insert", "Alter"])
    
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

# Function to display queries
def display_queries():
    query_choice = st.selectbox("Select a query", query_title)
    query_index = query_title.index(query_choice)
    query = sql_queries[query_index]
    
    if st.button("Run Query"):
        data = new_db.fetch_data(query)
        if data:
            df = pd.DataFrame(data, columns=[col[0] for col in new_db.cursor.description])
            st.dataframe(df)
        else:
            st.error("No data available for this query")

# Main App Logic
if operation == "Tables":
    st.header("Database Tables")
    display_tables()

elif operation == "CRUD":
    st.header("CRUD Operations")
    perform_crud()

elif operation == "Queries":
    st.header("SQL Queries")
    display_queries()
