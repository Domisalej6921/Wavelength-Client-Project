from data.DataHelper import DataHelper

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
