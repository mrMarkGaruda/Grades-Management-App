from flask import Flask, render_template
import requests

app = Flask(__name__)

# Base URL of the Django API
API_BASE_URL = "http://127.0.0.1:8000/api"  # Ensure this matches the Django server address

@app.route('/')
def dashboard():
    try:
        # Fetch data from the Django API
        students = requests.get(f"{API_BASE_URL}/students/").json()
        subjects = requests.get(f"{API_BASE_URL}/subjects/").json()
        grades = requests.get(f"{API_BASE_URL}/grades/").json()
    except requests.exceptions.RequestException as e:
        return f"Error fetching data from the API: {e}"

    # Organize and calculate average grades per student
    student_grades = {student['id']: [] for student in students}
    for grade in grades:
        student_grades[grade['student']].append(grade['grade'])

    averages = {
        student_id: sum(grades) / len(grades) if grades else 0
        for student_id, grades in student_grades.items()
    }

    # Create the final data structure for the template
    student_data = [
        {
            "name": next(student['name'] for student in students if student['id'] == student_id),
            "average": average
        }
        for student_id, average in averages.items()
    ]

    # Sort students by average grade for ranking
    student_data.sort(key=lambda x: x['average'], reverse=True)

    return render_template("dashboard.html", students=student_data, subjects=subjects)

if __name__ == "__main__":
    app.run(debug=True)