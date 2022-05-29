# Strings
text = "X-DSPAM-Confidence:    0.8475"
Pos=text.find(':')
print(Pos)
value=text[Pos+1:]
print(value)
result=float(value)
print(result)