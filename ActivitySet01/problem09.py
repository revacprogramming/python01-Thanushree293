# Lists
romeo = "But soft what light through yonder window breaksIt is the east and Juliet is the sun Arise fair sun and kill the envious moon Who is already sick and pale with grief"
fname = "enter the file name"
fh = open(fname)
lst = list()
for line in fh:
    for i in line.rstrip().split(' '):
        lst.append(i)
lst = list(set(lst))
lst.sort()
print(lst)
print
