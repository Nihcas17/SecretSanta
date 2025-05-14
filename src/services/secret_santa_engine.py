import pandas as pd
import random

class SecretSantaEngine:
    def __init__(self, employees_df, previous_assignments_df):
        self.employees_df = employees_df
        self.previous_assignments_df = previous_assignments_df

    def generate_assignments(self):
        employees = self.employees_df.copy()
        assigned = False
        max_attempts = 1000
        attempt = 0

        previous_map = dict(zip(
            self.previous_assignments_df['Employee_EmailID'],
            self.previous_assignments_df['Secret_Child_EmailID']
        ))

        while not assigned and attempt < max_attempts:
            attempt += 1
            shuffled = employees.sample(frac=1).reset_index(drop=True)
            merged = employees.assign(
                Secret_Child_Name=shuffled['Employee_Name'],
                Secret_Child_EmailID=shuffled['Employee_EmailID']
            )

            # Apply constraints
            valid = all(
                row['Employee_EmailID'] != row['Secret_Child_EmailID']
                and previous_map.get(row['Employee_EmailID']) != row['Secret_Child_EmailID']
                for _, row in merged.iterrows()
            )

            if valid:
                assigned = True
                return merged

        raise Exception("Failed to generate valid assignments after multiple attempts")

