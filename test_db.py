import MySQLdb
try:
    print("Attempting to connect with password...")
    db = MySQLdb.connect(host="localhost", user="root", passwd="Root@911820#", port=3306)
    print("Connection successful!")
    db.close()
except Exception as e:
    print(f"Connection failed: {e}")
