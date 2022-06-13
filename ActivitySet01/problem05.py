# Functions
def computepay(h, r):
    if h>40:
        p = 1.5 * r * (h-40)+(40 *r)
    else:#also can use elif
        p =h*r
    return p
hrs = float(input("Enter Hours:"))
rphrs = float(input("Enter rate per hour:"))
p = computepay(hrs,rphrs)
print("Pay", p)