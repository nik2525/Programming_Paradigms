def calculate_average(grades):
    """
    Calculate the average grade of a list of grades.

    :param grades: A list of student grades
    :return: The average grade
    """
    total = sum(grades)
    return total / len(grades)


def find_highest_grade(grades):
    """
    Find the highest grade in a list of grades.

    :param grades: A list of student grades
    :return: The highest grade
    """
    return max(grades)


def find_lowest_grade(grades):
    """
    Find the lowest grade in a list of grades.

    :param grades: A list of student grades
    :return: The lowest grade
    """
    return min(grades)


def count_above_threshold(grades, threshold):
    """
    Count the number of students with grades above a certain threshold.

    :param grades: A list of student grades
    :param threshold: The threshold grade
    :return: The number of students with grades above the threshold
    """
    return sum(1 for grade in grades if grade > threshold)


def main():
    try_again = True
    while try_again:
        grades = []
        num_students = int(input("Enter the number of students: "))
        for i in range(num_students):
            while True:
                try:
                    grade = int(input(f"Enter the grade for student {i + 1}: "))
                    if grade < 0 or grade > 100:
                        print("Grade must be between 0 and 100.")
                    else:
                        grades.append(grade)
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

        highest_grade = find_highest_grade(grades)
        lowest_grade = find_lowest_grade(grades)
        avg_grade = calculate_average(grades)

        print(f"The highest grade is {highest_grade} and the lowest grade is {lowest_grade}.")
        print(f"The average grade is {avg_grade:.2f}")

        while True:
            try:
                threshold = int(input("Enter the threshold grade: "))
                if threshold < 0 or threshold > 100:
                    print("Threshold grade must be between 0 and 100.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        num_above_threshold = count_above_threshold(grades, threshold)
        print(f"{num_above_threshold} students have grades above {threshold}.")

        choice = input("Do you want to try again? (yes/no): ")
        if choice.lower() != 'yes':
            try_again = False


if __name__ == "__main__":
    main()
