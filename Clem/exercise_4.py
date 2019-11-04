try:
    hours = int(input("Enter Hours: "))
    rate = int(input("Enter Rate: "))
except ValueError:
    print("Error, please enter numeric input.")
else:
    print("Pay:", min(hours, 40) * rate + ((hours - 40) * (15 if hours > 40 else 1)))
