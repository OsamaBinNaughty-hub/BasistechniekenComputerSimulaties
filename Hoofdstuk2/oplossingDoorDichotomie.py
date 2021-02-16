from datetime import datetime
startTime = datetime.now()

def dichotomie(f,a,b,N):
    '''
    Benaderde oplossing van f(x)=0 in het interval [a,b] door dichotomie (bisection method)
    Parameters
    ------------
    f:          Functie waar we de oplossing f(x)=0 voor zoeken.
    a,b:        Het interval waarvoor we een oplossing zoeken. 
                De functie return None als f(a)*f(b) >= 0 , want dan kan de oplossing fout zijn.
    N:          Het aantal iteraties dat we gaan doen.

    Returns
    ------------
    x_N:        Het middelpunt van het N-de interval berekend door dichotomie.
                Het initiele interval [a_0,b_0] is gegeven door [a,b]. Als f(m_n) == 0 voor
                een middelpunt m_n = (a_n + b_n)/2, dan zal de functie deze geven.
                Als alle tekens van de waarden f(a_n), f(b_n) en f(m_n) hetzelfde zijn bij 
                een iteratie, zal de functie None returnen.
    '''
    if f(a)*f(b) >= 0:
        print("Bisection method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Bisection method fails.")
            return None
    return (a_n + b_n)/2

def errorBound(f,a,b,N,approx):
    error_bound = (b-a)/(2**(N+1))
    if abs( (1 + 5**0.5)/2 - approx) < error_bound:
        return True
    else:
        return False
    

#Example: Supergolden ratio
#p(x) = x^3 - x^2 - 1

f = lambda x: x**2 - x - 1
a = 1
b = 2
N = 25
approx = dichotomie(f,a,b,N)

print('Approx: {approx}'.format(approx = approx))

print('Is the absolute error less than the error bound? : {answer}'.format(answer = errorBound(f,a,b,N,approx)))

time = datetime.now() - startTime
print('Time: {time}'.format(time = time))

