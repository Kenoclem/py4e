hours = int(input("Enter Hours: "))

print(
    "Pay:",
    min(hours, 40) * int(input("Enter Rate: "))
    + ((hours - 40) * (15 if hours > 40 else 1)),
)
