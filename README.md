# Zomata - Food Delivery Data Insights Using Python and SQL

## Project Overview
Zomata is a food delivery analytics project that leverages Python, SQL, and Streamlit to build an interactive data entry and insights tool for food delivery operations. The project aims to help improve operational efficiency and customer satisfaction by analyzing food delivery data, enabling data entry, and extracting valuable insights through an interactive tool.

## Key Technologies:

SQL
Python
Streamlit
Data Engineering
Database Management

## Problem Statement
Imagine you are a data scientist at Zomato working on food delivery data. The goal is to analyze delivery data, enhance operational efficiency, and improve customer satisfaction. To do so, we need to build an interactive Streamlit application that:

Allows seamless data entry for managing orders, customers, restaurants, and deliveries.
Supports robust database operations like adding columns or creating new tables dynamically while maintaining compatibility with existing code.

## Business Use Cases
### 1. Order Management
Identify peak ordering times and locations.
Track delayed and canceled deliveries.
### 2. Customer Analytics
Analyze customer preferences and order patterns.
Identify top customers based on order frequency and value.
### 3. Delivery Optimization
Analyze delivery times and delays to improve logistics.
Track delivery personnel performance.
### 4. Restaurant Insights
Evaluate the most popular restaurants and cuisines.
Monitor order values and frequency by restaurant.

## Approach
### 1. Dataset Creation
Tool Used: Python (Faker library) to generate synthetic datasets for customers, orders, restaurants, and deliveries.
Populate the SQL database with these datasets for testing and analysis.
### 2. Database Design
Create normalized SQL tables for Customers, Orders, Restaurants, and Deliveries.
Ensure the database schema allows dynamic changes (e.g., adding columns or creating new tables).
### 3. Data Entry Tool (Streamlit App)
Develop a Streamlit app that allows:
Adding, updating, and deleting records in the SQL database.
Dynamically creating new tables or modifying existing ones.
### 4. Data Insights
Use SQL queries and Python to extract insights like peak times, delayed deliveries, and customer trends.
Visualize the insights in the Streamlit app.
### 5. OOP Implementation
Use Object-Oriented Programming (OOP) principles to encapsulate database operations in Python classes.
Implement reusable methods for CRUD (Create, Read, Update, Delete) operations.

## Project Results
A fully functional SQL database to manage food delivery data.
An interactive Streamlit app for data entry and analysis.
Dynamic compatibility with database schema changes.
Insights into order trends, delivery performance, and customer behavior.


