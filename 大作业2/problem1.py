import gmpy2
from gmpy2 import mpq
from gmpy2 import mpz

'''get the z and x'''
z_exp = input("z = ")
x = input("Exact to:")
x_mpq = mpz(x)
z_exp_mpq =  mpq(z_exp)
#print(z_exp_mpq)

'''Calculate n'''
n = mpq(1)
n_times = 200
#1.75 * 
a = gmpy2.sub(gmpy2.exp(gmpy2.mul(2, z_exp_mpq)), 1)
b = gmpy2.div(gmpy2.square(z_exp_mpq), gmpy2.mul(2, gmpy2.square(n)))
ab = gmpy2.mul(a, b)
round_err_pre = gmpy2.mul(1.75, ab)
while()
'''Calculate m'''

'''iter to cal w(z_exp)'''