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
cursor.execute("SELECT c.company_name, SUM(i.total_amount) AS total_billed FROM invoice i JOIN customer c ON i.customer_id = c.customer_id GROUP BY c.company_name ORDER BY total_billed DESC;")

# Fetch results
rows = cursor.fetchall()

# Print results
for row in rows:
    print(row)

# Close connection
cursor.close()
conn.close()