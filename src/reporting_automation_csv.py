import duckdb
import pandas as pd

def run_query_from_file(filepath):
    with open(filepath, "r") as f:
        sql = f.read()
    return duckdb.query(sql).to_df()


#Εκτελεση queries
df1 = run_query_from_file("sql/csv/avg_ship_travel_time.sql")
df2 = run_query_from_file("sql/csv/ship_revenues_per_arrival_port_per_ship.sql")
df3 = run_query_from_file("sql/csv/netProfit_per_ship.sql")

#Μέση διάρκεια ταξιδιού ανά πλοίο ανά μήνα
df1["Month"] = pd.to_datetime(df1["departure_date"]).dt.month

pivot1 = df1.pivot_table(
    values="DurationDays",
    index="ShipName",
    columns="Month",
    aggfunc="mean",
    fill_value=0
)
#Συνολικά έσοδα ανά χώρα άφιξης (Arrival Country) ανά πλοίο
pivot2 = df2.pivot_table(
    values="TotalRevenue",
    index="ShipName",
    columns="ArrivalCountry",
    aggfunc="sum",
    fill_value= 0
)

#Σύγκριση εσόδων και κόστους ανά πλοίο – Net Profit (έσοδα - fuel - operational cost)
pivot3 = df3.pivot_table(
    index="ShipName",
    values=["TotalRevenue", "TotalFuelCost", "TotalOperationalCost", "NetProfit"],
    aggfunc="sum"
)

#Αποθηκευση αποτελεσματων
with pd.ExcelWriter("reports/avg_ship_travel_time_per_month.xlsx",engine="openpyxl") as writer: 
    pivot1.to_excel(writer,sheet_name="AvgTravelTime x Month")

with pd.ExcelWriter("reports/ship_revenue_per_ArrivalCountry.xlsx",engine="openpyxl") as writer: 
    pivot2.to_excel(writer,sheet_name="ShipRevenue x Country")
    
with pd.ExcelWriter("reports/ship_profit_comparison.xlsx",engine="openpyxl") as writer: 
    pivot3.to_excel(writer,sheet_name="Profit Analysis")