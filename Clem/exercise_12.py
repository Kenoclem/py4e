str = input("Enter a string: ")
sli = slice(str.find(":") + 1, len(str))
num = float(str[sli])

print("Number:", num)
