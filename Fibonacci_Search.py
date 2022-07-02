import numpy as np
import matplotlib.pyplot as plt

def Fibonacci_Search(f,a,b,num_iter,eps,plotting_step = 0.1, plot_function=True, plot_best_sols=True):
    """
    f:          univariate function to be minimized.
    a:          The beginning of the search interval.
    b:          End of search interval.
    num_iter:   Number of search iteration
    esp:        sufficient small number

    returns an interval in which the minimizer lies
    """
    if plot_function:
        X = np.arange(a,b+plotting_step,plotting_step)
        plt.figure(figsize = (8,6), dpi = 100)
        plt.plot(X,list(map(f,X)))
        plt.title('Fibonacci Search',fontname = 'Times New Roman', size = 20)
        plt.xlabel('X', size = 20, fontname = 'Times New Roman')
        plt.ylabel('f(x)', size = 20, fontname = 'Times New Roman')
    
    phi = (1+5**0.5)/2
    s = (1-5**0.5)/(1+5**0.5)
    rho = (1-s**num_iter) / ( phi*(1-s**(num_iter+1) ) )
    
    d = rho * b + (1-rho) * a
    fd = f(d)
    
    Sols = []
    Sols.append((a+b)/2)
    for i in range(1, num_iter):
        
        if i == num_iter-1:
            c = eps * a + (1-eps) * d
        else:
            c = rho * a + (1-rho) * b
        
        fc = f(c)
        if fc < fd:
            b, d, fd = d, c, fc
        else:
            a, b = b, c
        
        rho = (1-s**(num_iter-i)) / ( phi*(1-s**(num_iter-i+1)) )
        
        Sols.append((a+b)/2)
        
        if plot_function:
            xAVG = (a+b)/2
            plt.scatter([xAVG],[f(xAVG)], c = 'r')
    
    if plot_best_sols:
        plt.figure(figsize = (8,6), dpi = 100)
        plt.plot(list(range(0,len(Sols))),list(map(f,Sols)))
        plt.title('Best solutions',fontname = 'Times New Roman', size = 20)
        plt.xlabel('Iteration', size = 20, fontname = 'Times New Roman')
        plt.ylabel('f(best solutions)', size = 20, fontname = 'Times New Roman')
    
    
    return (a,b) if a<b else (b,a)
    
#f = lambda x: x**4 - 14*x**3 + 60*x**2 - 70*x # over [0,2]
#f = lambda x: x**5 - 3*x**4 + 5               # over [0,4]
#f = lambda x: x**4 - x
#f = lambda x: max(-x**3,x**2-150)
f = lambda x: 0.1 * x**2 - 2 * np.sin(x)

a, b = -10,10     # determine the search interval
(L,U) = Fibonacci_Search(f,a,b,num_iter=10,eps=0.01)

print(f"Minimizer = {round((L+U)/2,3)}")
print(f"Minimum = {round(f((L+U)/2),3)}")
