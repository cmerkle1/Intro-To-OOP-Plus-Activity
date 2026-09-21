
def get_student_with_more_classes(student_one, student_two):
    ''''
    This function accepts two params: student_one, student_two (instances of Student class)
    Returns 
    '''
    # Calls the get_num_classes method using two objects of Student
    classes_one = student_one.get_num_classes()
    classes_two = student_two.get_num_classes()

    # If student one contains more classes than student two, return one
    if classes_one > classes_two:
        return student_one.name

    # If both students have the same number of classes
    # Return statement stating that neither student has classes or
    # Return the classes for both students
    elif classes_one == classes_two:
        if classes_one == 0 and classes_two == 0:
            return "Both students do not have classes"
        else:
            return f"{student_one.name} and {student_two.name}"

    return student_two.name