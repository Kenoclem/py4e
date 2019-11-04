try:
    score = float(input("Enter score: "))

    if score >= 1 or score <= 0:
        print('Score is out of range.')
    elif score >= 0.9:
        grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    else:
        grade = 'F'

    if score < 1 and score > 0:
        print('Grade:', grade)

except ValueError:
    print('Error, please enter numeric input.')
