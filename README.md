Secret Santa Assignment Automation 🎅
This project is designed to automate the Secret Santa assignment process for a company. It takes an employee list (with names and emails) and automatically assigns each employee a "Secret Child" while ensuring:

No one gets themselves...

No one gets the same child as the previous year...

Every employee has exactly one unique child...

The system reads data from CSV or Excel files, processes the assignments using a randomized but rule-validated approach, and generates a neat Excel file with the results.
All logic is cleanly structured using object-oriented design, ensuring it’s modular and easy to update for future needs.

Setup & Requirements:

Install required packages using:

pip install pandas openpyxl

How to Run:

python -m src.main

The program will:

Read the provided data.

Generate safe, conflict-free assignments.

Output results in data/secret_santa_result.xlsx.

All error handling and logging are done to make the process smooth and foolproof.

IMPORTANT : CREATE A FOLDER NAMED DATA AND PLACE THE EMPLOYEES.CSV AND PREVIOUS_ASSIGNMENT.CSV INSIDE THE SECRETSANTA PROJECT FOLDER
