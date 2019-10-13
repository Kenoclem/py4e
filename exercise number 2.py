
eh= input("Enter Hours: ")
Enter Hours>? 50
er= input("Enter Rate: ")
Enter Rate>? 4.5
try:eh=
    eh=float(eh)
except ValueError:
    print("Error, please enter numeric input")
    sys.exit()

try:
    er=float(er)
except ValueError:
    print("Error, please enter numeric input")
    sys.exit()

if eh > 50:
    print("Pay: ", (50*er)+(eh-50)*4.5*er)
else:
    print("Pay: ", x*y)