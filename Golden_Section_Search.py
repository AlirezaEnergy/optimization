import numpy as np
import matplotlib.pyplot as plt

def Golden_Section_Search(f, xL, xU, NFE, plotting_step = 0.1):
    # gives an interval in which the minimizer lies
    
    X = np.arange(xL,xU+plotting_step,plotting_step)
    plt.figure(figsize = (8,6), dpi = 100)
    plt.plot(X,list(map(f,X)))
    plt.title('Golden section search',fontname = 'Times New Roman', size = 20)
    plt.xlabel('X', size = 20, fontname = 'Times New Roman')
    plt.ylabel('f(x)', size = 20, fontname = 'Times New Roman')
    
    phi = (5**0.5 + 1)/2
    for i in range(NFE):
        d = (phi - 1)*(xU - xL)
        
        # always => xL < x2 < x1 < xU
        x1 = xL + d
        x2 = xU - d
        
        fx1, fx2 = f(x1), f(x2)
        
        if fx1 < fx2:
            # the answer is not less than x2 for sure so xL = x2
            xL = x2
        else:
            # fx1 > fx2 which means that the answer is not greater that x1 so xU = x1
            xU = x1
        
        xAVG = (xL+xU)/2
        plt.scatter([xAVG],[f(xAVG)], c = 'r')
        
    return (x1+x2)/2, f((x1+x2)/2)

f1 = lambda x: abs(x)
f2 = lambda x: x**2
f3 = lambda x: max(-x**3,x**2-150)
f4 = lambda x: 0.1 * x**2 - 2 * np.sin(x)

xL = -10
xU = 10
NFE = 10
Minimizer, Minimum = Golden_Section_Search(f4, xL, xU, NFE)

print(f'Minimizer = {round(Minimizer,3)}, Minimum = {round(Minimum,3)}')