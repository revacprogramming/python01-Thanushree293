
def add(a, b):
    sum= (a+b)
    return(sum)
  
def output(a, b, sum):
    print("sum of two no's {0}+{1} = {2}".format(a,b,sum))
def main():
    a, b = map(int,input('input?').split())
    sum = add(a, b)
    output(a, b,sum)

if __name__ == '__main__':
    main()
#not proper