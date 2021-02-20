from datetime import datetime
startTime = datetime.now()

def newton(f, Df, x0, epsilon, max_iter):
    '''
    Parameters
    ------------
    f:          Functie waar we de oplossing f(x)=0 voor zoeken
    Df:         Afgeleide van f(x)
    x0:         Eerste gok voor de oplossing van f(x)=0
    epsilon:    Stop-criteria als abs(f(x)) < epsilon
    max_iter:   Max aantal iteraties

    Returns
    ------------
    xn:         zelfde als newton, maar niet elke keer afgeleide berekenen.
    '''
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfx0 = Df(x0)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfx0
    print('Exceeded maximum iterations. No solution found.')
    return None