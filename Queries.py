import pandas as pd

# SQL queries
sql_queries = [
    "SELECT * FROM zomato_orders.Customer",
    "SELECT * FROM zomato_orders.Customer WHERE average_rating > 3",
    "SELECT * FROM zomato_orders.Restaurant WHERE is_active = TRUE",
    "SELECT o.order_id, o.order_date, o.status, o.total_amount, o.payment_mode, c.name AS customer_name "
    "FROM Orders o JOIN customer c ON o.customer_id = c.customer_id",
    "SELECT order_id, order_date, status, total_amount FROM orders WHERE customer_id = 290",
    "SELECT order_id, feedback_rating, total_amount, status FROM orders WHERE feedback_rating > 2",
    "SELECT order_id, feedback_rating, total_amount, status FROM orders WHERE feedback_rating < 2",
    "SELECT customer_id, name, total_orders FROM customer WHERE is_premium = TRUE AND total_orders > 10",
    "SELECT r.restaurant_id, r.name, AVG(d.delivery_time) AS avg_delivery_time FROM Restaurant r "
    "JOIN Orders o ON r.restaurant_id = o.restaurant_id JOIN Deliveries d ON o.order_id = d.order_id "
    "GROUP BY r.restaurant_id",
    "SELECT delivery_id, delivery_status, delivery_time, distance FROM Deliveries WHERE delivery_status = 'Delivered'",
    "SELECT order_id, total_amount, discount_applied FROM Orders WHERE discount_applied > 25",
    "SELECT delivery_id, delivery_status, distance, delivery_fee FROM Deliveries d WHERE order_id = 726",
    "SELECT order_id, payment_mode, total_amount, status FROM Orders",
    "SELECT vehicle_type, AVG(delivery_time) AS avg_delivery_time, AVG(delivery_fee) AS avg_delivery_fee "
    "FROM Deliveries GROUP BY vehicle_type",
    "SELECT order_id, order_date, total_amount FROM Orders WHERE order_date = '2022-06-05'",
    "SELECT customer_id, name, email FROM Customer WHERE is_premium = TRUE",
    "SELECT COUNT(order_id) AS total_orders FROM Orders WHERE restaurant_id = 550",
    "SELECT customer_id, name, total_orders FROM Customer WHERE total_orders > 5",
    "SELECT delivery_status FROM Deliveries WHERE order_id = 768",
    "SELECT SUM(discount_applied) AS total_discount FROM Orders WHERE discount_applied > 0"
]

# Query Titles
query_title = [
    "Fetching all customer information",
    "Customers with avg_rating above 3",
    "Information of active restaurants",
    "Customer Order details",
    "Specific customers order details",
    "Feedback rating above 2",
    "Feedback rating below 2",
    "Customers Who Are Premium and Have More Than 10 Orders",
    "Restaurant's average delivery time",
    "Deliveries by delivery status",
    "Orders with discounts applied above 25",
    "Delivery details for a specific order",
    "Orders with their payment mode",
    "Average delivery time and fee for each delivery vehicle type",
    "Orders placed on a specific date",
    "Premium customers details",
    "Specific restaurant ID detail",
    "Customer orders above 5",
    "Delivery status of an order",
    "Total discount applied for all orders"
]

# Executing query
def execute_query(query, connection):
    try:
        return pd.read_sql(query, connection)
    except Exception as e:
        print(f"Error executing query: {e}")
        return None
