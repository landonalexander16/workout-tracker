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

    def add_set(self, Sets):
        self.sets.append(Sets)

class Session:
    def __init__(self, date):
        self.date = date
        self.exercises = []

    def add_exercise(self, Exercise):
        self.exercises.append(Exercise)

class WorkoutTracker:
    def __init__(self):
        self.sessions = []

    def add_session(self, Session):
        self.sessions.append(Session)

def main():
    tracker = WorkoutTracker()
    
    new_workout = Session("2023-01-01")
    new_workout.add_exercise(Exercise("Bench Press"))
    new_workout.exercises[0].add_set(Sets(50, 10))
    new_workout.exercises[0].add_set(Sets(50, 8))
    tracker.add_session(new_workout)

    second_workout = Session("2023-01-02")
    second_workout.add_exercise(Exercise("Squat"))
    second_workout.exercises[0].add_set(Sets(100, 5))
    second_workout.exercises[0].add_set(Sets(100, 3))
    tracker.add_session(second_workout)

    for session in tracker.sessions:
        print(f"Date: {session.date}")
        for exercise in session.exercises:
            print(f"Exercise: {exercise.name}")
            for set in exercise.sets:
                print(f"Weight: {set.weight}, Reps: {set.reps}")

if __name__ == "__main__":
    main()

    

