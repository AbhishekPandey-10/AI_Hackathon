import MySQLdb
try:
    print("Connecting to MySQL server...")
    db = MySQLdb.connect(host="localhost", user="root", passwd="Root@911820#", port=3306)
    cursor = db.cursor()
    print("Creating database 'nexus_db'...")
    cursor.execute("CREATE DATABASE IF NOT EXISTS nexus_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
    print("Database created successfully.")
    db.close()
except Exception as e:
    print(f"Failed to create database: {e}")
