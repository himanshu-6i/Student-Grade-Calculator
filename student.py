# Student Grade Calculator
# Author: Your Name
# Description: A simple Python project to calculate student grades based on marks.

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

def main():
    print("===== Student Grade Calculator =====")
    name = input("Enter Student Name: ")
    marks = []

    for i in range(1, 6):
        score = float(input(f"Enter marks for subject {i}: "))
        marks.append(score)

    total = sum(marks)
    avg = total / 5
    grade = calculate_grade(avg)

    print("\n===== RESULT =====")
    print(f"Name: {name}")
    print(f"Total Marks: {total}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")
    print("==============================")

if __name__ == "__main__":
      main()