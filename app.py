import csv
import bcrypt
import random
from datetime import datetime, timedelta

# Function to hash a password
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Function to generate a random date
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randrange(delta.days)
    return start_date + timedelta(days=random_days)

# Dummy names for users
first_names = ["John", "Jane", "Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Ian", "Julia", "Kevin", "Linda", "Mike", "Nancy", "Oscar", "Pamela", "Quincy", "Rachel", "Steve", "Tina", "Uma", "Victor", "Wendy", "Xander", "Yara", "Zack"]
last_names = ["Smith", "Johnson", "Brown", "Taylor", "Miller", "Davis", "Wilson", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores"]

# Generate Users Data
users = []
for i in range(1, 101):
    user = {
        "user_id": i,
        "first_name": random.choice(first_names),
        "last_name": random.choice(last_names),
        "email": f"user{i}@example.com",
        "password": "password123",
        "active_status": random.choice([0, 1]),
        "hire_date": random_date(datetime(2020, 1, 1), datetime(2023, 1, 1)).strftime('%Y-%m-%d'),
        "user_type": "manager" if i % 10 == 0 else "user"
    }
    users.append(user)

# Generate Competencies Data
competency_names = [f"Competency {i}" for i in range(1, 101)]
competencies = [{"competency_id": i, "name": name, "date_created": random_date(datetime(2020, 1, 1), datetime(2023, 1, 1)).strftime('%Y-%m-%d')} for i, name in enumerate(competency_names, start=1)]

# Generate Assessments Data
assessments = [{"assessment_id": i, "name": f"Assessment {i}", "competency_id": random.randint(1, 100), "date_created": random_date(datetime(2021, 1, 1), datetime(2023, 1, 1)).strftime('%Y-%m-%d')} for i in range(1, 101)]

# Generate Assessment Results Data
assessment_results = []
for i in range(1, 201):
    result = {
        "result_id": i,
        "user_id": random.randint(1, 100),
        "assessment_id": random.randint(1, 100),
        "score": random.randint(0, 4),
        "date_taken": random_date(datetime(2021, 1, 1), datetime(2023, 6, 1)).strftime('%Y-%m-%d'),
        "manager_id": random.choice([user['user_id'] for user in users if user['user_type'] == 'manager'])
    }
    assessment_results.append(result)

# Write to CSV
def write_to_csv(file_name, field_names, data):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

# Update users data with hashed passwords and created date
for user in users:
    user["password_hash"] = hash_password(user["password"])
    del user["password"]  # remove plain password
    user["date_created"] = random_date(datetime(2020, 1, 1), datetime(2023, 1, 1)).strftime('%Y-%m-%d')

# Write data to CSV files
write_to_csv('Users.csv', ['user_id', 'first_name', 'last_name', 'email', 'password_hash', 'active_status', 'date_created', 'hire_date', 'user_type'], users)
write_to_csv('Competencies.csv', ['competency_id', 'name', 'date_created'], competencies)
write_to_csv('Assessments.csv', ['assessment_id', 'name', 'competency_id', 'date_created'], assessments)
write_to_csv('Assessment_Results.csv', ['result_id', 'user_id', 'assessment_id', 'score', 'date_taken', 'manager_id'], assessment_results)

print("CSV files generated successfully.")
