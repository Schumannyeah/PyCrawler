import json
import pymssql
import os
import pyodbc

# Construct the relative path to the JSON file
# os.pardir refers to the parent directory, and os.path.join is used to create a cross-platform
# compatible path to the JSON file located one level up from the current script's directory
# json_file_path = os.path.join(os.pardir, 'cssc-company.json')
json_file_path = os.path.abspath(os.path.join(os.pardir, os.pardir, 'cssc-company.json'))

# Load data from the JSON file
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Database connection details
server = r"DESKTOP-224LS54\SQLEXPRESS"
user = "sa"
password = "s123456s"
database = "gorilla"

# Connect to the database
# conn = pymssql.connect(server, user, password, database)
# cursor = conn.cursor()

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+user+';PWD='+ password)
cursor = conn.cursor()

# SQL query to insert data with pymssql
# insert_query = "INSERT INTO DT_COMPANY (INDUSTRY, COMPANY, WEBSITE) VALUES (%s, %s, %s)"

# SQL query to insert data - using ? as placeholders with pyodbc
insert_query = "INSERT INTO DT_COMPANY (INDUSTRY, COMPANY, WEBSITE) VALUES (?, ?, ?)"

# Iterate over the data and insert into the database
for item in data:
    # company_name = item['company'][0]  # Assuming 'company' always contains a single element
    # website = item['website'][0]       # Similarly, assuming 'website' contains a single URL
    # cursor.execute(insert_query, ('SHIP_BUILDING',company_name, website))
    company_name = item.get('company', [''])[0]  # Provides a default empty list if 'company' is missing
    print(company_name)
    websites = item.get('website', [])  # Get the 'website' list, defaulting to an empty list if not present
    print(websites)

    # Proceed only if there is a valid website URL available
    if websites:  # This checks if the 'website' list is not empty
        website = websites[0]
        cursor.execute(insert_query, ('SHIP_BUILDING', company_name, website))
    else:
        print(f"Skipping record for '{company_name}' due to missing website.")


# Commit the transaction and close the connection
conn.commit()
cursor.close()
conn.close()

print("Data inserted successfully.")