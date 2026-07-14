# Student Grade Calculator

def calculate_grade(marks):
    """Returns grade and encouraging message based on marks."""

    if marks >= 90:
        return "A", "Outstanding! Keep up the excellent work!"
    elif marks >= 80:
        return "B", "Great job! You're doing really well."
    elif marks >= 70:
        return "C", "Good effort! Keep practicing to improve."
    elif marks >= 60:
        return "D", "You're passing! Work a little harder for better results."
    else:
        return "F", "Failure is not the end. Keep learning and try again!"


# Get student name
student_name = input("Enter student name: ")

# Input validation using while loop
while True:
    try:
        marks = float(input("Enter student marks (0-100): "))

        if 0 <= marks <= 100:
            break
        else:
            print("❌ Marks must be between 0 and 100. Please try again.")

    except ValueError:
        print("❌ Invalid input! Please enter a numeric value.")

# Calculate grade
grade, message = calculate_grade(marks)

# Display result
print("\n----- Result -----")
print("Student Name :", student_name)
print("Marks        :", marks)
print("Grade        :", grade)
print("Message      :", message)
