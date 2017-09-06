import pyodbc
# import pandas as pd
from pandas.io import sql

conn = pyodbc.connect('Trusted_Connection=yes', driver = '{ODBC Driver 13 for SQL Server}',server = 'localhost\SQLEXPRESS', database = 'TestDB')
cursor = conn.cursor()
# cursor.execute("select * from person")
# results = cursor.fetchall()
results = sql.read_sql("select * from person", con=conn)
print results.head()
