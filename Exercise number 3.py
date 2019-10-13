
Grade= input("Enter Score: ")

try:
    G= float(G)

except:
    print("Error message")
    quit()

if G == 1.0:
    print("A")
elif 1.0 > G >= 0.9:
    print("A")
elif 0.9 > G >= 0.8:
    print("B")
elif 0.8 > G >= 0.7
    print("C")
elif 0.7 > G >= 0.6
    print("D")
elif 0.6 > G >= 0.5
    print("E")
else:
    print("Error Message")