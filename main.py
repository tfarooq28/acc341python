import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Connect to database
conn = psycopg2.connect(os.getenv("DATABASE_URL"))

# Create cursor
cursor = conn.cursor()

# Run query
cursor.execute("SELECT * FROM customer;")

# Fetch results
rows = cursor.fetchall()

# Print results
for row in rows:
    print(row)

# Close connection
cursor.close()
conn.close()