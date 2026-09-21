from activity.student import Student # Importing Student class to create objects
from activity.comparison import get_student_with_more_classes # Importing the function being tested

# ---------- Test Data ----------
NAME_1 = "Samara"
GRADE_1 = "junior"
CLASSES_1 = [
    "Pre-Calc", 
    "English III", 
    "World History", 
    "Gym", 
    "Chemistry",
    "Music Composition"
]

NAME_2 = "Claire"
GRADE_2 = "freshman"
CLASSES_2 = [
    "Algebra", 
    "Writing", 
    "Contemporary World Issues", 
    "Gym", 
    "Earth Science"
]

# Testing one student with more classes
def test_get_student_name_with_more_classes():
    # ----- Arrange Section -----
    # Two test sets using data from above
    name_1 = NAME_1
    grade_1 = GRADE_1
    classes_1 = list(CLASSES_1)
    student_1 = Student(name_1, grade_1, classes_1) # Creates a student object

    name_2 = NAME_2
    grade_2 = GRADE_2
    classes_2 = list(CLASSES_2)
    student_2 = Student(name_2, grade_2, classes_2) # Creates the second student object

    # ----- Act Section -----
    # Calls the imported get_student_with_more_classes method
    result = get_student_with_more_classes(student_1, student_2)

    # ----- Assert Section -----
    # Asserts that Samara has more classes (6) than Claire (5)
    assert result == "Samara"


# Testing students that have the same no of classes
def test_get_student_names_with_same_no_of_classes():
    # ----- Arrange Section -----
    # Using test sets defined at the beginning of .py
    name_1 = NAME_1
    grade_1 = GRADE_1
    classes_1 = ["Class1", "Class2", "Class3"]
    student_1 = Student(name_1, grade_1, classes_1) # Creates the 1st student object

    name_2 = NAME_2
    grade_2 = GRADE_2
    classes_2 = ["Class1", "Class2", "Class3"]
    student_2 = Student(name_2, grade_2, classes_2) # Creates a 2nd student object

    # ----- Act Section -----
    # Calls the imported get_student_with_more_classes function
    result = get_student_with_more_classes(student_1, student_2)

    # ----- Assert Section -----
    # Asserts that Samara and Claire have the same number of classes
    assert result == "Samara and Claire"


# Testing students that both have zero classes
def test_get_student_names_with_same_no_of_classes_zero():
    # ----- Arrange Section -----
    # Uses testing data from above, leaving classes_1 and classes_2 as empty lists
    name_1 = NAME_1
    grade_1 = GRADE_1
    classes_1 = []
    student_1 = Student(name_1, grade_1, classes_1) # Creates a Student object

    name_2 = NAME_2
    grade_2 = GRADE_2
    classes_2 = []
    student_2 = Student(name_2, grade_2, classes_2) # Creates the second Student object

    # ----- Act Section -----
    # Calls the get_student_with_more_classes method
    result = get_student_with_more_classes(student_1, student_2) 

    # ----- Assert Section -----
    # Since both classes lists are empty, the assertion is that neither student has classes
    assert result == "Both students do not have classes"
