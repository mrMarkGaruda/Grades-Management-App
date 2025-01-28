# Student Dashboard - README

## Overview
This project displays student grades and averages in a dashboard. The dashboard fetches data from a Django API.

## How to Run

1. **Start the Django API:**
   - Run your Django server at `http://127.0.0.1:8000/api`.

2. **Set Up Flask App:**
   - Install Flask and `requests`:
     ```bash
     pip install flask requests
     ```
   - Run the Flask app:
     ```bash
     python app.py
     ```

3. **Access the Dashboard:**
   - Open your browser and go to `http://127.0.0.1:5000`.

## Features
- **Django Application:**
  - Manage students, subjects, and grades through REST API endpoints.
  - Record multiple grades per student for each subject.
- **Flask Application:**
  - Fetches and processes data from the Django API.
  - Calculates and displays:
    - Students’ average grades per subject and overall.
    - Rankings of students based on their average grades.
  - Displays grades for each subject under their respective categories.
