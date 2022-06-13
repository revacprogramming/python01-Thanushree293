fname = input("Enter file name: ")
fh = open(fname)
ans = 0.0
count = 0

for line in fh:
        if not line.startswith("X-DSPAM-Confidence:") :
                continue
        else:
                ans = ans + float(line[20:])
                count = count + 1
print
print("Average spam confidence:", ans/count) 
#try this print(f"Average spam confidence: {sm/count}")
