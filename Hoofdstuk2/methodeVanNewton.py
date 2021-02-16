def newton(f, Df, x0, epsilon, max_iter):
    '''
    Parameters
    ------------
    f: Functie waar we de oplossing f(x)=0 voor zoeken
    Df: Afgeleide van f(x)
    x0: Eerste gok voor de oplossing van f(x)=0
    epsilon: Stop-criteria als abs(f(x)) < epsilon
    max_iter: Max aantal iteraties

    Returns
    ------------
    xn: bereken een lineare benadering van f(x) op xn en zoekt snijpunt door formule
            x = xn - f(xn)/Df(xn)
        Gaat verder tot abs(f(x)) < epsilon and returns xn.
        Als Df(xn)==0, return None. Als de aantal iteraties over max_iter gaat,
        return None.
    '''
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None


#Example: Supergolden ratio
#p(x) = x^3 - x^2 - 1

p = lambda x: x**3 - x**2 - 1
Dp = lambda x: 3*x**2 - 2*x
approx = newton(p,Dp,1,1e-10,10)
print(approx)
