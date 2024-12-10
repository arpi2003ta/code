class Student:
    def __init__(self, classRoll, name, gender):
        # Constructor (__init__) initializes the object
        self.classRoll = classRoll
        self.name = name
        self.gender = gender
        print("Object initialized")  # Display message when object is created

    def showData(self):
        # Method to display the student information
        print(f"Class Roll: {self.classRoll}, Name: {self.name}, Gender: {self.gender}")

    def __del__(self):
        # Destructor (__del__) will be called when the object is destroyed
        print("Object destroyed")  # Display message when object is destroyed

# Create an object of the Student class
student1 = Student(8, "Arpita Nath", "Female")

# Display student information
student1.showData()

# Explicitly destroy the object using `del`
del student1  # This will call the destructor (__del__)

