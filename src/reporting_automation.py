import pyodbc
import pandas as pd

#Συνδεση με τον SQL Server
conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost;"
    "Database=ShippingDB;"
    "Trusted_Connection=yes;"
)

#Εκτελεση και αποθηκευση αποτελεσματων 
with open("sql/sql_server/most_traveled_ships_2024.sql",'r',encoding='utf-8') as file:
    query = file.read()
    df1 = pd.read_sql(query,conn)

with open("sql/sql_server/arrival_ports_stats.sql",'r',encoding='utf-8') as file:
    query = file.read()
    df2 = pd.read_sql(query,conn)

with open("sql/sql_server/voyage_summary.sql",'r',encoding='utf-8') as file:
    query = file.read()
    df3 = pd.read_sql(query,conn)

#Export των Dataframes σε Excel
with pd.ExcelWriter("reports/sql_server/shipping_report.xlsx", engine="openpyxl") as writer: 
    df1.to_excel(writer,sheet_name="Top Arrival Ports", index=False)
    df2.to_excel(writer, sheet_name="Voyage Durations", index=False)
    df3.to_excel(writer, sheet_name="Full Voyage List", index=False)






