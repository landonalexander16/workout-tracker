#1. A single logged set will be of an exercise, with a weight and number of repetitions.

#2. Each entry will need the date, the exercise, the weight, and the reps. Each set will be tracked together
#   i.e 2 sets of bench press will be one data entry just with two different reps

#3 The entries will be stored as a session (based on the date) and each session will include the exercises
#  which will include the sets and reps.

# A Session will need the fields: a list of Exercises and date
# An Exercise will need the fields: name and a list of Sets
# Set will need the fields: weight and reps

import json
import os

class Sets:
    def __init__(self, weight, reps):
        self.weight = weight
        self.reps = reps

    # This method converts the Sets instance into a dictionary format.
    def to_dict(self):
        return {
            "weight": self.weight,
            "reps": self.reps
        }

    #This method creates a new Sets instance from a dictionary containing the weight and reps values.
    @staticmethod
    def from_dict(data):
        return Sets(data["weight"], data["reps"])

class Exercise:
    def __init__(self, name):
        self.name = name
        self.sets = []

    def add_sets(self, sets):
        self.sets.append(sets)
        
    # This method prompts the user to input the weight and reps for a set, creates a Sets object, and adds it to the exercise's list of sets.    
    def add_set_to_exercise(self):
        # The while loop and try-except block is used to handle invalid input for weight and reps if the user enters a non-numeric value.
        while True:
            try:
                weight = float(input(f"Enter the weight for {self.name}: "))
                reps = int(input(f"Enter the number of reps for {self.name}: "))
                new_set = Sets(weight, reps)
                self.add_sets(new_set)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # This method converts the Exercise instance into a dictionary format, including the exercise name and a list of sets represented as dictionaries.
    def to_dict(self):
        return {
            "exercise": self.name,
            "sets": [s.to_dict() for s in self.sets]
        }

    # This method creates a new Exercise instance from a dictionary containing the exercise name and a list of sets represented as dictionaries.
    # It uses the from_dict method of the Sets class to create Sets objects for each set in the list.
    @staticmethod
    def from_dict(data):
        exercise = Exercise(data["exercise"])
        exercise.sets = [Sets.from_dict(s) for s in data["sets"]]
        return exercise



class Session:
    def __init__(self, date):
        self.date = date
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    # This method converts the Session instance into a dictionary format, including the session date and a list of exercises represented as dictionaries.
    def to_dict(self):
        return {
            "date": self.date,
            "exercises": [e.to_dict() for e in self.exercises]
        }

    # This method creates a new Session instance from a dictionary containing the session date and a list of exercises represented as dictionaries.
    # It uses the from_dict method of the Exercise class to create Exercise objects for each exercise in the list.
    @staticmethod
    def from_dict(data):
        session = Session(data["date"])
        session.exercises = [Exercise.from_dict(e) for e in data["exercises"]]
        return session

class WorkoutTracker:
    def __init__(self):
        self.sessions = []

    def add_session(self, session):
        self.sessions.append(session)

    # This method converts the WorkoutTracker instance into a dictionary format, including a list of sessions represented as dictionaries.
    def to_dict(self):
        return {
            "sessions": [s.to_dict() for s in self.sessions]
        }

    # This method creates a new WorkoutTracker instance and populates it with Session objects created from the provided dictionary data. 
    # It iterates through the list of sessions in the data, creating a Session object for each one using the from_dict method of the Session class,
    # and adds them to the sessions list of the WorkoutTracker instance.
    @staticmethod
    def from_dict(data):
        tracker = WorkoutTracker()
        tracker.sessions = [Session.from_dict(s) for s in data["sessions"]]
        return tracker

def main():
    # Loads existing workout data from a JSON file if it exists, otherwise creates a new WorkoutTracker instance
    if os.path.exists("workout_data.json"):
        with open("workout_data.json", "r") as f:
            data = json.load(f)
            tracker = WorkoutTracker.from_dict(data)
    else:
        tracker = WorkoutTracker()

    # Creates a session and adds it to the tracker
    input_date = input("Enter the date of the workout session(YYYY-MM-DD):")
    session = Session(input_date)
    tracker.add_session(session)

    # Creates Exercise object and adds it to the session
    # Unable to use a helper method because main() needs access to the current exercise when adding more sets
    exercise_name = input("Enter the name of the exercise:")
    exercise = Exercise(exercise_name)
    session.add_exercise(exercise)
   
    # Creates a set for the exercise and adds it to the exercise
    exercise.add_set_to_exercise()

    # A loop to allow the user to add more sets to the current exercise, start a new exercise, or finish the session
    while True:
        choice = input("Would you like to add another set to this exercise, start a new exercise, or done? (s/e/d): ").strip().lower()
        if choice == 's':
            exercise.add_set_to_exercise()
        elif choice == 'e':
            exercise_name = input("Enter the name of the exercise:")
            exercise = Exercise(exercise_name)
            session.add_exercise(exercise)
            exercise.add_set_to_exercise()
        elif choice == 'd':
            break
        else:
            print("Invalid choice. Please enter 's', 'e', or 'd'.")

    # Prints out the workout tracker details
    for session in tracker.sessions:
        print(f"Date: {session.date}")
        for exercise in session.exercises:
            print(f"Exercise: {exercise.name}")
            for sets in exercise.sets:
                print(f"Weight: {sets.weight}, Reps: {sets.reps}")


    # Saves the workout session details to a JSON file
    with open("workout_data.json", "w") as f:
        json.dump(tracker.to_dict(), f, indent=4)

if __name__ == "__main__":
    main()

    

