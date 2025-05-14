from src.services.secret_santa_engine import SecretSantaEngine
from src.utils.file_handler import read_employees, write_assignments

def main():
    employees = read_employees('data/employees.csv')
    prev_assignments = read_employees('data/previous_assignments.csv')

    engine = SecretSantaEngine(employees, prev_assignments)
    try:
        assignments = engine.generate_assignments()
        write_assignments(assignments, 'data/secret_santa_result.xlsx')
        print("Secret Santa assignments created successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()


