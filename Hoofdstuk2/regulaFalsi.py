from datetime import datetime
startTime = datetime.now()

def regulaFalsi(f,x0,x1,e):
    step = 1
    print('\n\n*** REGULA FALSI METHODE ***')
    condition = True
    if f(x0) * f(x1) > 0.0:
        print('Gegeven gok waarden kunnen geen nulpunt vinden.')
        print('Probeer opnieuw met nieuwe waarden.')
    else:
        while condition:
            x2 = x0 - (x1-x0) * f(x0) / ( f(x1) - f(x0) )
            print('Iteratie-%d, x2 = %0.6f en f(x2) = %0.6f' % (step, x2, f(x2)))
            
            if f(x0) * f(x2) < 0:
                x1 = x2
            else:
                x0 = x2
            
            step = step + 1
            condition = abs(f(x2)) > e

        print('\nGevonden nulpunt is: %0.8f' % x2)
        time = datetime.now() - startTime
        print('Time: {time}'.format(time = time))

p= lambda x: x**3 - x**2 - 1
x0 = 1
x1 = 2
e = 0.00001

regulaFalsi(p, x0, x1, e)
    
    
