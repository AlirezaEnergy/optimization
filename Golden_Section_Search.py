import numpy as np
import matplotlib.pyplot as plt

def Golden_Section_Search(f, xL, xU, num_iter, plotting_step = 0.1, plot_function=True, plot_best_sols=True):
    """
    f:          univariate function to be minimized.
    xL:         The beginning of the search interval.
    xU:         End of search interval.
    num_iter:   Number of search iteration

    returns an interval in which the minimizer lies
    """
    if plot_function:
        X = np.arange(xL,xU+plotting_step,plotting_step)
        plt.figure(figsize = (8,6), dpi = 100)
        plt.plot(X,list(map(f,X)))
        plt.title('Golden section search',fontname = 'Times New Roman', size = 20)
        plt.xlabel('X', size = 20, fontname = 'Times New Roman')
        plt.ylabel('f(x)', size = 20, fontname = 'Times New Roman')
    
    phi = (5**0.5 + 1)/2

    Sols = []
    Sols.append((xL+xU)/2)
    for i in range(num_iter):
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
        if plot_function:
            xAVG = (xL+xU)/2
            plt.scatter([xAVG],[f(xAVG)], c = 'r')
        
        Sols.append((xL+xU)/2)

    if plot_best_sols:
        plt.figure(figsize = (8,6), dpi = 100)
        plt.plot(list(range(0,len(Sols))),list(map(f,Sols)))
        plt.title('Best solutions',fontname = 'Times New Roman', size = 20)
        plt.xlabel('Iteration', size = 20, fontname = 'Times New Roman')
        plt.ylabel('f(best solutions)', size = 20, fontname = 'Times New Roman')

    return (x1+x2)/2, f((x1+x2)/2)

#f = lambda x: x**4 - 14*x**3 + 60*x**2 - 70*x # over [0,2]
#f = lambda x: x**5 - 3*x**4 + 5               # over [0,4]
#f = lambda x: x**4 - x
#f = lambda x: max(-x**3,x**2-150)
f = lambda x: 0.1 * x**2 - 2 * np.sin(x)

xL = -10
xU = 10
num_iter = 10
Minimizer, Minimum = Golden_Section_Search(f, xL, xU, num_iter)

print(f'Minimizer = {round(Minimizer,3)}, Minimum = {round(Minimum,3)}')