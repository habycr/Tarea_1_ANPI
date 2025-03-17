import math

# --------------------- FUNCIONES BASE ---------------------
_eps = 2.2204e-16

def div_t(a, b, tol=1e-8, max_iter=2500):
    if b == 0:
        raise ValueError("Division por cero")
    if b >= 100:
        return 0.0
    x0 = _eps**15 if b >= 80 else _eps**11 if b >=60 else _eps**8 if b >=40 else _eps**4 if b >=20 else _eps**2
    x = x0
    for _ in range(max_iter):
        x_new = x * (2 - b * x)
        if abs(x_new - x) < tol * abs(x_new):
            break
        x = x_new
    return a * x

def factorial(n):
    if n < 0:
        raise ValueError("Factorial negativo")
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

# --------------------- FUNCIONES TRASCENDENTES ---------------------
def exp_t(x, tol=1e-8, max_iter=2500):
    suma, term = 1.0, 1.0
    for n in range(1, max_iter):
        term = term * x * div_t(1, n)
        suma += term
        if abs(term) < tol:
            break
    return suma

def sin_t(x, tol=1e-8, max_iter=2500):
    suma, term = x, x
    x_cuad = x * x
    for n in range(1, max_iter):
        term = term * x_cuad * div_t(1, (2*n)*(2*n+1))
        suma += (-1)**n * term
        if abs(term) < tol:
            break
    return suma

def cos_t(x, tol=1e-8, max_iter=2500):
    suma, term = 1.0, 1.0
    x_cuad = x * x
    for n in range(1, max_iter):
        term = term * x_cuad * div_t(1, (2*n-1)*(2*n))
        suma += (-1)**n * term
        if abs(term) < tol:
            break
    return suma

def ln_t(x, tol=1e-8, max_iter=2500):
    if x <= 0:
        raise ValueError("ln_t: x debe ser positivo")
    z = div_t(x-1, x+1)
    suma, term = z, z
    z_cuad = z * z
    for n in range(1, max_iter):
        term = term * z_cuad
        suma += div_t(term, 2*n+1)
        if abs(term) < tol:
            break
    return 2 * suma

def atan_t(x, tol=1e-8, max_iter=2500):
    if abs(x) <= 1:
        suma, term = x, x
        x_cuad = x * x
        for n in range(1, max_iter):
            term = term * x_cuad
            suma += (-1)**n * div_t(term, 2*n+1)
            if abs(term) < tol:
                break
        return suma
    else:
        signo = 1 if x > 0 else -1
        suma = div_t(math.pi, 2) - div_t(1, abs(x))
        term = div_t(1, abs(x))
        x_inv_cuad = div_t(1, x*x)
        for n in range(1, max_iter):
            term = term * x_inv_cuad
            suma += (-1)**n * div_t(term, 2*n+1)
            if abs(term) < tol:
                break
        return signo * suma

def root_t(x, y, tol=1e-8, max_iter=2500):
    if y == int(y) and y > 0:
        if x < 0 and y % 2 == 0:
            raise ValueError("Raiz par de negativo")
        aprox = x / 2
        for _ in range(max_iter):
            aprox_new = div_t(1, y) * ((y-1)*aprox + div_t(x, aprox**(y-1)))
            if abs(aprox_new - aprox) < tol * abs(aprox_new):
                return aprox_new
            aprox = aprox_new
        return aprox
    else:
        return exp_t(div_t(ln_t(x), y))

# --------------------- FUNCIONES DERIVADAS ---------------------
def tan_t(x):
    return div_t(sin_t(x), cos_t(x))

def sinh_t(x):
    return div_t(exp_t(x) - exp_t(-x), 2)

def cosh_t(x):
    return div_t(exp_t(x) + exp_t(-x), 2)

def tanh_t(x):
    return div_t(sinh_t(x), cosh_t(x))

def sqrt_t(x):
    if x < 0:
        raise ValueError("sqrt_t: x no negativo")
    return root_t(x, 2)

def asin_t(x):
    if x < -1 or x > 1:
        raise ValueError("asin_t: dominio invalido")
    return div_t(math.pi, 2) - atan_t(div_t(x, sqrt_t(1 - x*x)))

def acos_t(x):
    if x < -1 or x > 1:
        raise ValueError("acos_t: dominio invalido")
    return div_t(math.pi, 2) - asin_t(x)

def log_t(x, base):
    return div_t(ln_t(x), ln_t(base))

def power_t(x, y):
    return exp_t(y * ln_t(x))

def sec_t(x):
    return div_t(1, cos_t(x))

def cot_t(x):
    return div_t(1, tan_t(x))

def csc_t(x):
    return div_t(1, sin_t(x))