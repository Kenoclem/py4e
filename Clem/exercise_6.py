def computepay(hours, rate):
    return min(hours, 40) * rate + ((hours - 40) * (15 if hours > 40 else 1))

try:
    h = int(input("Enter Hours: "))
    r = int(input("Enter Rate: "))
except ValueError:
    print("Error, please enter numeric input.")
else:
    print("Pay:", computepay(h, r))
