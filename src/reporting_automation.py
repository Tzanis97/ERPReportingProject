import pyodbc
import pandas as pd

#Συνδεση με τον SQL Server
conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost;"
    "Database=ShippingDB;"
    "Trusted_Connection=yes;"
)

# Ποια πλοία έκαναν τα περισσότερα ταξίδια το 2024
query1 = """SELECT 
    s.name AS ShipName,
    COUNT(v.voyage_id) AS VoyageCount
FROM Voyages v
JOIN Ships s ON v.ship_id = s.ship_id
WHERE YEAR(v.departure_date) = 2024
GROUP BY s.name
ORDER BY VoyageCount DESC;
"""

# Μέση διάρκεια ταξιδιού ανά πλοίο (σε μέρες)
query2 = """SELECT 
    v.voyage_id,
    s.name AS ShipName,
    dp.name AS DeparturePort,
    ap.name AS ArrivalPort,
    v.departure_date,
    v.arrival_date,
    DATEDIFF(DAY, v.departure_date, v.arrival_date) AS DurationDays
FROM Voyages v
JOIN Ships s ON v.ship_id = s.ship_id
JOIN Ports dp ON v.departure_port_id = dp.port_id
JOIN Ports ap ON v.arrival_port_id = ap.port_id
ORDER BY v.departure_date;
"""

# Ποια ήταν τα πιο συχνά λιμάνια άφιξης
query3 = """SELECT 
    p.name AS ArrivalPort,
    COUNT(*) AS Arrivals
FROM Voyages v
JOIN Ports p ON v.arrival_port_id = p.port_id
GROUP BY p.name
ORDER BY Arrivals DESC;
"""

# Λίστα όλων των ταξιδιών με πλήρη στοιχεία
query4 = """SELECT 
    v.voyage_id,
    s.name AS ShipName,
    dp.name AS DeparturePort,
    ap.name AS ArrivalPort,
    v.departure_date,
    v.arrival_date,
    DATEDIFF(DAY, v.departure_date, v.arrival_date) AS DurationDays
FROM Voyages v
JOIN Ships s ON v.ship_id = s.ship_id
JOIN Ports dp ON v.departure_port_id = dp.port_id
JOIN Ports ap ON v.arrival_port_id = ap.port_id
ORDER BY v.departure_date;
"""

#Εκτελεση και αποθηκευση αποτελεσματων 
df1 = pd.read_sql(query1,conn)
df2 = pd.read_sql(query2,conn)
df3 = pd.read_sql(query3,conn)
df4 = pd.read_sql(query4,conn)


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






