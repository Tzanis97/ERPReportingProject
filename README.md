# ERP Reporting Automation (csv)

This project simulates supporting on ERP systems in a maritime environment.  
It demonstrates how to:

- Load ERP-related voyage, ship, and port data from CSV files
- Generate analytical reports with Python and Pandas
- Build pivot tables for KPIs such as:
  - Average voyage duration per ship and month
  - Revenue per arrival country per ship
  - Profit vs. cost per ship
- Export reports to Excel

## Folder Structure

- `src/reporting_automation_csv.py` – Python scripts for extraction, filtering, pivoting, exporting
- `sql/csv` – Queries used for data extraction
- `reports/csv` – Generated reports (Excel)
- `requirements.txt` – Python dependencies

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Run script :
   ```bash
   python src/reporting_automation_csv.py


# ERP Reporting Automation (SQL Server version)

Similar demonstration as before:

- Connect to a SQL Server ERP database
- Extract and transform voyage data using Python and SQL
- Generate monthly KPIs like average voyage duration per ship
- Export reports to Excel

## Folder Structure

- `src/reporting_automation.py` – Python scripts for extraction, filtering, pivoting, exporting
- `sql/sql_server` – Queries used for data extraction
- `reports/sql_server` – Generated reports (Excel)
- `requirements.txt` – Python dependencies

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Configure SQL connection in [reporting_automation.py](src/reporting_automation.py)

3. Run script :
   ```bash
   python src/reporting_automation.py
