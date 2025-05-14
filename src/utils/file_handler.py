import pandas as pd
import os

def read_employees(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    if file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    elif file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    else:
        raise ValueError("Unsupported file format. Use .csv or .xlsx")

def write_assignments(df, file_path):
    df.to_excel(file_path, index=False)



