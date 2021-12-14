from tqdm import tqdm
import gmpy2
from gmpy2 import mpq
from gmpy2 import mpz
from gmpy2 import mpfr

from problem1 import calw0z

def caln(t, x):
    t2 = gmpy2.square(t) # t^2
    t4 = gmpy2.square(t2) # t^4
    t5 = gmpy2.mul(t4, t) # t^5
    t6 = gmpy2.mul(t4, t2) # t^6
    a0 = gmpy2.div(t5, mpz(720)) # t^5 / 720
    a1 = mpz(24)
    a_temp = gmpy2.mul(156, t2)
    a1 = gmpy2.add(a1, a_temp)
    a_temp = gmpy2.mul(112, t4)
    a1 = gmpy2.add(a1, a_temp)
    a_temp = gmpy2.mul(16, t6)
    a1 = gmpy2.add(a1, a_temp)
    a2 = gmpy2.exp(t2)
    a3 = gmpy2.exp10(x) 
    a = gmpy2.mul(a0, a1)
    a = gmpy2.mul(a, a2)
    a = gmpy2.mul(a, a3) # n^4
    a = gmpy2.sqrt(a)
    a = gmpy2.sqrt(a) #n
    n = gmpy2.ceil(a)
    n = mpz(n)
    return n

def calm(t, x, n):
    t2 = gmpy2.square(t)
    t4 = gmpy2.square(t2)
    a1 = gmpy2.mul(mpq(3.5), t2)
    a2 = gmpy2.mul(mpq(7, 3), t4)
    a3 = gmpy2.exp(t2)
    a4 = gmpy2.exp10(x)
    a4 = gmpy2.mul(2, a4)
    a = gmpy2.add(a1, a2)
    a = gmpy2.add(a, gmpy2.mul(2, n))
    a = gmpy2.mul(a, a3)
    a = gmpy2.mul(a, a4)
    m = mpz(gmpy2.ceil(gmpy2.log10(a)))
    return m
    
def cali1(t, n):
    h = mpq(gmpy2.div(t, n))
    #print("h", h)
    a1 = mpq(0)
    for i  in range(1, int(n)):
        tk = gmpy2.mul(i, h)
        tk2 = gmpy2.square(tk)
        etk2 = gmpy2.exp(tk2)
        a1k = gmpy2.mul(tk2, etk2)
        a1k = gmpy2.mul(2, a1k)
        a1 = gmpy2.add(a1, a1k)
    a2 = mpq(0)
    for i in range(int(n)):
        tkh = gmpy2.add(gmpy2.mul(i, h), gmpy2.div(h, 2))
        tkh2 = gmpy2.square(tkh)
        etkh2 = gmpy2.exp(tkh2)
        a2k = gmpy2.mul(4, gmpy2.mul(tkh2, etkh2))
        a2 = gmpy2.add(a2, a2k)
    t2 = gmpy2.square(t)
    a3 = gmpy2.mul(t2, gmpy2.exp(t2))
    #print("A3", a3)
    a = gmpy2.add(a1, gmpy2.add(a2, a3))
    i1 = gmpy2.mul(gmpy2.div(h, 6), a)
    return i1


if __name__ == "__main__":
    '''get the z and x'''
    a = input("a = ")
    x = input("Precision[int]:")
    x_mpq = mpz(x)
    x_minus_mpq = mpz("-" + x)
    a_mpq =  mpq(a)
    #if_tqdm = input("use tqdm[y/n]:")
    if_tqdm = 'n'

    '''rough calculate'''
    z0, w0 = calw0z(a_mpq, 4, "n")
    t0 = gmpy2.sqrt(w0)

    '''calculate n'''
    n = caln(t0, x_mpq)
    print("n = ", n)

    '''calculate m'''
    m = calm(t0, x_mpq, n)
    print("m = ", m)
    gmpy2.local_context(gmpy2.context(), precision=int(gmpy2.ceil(gmpy2.mul(gmpy2.log2(10), m))))

    '''recalculate t'''
    z1, w1 = calw0z(a_mpq, m, "n")
    #t1 = mpq(0.75308926)
    t1 = gmpy2.sqrt(w1)
    #print(type(t1))
    exact_str = "{0:." + str(int(m + 1)) + "f}"
    t_str = exact_str.format(t1)
    t1 = mpq(t_str)
    #print("z1 = ", z1)

    '''calculate integral'''
    i1 = cali1(t1, n)
    #print(type(i1))
    i = gmpy2.sub(gmpy2.mul(a_mpq, t1), i1)
    #print(type(i))

    '''print result'''
    exact_str = "{0:." + str(x_mpq) + "f}"
    #print(exact_str)
    z1 = mpfr(z1, int(gmpy2.ceil(gmpy2.mul(gmpy2.log2(10), gmpy2.add(x_mpq, 4))))) 
    i = mpfr(i, int(gmpy2.ceil(gmpy2.mul(gmpy2.log2(10), gmpy2.add(x_mpq, 4)))))
    z_toprint = exact_str.format(z1)
    i_toprint = exact_str.format(i)
    print("(z, i) = (", z_toprint, ", ", i_toprint, ")")


    