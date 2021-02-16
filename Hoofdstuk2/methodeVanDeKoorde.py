def koorde(f,a,b,N):
    '''
    Benaderde oplossing van f(x)=0 in het interval [a,b] met de methode van de koorde (secant method).

    Parameters
    ------------
    f:          Functie waar we de oplossing f(x)=0 voor zoeken.
    a,b:        Het interval waarvoor we een oplossing zoeken. 
                De functie return None als f(a)*f(b) >= 0 , want dan kan de oplossing fout zijn.
    N:          Het aantal iteraties dat we gaan doen.

    Returns
    ------------
    m_N:        x is het snijpunt van de koorde op het N-de interval
                    m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
                Het initiele interval [a_0,b_0] is gegeven door [a,b]. Als f(m_n) == 0
                for een snijpunt m_n dan geeft de functie deze oplossing.
                Als alle tekens van de waarden van f(a_n), f(b_n) en f(m_n) hetzelfde zijn
                in een van de iteraties, returnt deze None
    '''
    if f(a)*f(b) >= 0:
        print("Secant method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1, N+1):
        m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
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
            print("Secant method fails.")
            return None
    return a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))


#Example: Supergolden ratio
#p(x) = x^3 - x^2 - 1

p = lambda x: x**3 - x**2 - 1
approx = koorde(p,1,2,20) # [1,2]
print('Approx: {approx}'.format(approx = approx))

supergolden = (1 + ((29 + 3*93**0.5)/2)**(1/3) + ((29 - 3*93**0.5)/2)**(1/3))/3
print('Supergolden: {super}'.format(super = supergolden))

error = abs(approx - supergolden)
print('Error: {error}'.format(error = error))