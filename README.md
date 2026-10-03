# Workout Tracker

A command-line Python application that logs workout sessions, tracks exercises and sets, and persists data between runs.

## Features

- Log workout sessions by date (with date format validation)
- Track multiple exercises per session, each with multiple sets (weight + reps)
- Input validation with retry loops - invalid input is caught and re-prompted
- Persistent storage via JSON - previous sessions automatically load back in on startup, so data survives between runs
- Sessions are automatically sorted chronologically by date

## Setup

1. Clone the repo:
   git clone https://github.com/lalexander16/workout-tracker.git
   cd workout-tracker
2. (Optional) Create and activate a virtual environment:
   python -m venv venv
   venv\Scripts\activate # Windows
   source venv\bin\activate # Mac\Linux
3. Run the program:
   python main.py

## Usage
When you run the program, you'll be prompted to log a workout session:

- Enter the date of the workout session (YYYY-MM-DD): 2026-10-01
- Enter the name of the exercise: Bench Press
- Enter the weight for Bench Press: 135
- Enter the number of reps for Bench Press: 8
- Would you like to add another set to this exercise, start a new exercise, or done (s/e/d): s
- Enter the weight for Bench Press: 135
- Enter the number of reps for Bench Press: 6
  ...

At the end of the session, your data is saved to 'workout_data.json'. sorted chronologically by date. The next time you run the program, it automatically loads previous sessions.

## Technical notes

- **Object-oriented design**: data is modeled as a 'Session' containing multiple 'Exercise' objects, each containing multiple 'Sets' objects (one per logged set).
- **Serialization**: each class implements a 'to_dict()' method, recursively building a nested dictionary from the object hierarchy for JSON export. The reverse process ('from_dict()' static methods) rebuilds full object instances from loaded JSON data.
- **Input validation**: numeric input (weight, reps) and date input are each wrapped in 'try'/'except' retry loops, so malformed input prompts a re-ask instead of crashing the program.
- **Sorting** sessions are sorted chronologically using Python's 'sorted()' with a 'lambda' key function, relying on a consistent 'YYYY-MM-DD' date format for correct string-based ordering.

## Demo Video

https://github.com/user-attachments/assets/6fc797c6-6927-4bd4-b7a4-2af691fa4d53

## Planned Features
- Analytics: max weight per exercise, total volume per session. plateau detection
- Data visualization with matplotlib (progress charts over time)
- Web version (Flask or Django) with a persistent database backend

