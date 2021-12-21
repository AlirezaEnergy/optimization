import numpy as np
import matplotlib.pyplot as plt

def Bracketing(f, x_init, x_min, x_max,step = 1e-2, step_growth = 1.1, plotting_step = 0.01):
    # the aim is to find a<b<c such that f(a) > f(b) and f(b) < f(c)
    a, fa = x_init, f(x_init)
    
    if a + step < x_min or a + step > x_max:
        step = -step
    
    b, fb = a + step, f(a + step)
    
    X = np.arange(x_min,x_max+plotting_step,plotting_step)
    plt.figure(figsize = (6,4), dpi = 100)
    plt.plot(X,list(map(f,X)))
    plt.xlabel('X')
    plt.ylabel('f(x)')
    
    while True:
        
        if fb > fa: # this means our direction was wrong as we have growth
            step = -step    # change the movement direction
            a, b = b, a     # change the beginning and end of the interval
            fa, fb = fb, fa # ""
        
        c, fc = b + step, f(b + step)
        
        if c > x_max or c < x_min:
            if a > b:
                return (b,a)
            else:
                return (a,b)
        
        plt.scatter([a,b,c],[f(a),f(b),f(c)],c='r')
        
        if fb < fc: # we reached to an interval => end and return the interval
            if a < c:
                return (a,c)
            else:
                return (c,a)
    
        a, b = b, c
        fa, fb = fb, fc
        step = step * step_growth

f1 = lambda x: abs(x)
f2 = lambda x: x**2
f3 = lambda x: max(-x**3,x**2-150)

x_init = -2
min_, max_ = Bracketing(f3,x_init,x_min = -5, x_max = 10)
print(f'{(round(min_,3),round(max_,3))}')


























