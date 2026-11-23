import json
cells = []
def md(text):
    cells.append({"cell_type":"markdown","metadata":{},"source":[text]})
def code(text):
    cells.append({"cell_type":"code","execution_count":None,"metadata":{},"outputs":[],"source":[text]})

md("# Week 10 Class 5 Capstone — Production Pipeline\n\n**Student:** Hauwa Ibrahym Kabara\n\nThis notebook runs the production pipeline and shows the results.")
md("## 1. Run Pipeline")
code("from src.production_pipeline import run_pipeline\nrun_pipeline('data/historical_production_capstone.csv', 'outputs')")
md("## 2. Show Cleaned Data")
code("import pandas as pd\npd.read_csv('outputs/cleaned_production.csv').head(10)")
md("## 3. Show Data Quality Report")
code("pd.read_csv('outputs/data_quality_report.csv')")
md("## 4. Show Daily Summary")
code("pd.read_csv('outputs/daily_production_summary.csv').head(12)")
md("## 5. Show Rejected Records")
code("pd.read_csv('outputs/rejected_source_records.csv')")
md("## Conclusion\n\n- Valid: 45, Rejected: 1 (invalid timestamp)\n- Cleaned: 48 rows after dedup (1 duplicate removed) + 4 gaps created\n- Daily summary: 12 rows (3 wells x 4 days)\n- Duplicate rule: keep last by ingested_at (oil=999 wins)\n- Gap rule: 6h grid, pressure interpolated max 1 slot")
nb = {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python", "version": "3.10.0"}}, "nbformat": 4, "nbformat_minor": 4}
open("notebook/Week10_Class5_Student_Capstone.ipynb","w").write(json.dumps(nb, indent=1))
print("notebook created")