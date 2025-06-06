# Navios ERP Reporting Automation

This project simulates supporting on ERP systems in a maritime environment.  
It demonstrates how to:

- Connect to a SQL Server ERP database
- Extract and transform voyage data using Python and SQL
- Generate monthly KPIs like average voyage duration per ship
- Export reports to Excel with dynamic filters

## Folder Structure

- `src/` – Python scripts for extraction, filtering, pivoting, exporting
- `sql/` – Queries used for data extraction
- `reports/` – Generated reports (Excel)
- `requirements.txt` – Python dependencies

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Configure SQL connection in [reporting_automation.py](src/reporting_automation.py)
3. Run script :
   ```bash
   python src/reporting_automation.py
