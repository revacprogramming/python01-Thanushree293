
def f(*args,**kwags):
  print(args,*args,kwags)

f (1,2,3,a=2,b=3,c=4)