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


