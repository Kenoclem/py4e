def computegrade(score):
    if score >= 1 or score <= 0:
        print("Score is out of range.")
        return
    elif score >= 0.9:
        grade = "A"
    elif score >= 0.8:
        grade = "B"
    elif score >= 0.7:
        grade = "C"
    elif score >= 0.6:
        grade = "D"
    else:
        grade = "F"

    return grade

try:
    print("Grade:", computegrade(float(input("Enter score: "))))

except ValueError:
    print("Error, please enter numeric input.")
