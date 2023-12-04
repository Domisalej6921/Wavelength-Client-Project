import sqlite3
import json

conn = sqlite3.connect('general.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM Files')
data = cursor.fetchall()

jsonData = []
for row in data:
    rowDict = dict(zip([description[0] for description in cursor.description], row))
    jsonData.append(rowDict)

existingJSONData = []
try:
    with open('mainPage.json', 'r') as JSONFile:
        existingJSONData = json.load(JSONFile)
except FileNotFoundError:
    pass

combinedJSONData = existingJSONData + jsonData

with open('mainPage.json', 'w') as JSONFile:
    json.dump(combinedJSONData, JSONFile, indent=2)

conn.close()