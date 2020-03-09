import math

#Define dy/dt
def f(t, y):
    dy = 3 + math.exp(-t) - 0.5 * y
    return dy

def approx_ode(h, t0, y0, tn):
    while t0 < tn:
        y0 = y0 + h * (f(t0, y0))
        t0 += round(h, 1) #Trailing zeros
        t0 = round(t0, 1)
    return y0


print(approx_ode(0.1,0,1,5))
print(approx_ode(0.1,0,1,2.5))
print(approx_ode(0.1,0,1,3))
print(approx_ode(0.1,0,1,1))
print(approx_ode(0.1,0,1,0))