# Employee Competency Assessment Data Generator

This Python script generates dummy data for an employee competency assessment system and writes the data to CSV files. The generated data includes user information, competencies, assessments, and assessment results for the Employee Competency Tracker found here: https://github.com/FastEddyOne/EmployeeCompetencyTracker

## Dependencies

bcrypt: Used for hashing passwords securely.

### How to Use

Clone or download the repository to your local machine.

Install the required dependencies using the following command:


Copy code
```pip install bcrypt```

### Run the script:

Copy code
```python generate_data.py```

### CSV files (Users.csv, Competencies.csv, Assessments.csv, Assessment_Results.csv) will be generated in the same directory.

### Data Generated

#### Users
- user_id: Unique identifier for each user.
- first_name: User's first name.
- last_name: User's last name.
- email: User's email address.
- password_hash: Hashed password using bcrypt.
- active_status: Randomly assigned active status (0 or 1).
- date_created: Date when the user was created.
- hire_date: Random date between January 1, 2020, and January 1, 2023.
- user_type: User type, with "manager" assigned to every 10th user.

#### Competencies
- competency_id: Unique identifier for each competency.
- name: Name of the competency.
- date_created: Date when the competency was created.

#### Assessments

- assessment_id: Unique identifier for each assessment.
- name: Name of the assessment.
- competency_id: ID of the competency associated with the assessment.
- date_created: Date when the assessment was created.

#### Assessment Results

- result_id: Unique identifier for each assessment result.
- user_id: ID of the user who took the assessment.
- assessment_id: ID of the assessment.
- score: Randomly assigned score between 0 and 4.
- date_taken: Random date between January 1, 2021, and June 1, 2023.
- manager_id: ID of a randomly selected manager.

### Note

The script uses bcrypt to securely hash passwords before writing them to the CSV file.

The generated data is random and is intended for testing and development purposes only.

Feel free to modify the script to suit your specific needs or integrate it into your project.
