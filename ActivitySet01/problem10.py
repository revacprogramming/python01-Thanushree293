# Dictionaries
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
counts = dict()
handle = open(name)
for line in handle:
    line = line.strip()
    if line.startswith('From ') :
        person = line.split()
        need = person[1]
        counts[need] = counts.get(need,0)+1
    else:
        continue
bigcount = None
bigword = None
for need,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = need
        bigcount = count  
print(bigword, bigcount)
