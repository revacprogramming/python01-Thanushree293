# Loops & Iterators
score = float(input("Enter Score: "))
if score>=0.9:
      x='A'
elif score>=0.8:
      x='B'
elif score>=0.7:
      x='C'
elif score>=0.6:
      x='D'
elif score<0.6:
      x='F'
else:
      x='out of range"'
print(x)