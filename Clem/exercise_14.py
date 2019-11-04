f = open(input("Enter a file name: "))

num = []

hint = "X-DSPAM-Confidence:"

for line in f.readlines():
    if line.find(hint) != -1:
        sli = slice(line.find(":") + 1, len(line))
        num.append(float(line[sli]))

print("Average spam confidence: ", sum(num) / len(num))

f.close()