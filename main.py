#1. A single logged set will be of an exercise, with a weight and number of repetitions.

#2. Each entry will need the date, the exercise, the weight, and the reps. Each set will be tracked together
#i.e 2 sets of bench press will be one data entry just with two different reps

#3 The entries will be stored as a session (based on the date) and each session will include the exercises
# wich will include the sets and reps.

# A Session will need the fields: a list of Exercises and date
# An Exercise will need the fields: name and a list of Sets
# Set will need the fields: weight and reps

class Sets:
    def __init__(self, weight, reps):
        self.weight = weight
        self.reps = reps

class Exercise:
    def __init__(self, name):
        self.name = name
        self.sets = []

    def add_sets(self, sets):
        self.sets.append(sets)
        
    def add_set_to_exercise(self):
        weight = float(input(f"Enter the weight for {self.name}: "))
        reps = int(input(f"Enter the number of reps for {self.name}: "))
        new_set = Sets(weight, reps)
        self.add_sets(new_set)

class Session:
    def __init__(self, date):
        self.date = date
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

class WorkoutTracker:
    def __init__(self):
        self.sessions = []

    def add_session(self, session):
        self.sessions.append(session)

def main():
    tracker = WorkoutTracker()
    
    
    input_date = input("Enter the date of the workout session(YYYY-MM-DD):")
    session = Session(input_date)
    tracker.add_session(session)

    exercise_name = input("Enter the name of the exercise:")
    exercise = Exercise(exercise_name)
    session.add_exercise(exercise)

    exercise.add_set_to_exercise()

    print("Add another set to this exercise, start a new exercise, or done?")
    while True:
        choice = input("Enter your choice (s/e/d): ").strip().lower()
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

    for session in tracker.sessions:
        print(f"Date: {session.date}")
        for exercise in session.exercises:
            print(f"Exercise: {exercise.name}")
            for sets in exercise.sets:
                print(f"Weight: {sets.weight}, Reps: {sets.reps}")

if __name__ == "__main__":
    main()

    

