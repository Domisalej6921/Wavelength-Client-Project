import os
from data.DataHelper import DataHelper

# Check the databases directory exists and if not create it
if not os.path.exists("data/databases"):
    os.makedirs("data/databases")

# Check if the general.db file exists and if not create it
if not os.path.exists("data/databases/general.db"):
    file = open("data/databases/general.db", "w")
    file.close()

# Create DB instance
db = DataHelper()

# Read the sql table import file
file = open("import.sql", "r")
dbInfo = file.read()
file.close()

# Split the file into individual queries
queries = dbInfo.split(";")

# Execute each query
for query in queries:
    db.Execute(query)
