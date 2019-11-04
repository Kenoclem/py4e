numbers = []

while True:
    val = input("Enter a number: ")

    if val != "done":
        try:
            numbers.append(int(val))
        except ValueError:
            print("Error, please enter numeric input.")
    else:
        print("Minimum:", min(numbers))
        print("Maximum:", max(numbers))
        break