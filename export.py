# import sqlite3

# # Connect to your SQLite3 database
# sqlite_conn = sqlite3.connect('db.sqlite3')
# cursor = sqlite_conn.cursor()

# # Export to SQL file
# with open('sqlite_dump.sql', 'w') as f:
#     for line in sqlite_conn.iterdump():
#         f.write('%s\n' % line)

# # Close the connection
# sqlite_conn.close()
import re

# Read the SQLite SQL dump file
with open('sqlite_dump.sql', 'r') as file:
    data = file.read()

# Replace double quotes with backticks for MySQL
data = re.sub(r'\"([^\"]+)\"', r'`\1`', data)

# Replace other SQLite-specific types and constraints if needed
data = data.replace('AUTOINCREMENT', 'AUTO_INCREMENT')
data = data.replace('INTEGER', 'INT')
data = data.replace('TEXT', 'VARCHAR(255)')
data = data.replace('BLOB', 'LONGBLOB')
data = data.replace('BEGIN TRANSACTION;', '')
data = data.replace('COMMIT;', '')
data = data.replace('PRAGMA foreign_keys=OFF;', '')

# Remove DEFERRABLE INITIALLY DEFERRED
data = re.sub(r'DEFERRABLE INITIALLY DEFERRED', '', data, flags=re.IGNORECASE)

# Write the modified data to a new file
with open('mysql_dump.sql', 'w') as file:
    file.write(data)

print("SQL dump file converted for MySQL compatibility.")

