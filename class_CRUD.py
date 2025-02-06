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
