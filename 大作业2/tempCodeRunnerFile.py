exact_str = "{0:." + str(x_mpq) + "f}"
    #print(exact_str)
    z1 = mpfr(z1, int(gmpy2.ceil(gmpy2.mul(gmpy2.log2(10), gmpy2.add(x_mpq, 4))))) 
    i = mpfr(i, int(gmpy2.ceil(gmpy2.mul(gmpy2.log2(10), gmpy2.add(x_mpq, 4)))))
    z_toprint = exact_str.format(z1)
    i_toprint = exact_str.format(i)
    print("(z, i) = (", z_toprint, ", ", i_toprint, ")")