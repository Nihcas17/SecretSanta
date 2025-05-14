import pandas as pd
from src.services.secret_santa_engine import SecretSantaEngine

def test_generate_assignments_no_self():
    employees = pd.DataFrame({
        'Employee_Name': ['A', 'B', 'C'],
        'Employee_EmailID': ['a@example.com', 'b@example.com', 'c@example.com']
    })
    previous = pd.DataFrame({
        'Employee_Name': ['A', 'B', 'C'],
        'Employee_EmailID': ['a@example.com', 'b@example.com', 'c@example.com'],
        'Secret_Child_Name': ['B', 'C', 'A'],
        'Secret_Child_EmailID': ['b@example.com', 'c@example.com', 'a@example.com']
    })

    engine = SecretSantaEngine(employees, previous)
    result = engine.generate_assignments()

    for _, row in result.iterrows():
        assert row['Employee_EmailID'] != row['Secret_Child_EmailID']
        assert previous.loc[previous['Employee_EmailID'] == row['Employee_EmailID'], 'Secret_Child_EmailID'].values[0] != row['Secret_Child_EmailID']

