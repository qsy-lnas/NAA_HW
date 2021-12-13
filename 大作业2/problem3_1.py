from tqdm import tqdm
import gmpy2
from gmpy2 import mpq
from gmpy2 import mpz
from gmpy2 import mpfr

from problem1 import calw0z


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

    '''calculate error range'''
    w0 = gmpy2.ceil(w0)
    method_err = gmpy2.div(gmpy2.mul(mpq(0.5), gmpy2.exp10(x_minus_mpq)), gmpy2.mul(gmpy2.exp(w0), gmpy2.add(gmpy2.square(w0), w0)))
    x_acc = mpz(gmpy2.ceil(gmpy2.log10(gmpy2.mul(2, method_err))))
    x_acc = gmpy2.mul(-1, x_acc)
    
    '''precision calculate'''
    z1, w1 = calw0z(a_mpq, x_acc, if_tqdm)



    '''calculate integral'''
    i = gmpy2.sub(gmpy2.mul(gmpy2.exp(w1), gmpy2.add(gmpy2.sub(gmpy2.square(w1), w1), 1)), 1)


    '''print answer'''
    exact_str = "{0:." + str(x) + "f}"
    #print(exact_str)
    z1 = mpfr(z1, int(gmpy2.ceil(gmpy2.mul(gmpy2.log2(10), gmpy2.add(x_mpq, 4))))) 
    i = mpfr(i, int(gmpy2.ceil(gmpy2.mul(gmpy2.log2(10), gmpy2.add(x_mpq, 4)))))
    z_toprint = exact_str.format(z1)
    i_toprint = exact_str.format(i)
    print("(z, i) = (", z_toprint, ", ", i_toprint, ")")
    