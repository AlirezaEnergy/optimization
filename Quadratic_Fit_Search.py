import numpy as np
import matplotlib.pyplot as plt

def Quadratic_Fit_Search(f,x,accuracy,plot_best_sols = True):
    """
        f:          the input function
        x:          list of three initial guesses
        accuracy:   the answer accuracy (the less, the more accurate)
    """
    Sols = []
    iteration = 0
    diff = 1
    while diff > accuracy:
    
        y = list(map(f,x))
        
        Coefs = np.polynomial.polynomial.polyfit(x,y,deg = 2)
        
        Derivative_Root = -Coefs[1]/(2*Coefs[2])
        
        if Derivative_Root > x[1]:
            diff = abs(Derivative_Root-x[1])
            x = [x[1],Derivative_Root,x[2]]
        else:
            diff = abs(Derivative_Root-x[1])
            x = [x[0],Derivative_Root,x[1]]
        
        Sols.append(x[1])
        
        iteration += 1
    
    if plot_best_sols:
        plt.figure(figsize = (6,4), dpi = 120)
        plt.plot(range(iteration),list(map(f,Sols)))
        plt.title('Quadratic fit search',fontname = 'Times New Roman', size = 20)
        plt.xlabel('Iteration', size = 20, fontname = 'Times New Roman')
        plt.ylabel('Minimum', size = 20, fontname = 'Times New Roman')
    
    return x[1],f(x[1]),Sols

f = lambda x: x**4 - 14*x**3 + 60*x**2 - 70*x
g = lambda x: 0.1 * x**2 - 2 * np.sin(x)

x = [0,1,2]
accuracy = 0.001
Minimizer, Minimum, Sols = Quadratic_Fit_Search(f,x,accuracy)

print(f'Minimizaer = {round(Minimizer,4)}')
print(f'Minimum = {round(Minimum,4)}')