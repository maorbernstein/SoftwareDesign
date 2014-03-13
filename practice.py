from math import *
def Ack(m,n):
    if m==0:
        return n+1
    if n==0:
        return Ack(m-1,1)
    else:
        return Ack(m-1,Ack(m,n-1))

def estimate_pi(last_term):
    i = 0
    estimate = 0
    while True:
        errorn =  2*(2**0.5)/9801 * factorial(4*i) * (1103+26390*i) /float((factorial(i)**4*396**(4*i)))
        print errorn
        i += 1
        estimate += errorn 
        if errorn < last_term:
            return float(estimate)**-1
print estimate_pi(10**-15)
