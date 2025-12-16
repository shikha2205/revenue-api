import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="192.168.39.5",
        user="shikha",
        password="FDV76$sc2ns",
        database="billing_portal",
        port=3306
    )
