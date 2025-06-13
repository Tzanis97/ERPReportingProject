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
with open("sql\sql_server\most_traveled_ships_2024.sql",'r') as file:
    query = file.read()
    df1 = pd.read_sql(query,conn)

with open("sql\sql_server\most_traveled_ships_2024.sql",'r') as file:
    query = file.read()
    df2 = pd.read_sql(query,conn)
    
with open("sql\sql_server\most_traveled_ships_2024.sql",'r') as file:
    query = file.read()
    df3 = pd.read_sql(query,conn)

with open("sql\sql_server\most_traveled_ships_2024.sql",'r') as file:
    query = file.read()
    df4 = pd.read_sql(query,conn)

#Export των Dataframes σε Excelq
with pd.ExcelWriter("shipping_report.xlsx", engine="openpyxl") as writer: 
    df1.to_excel(writer,sheet_name="Top Arrival Ports", index=False)
    df2.to_excel(writer, sheet_name="Voyage Durations", index=False)
    df3.to_excel(writer, sheet_name="Arrival Port Stats", index=False)
    df4.to_excel(writer, sheet_name="Full Voyage List", index=False)


#Χρειαζομαι το country επομενως πρεπει να το κανω merge στο df4

df_ports = pd.read_sql("SELECT port_id,country FROM Ports",conn)

df4 = df4.merge(
    df_ports,
    how= "left",
    left_on="arrival_port_id",
    right_on="port_id"
)

df4.rename(columns={"country": "ArrivalCountry"}, inplace=True)
df4.drop(columns=["port_id"],inplace=True)

pivot3 = df4.pivot_table(
    values="DurationDays",
    index="ShipName",
    columns="ArrivalCountry",
    aggfunc="sum",
    fill_value=0
)

with pd.ExcelWriter("total_voyage_hours_by_ship_and_arrival_port.xlsx",engine="openpyxl") as writer:
    pivot3.to_excel(writer,sheet_name="ShipVoyageHours x ArrivalPort")






