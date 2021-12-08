from tqdm import tqdm
import gmpy2
from gmpy2 import mpq
from gmpy2 import mpz
from gmpy2 import mpfr

def method_error(n, z):
    '''n = iters, z = z*'''
    a = gmpy2.sub(gmpy2.exp(gmpy2.mul(mpz(1), z)), mpz(1))
    b = gmpy2.div(gmpy2.square(z), gmpy2.square(n))
    ab = gmpy2.mul(a, b)
    method_err = gmpy2.mul(mpq(1.25), ab)
    return method_err

def round_error(n, z, x):
    '''n = iters, z = z*, x = x*'''
    a = gmpy2.sub(gmpy2.exp(gmpy2.mul(mpz(1), z)), mpz(1))
    b = gmpy2.mul(gmpy2.div(n, z), gmpy2.exp10(x))
    ab = gmpy2.mul(a, b)
    round_err = gmpy2.mul(mpz(2), ab)
    return round_err

def f(z, w):
    return gmpy2.div(1, gmpy2.add(z, gmpy2.exp(w)))

def calw0z(z_exp_mpq, x_mpq, if_tqdm):
    '''Calculate n'''
    method_err_exp = gmpy2.mul(mpq(0.25), gmpy2.exp10(gmpy2.mul(x_mpq, mpz(-1))))
    a = gmpy2.mul(gmpy2.sub(gmpy2.exp(z_exp_mpq), mpz(1)), gmpy2.square(z_exp_mpq))
    method_err = gmpy2.div(gmpy2.mul(mpq(1.25), a), method_err_exp)
    n = gmpy2.ceil(gmpy2.sqrt(method_err))
    h = gmpy2.div(z_exp_mpq, n)
    print("n = ", n)
    print("h = ", h)
    '''Calculate m'''
    m = mpz(1)
    round_err_exp = round_error(n, z_exp_mpq, x_mpq)
    while(round_err_exp > gmpy2.exp10(m)):
        m = gmpy2.add(m, mpz(1))
    print("m(10) = ", m)
    '''set precision'''
    gmpy2.local_context(gmpy2.context(), precision=int(gmpy2.ceil(gmpy2.mul(gmpy2.log2(10), m))))
    print("m(2) = ", int(gmpy2.ceil(gmpy2.mul(gmpy2.log2(10), m))))

    '''iter to calculate w(z_exp)'''
    w = mpfr(0)
    w_bar = mpfr(0)
    z = mpfr(0)
    if if_tqdm == 'y':
        for i in tqdm(range(int(n))):
            w_bar = gmpy2.add(w, gmpy2.mul(h, f(z, w)))
            w_next = gmpy2.add(w, gmpy2.mul(gmpy2.div(h, 2), gmpy2.add(f(z, w), f(gmpy2.add(z, h), w_bar))))
            z = gmpy2.add(z, h)
            w = w_next
            #if i % 1000 == 0: print(w)
    else:
        for i in range(int(n)):
            w_bar = gmpy2.add(w, gmpy2.mul(h, f(z, w)))
            w_next = gmpy2.add(w, gmpy2.mul(gmpy2.div(h, 2), gmpy2.add(f(z, w), f(gmpy2.add(z, h), w_bar))))
            z = gmpy2.add(z, h)
            w = w_next

    
    return z, w


if __name__ == "__main__":
    '''get the z and x'''
    z_exp = input("z = ")
    x = input("Precision[int]:")
    x_mpq = mpz(x)
    z_exp_mpq =  mpq(z_exp)
    if_tqdm = input("use tqdm[y/n]:")
    
    z, w = calw0z(z_exp_mpq, x_mpq, if_tqdm)

    '''print answer'''
    exact_str = "{0:." + str(x) + "f}"
    #print(exact_str)
    z_toprint = exact_str.format(z)
    w_toprint = exact_str.format(w)
    print("(z, w) = (", z_toprint, ", ", w_toprint, ")")