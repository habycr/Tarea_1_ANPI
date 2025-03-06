import math

# div_t(x) - Aproximación de la división
def div_t(a, b, tol=1e-8, max_iter=2500):
    if b == 0:
        raise ValueError("División por cero no permitida")
    x = 1.0
    for _ in range(max_iter):
        x *= (2 - b * x)
        if abs(1 - b * x) < tol:
            break
    return a * x

# sin_t(x) - Aproximación de la función seno
def sin_t(x, tol=1e-8, max_iter=2500):
    sum_val, term, sign = x, x, -1
    for n in range(1, max_iter):
        term *= x * x * div_t(1, (2 * n) * (2 * n + 1))
        sum_val += sign * term
        sign *= -1
        if abs(term) < tol:
            break
    return sum_val

# exp_t(x) - Aproximación de la función exponencial
def exp_t(x, tol=1e-8, max_iter=2500):
    sum_val, term = 1, 1
    for n in range(1, max_iter):
        term *= x * div_t(1, n)
        sum_val += term
        if abs(term) < tol:
            break
    return sum_val



# cos_t(x) - Aproximación de la función coseno
def cos_t(x, tol=1e-8, max_iter=2500):
    sum_val, term, sign = 1, 1, 1
    for n in range(1, max_iter):
        term *= div_t(x * x, (2 * n - 1) * (2 * n))
        sum_val += sign * term
        sign *= -1
        if abs(term) < tol:
            break
    return sum_val

# tan_t(x) - Aproximación de la función tangente
def tan_t(x):
    return div_t(sin_t(x), cos_t(x))

# ln_t(x) - Aproximación del logaritmo natural
def ln_t(x, tol=1e-8, max_iter=2500):
    if x <= 0:
        raise ValueError("ln_t(x) solo está definido para x > 0")
    y = div_t(x - 1, x + 1)
    sum_val, term = 0, y
    for n in range(max_iter):
        sum_val += div_t(term, 2 * n + 1)
        term *= y * y
        if abs(term) < tol:
            break
    return 2 * sum_val

# log_t(x, y) - Aproximación del logaritmo en base y
def log_t(x, y):
    return div_t(ln_t(x), ln_t(y))

# power_t(x, y) - Aproximación de x elevado a y
def power_t(x, y):
    return exp_t(y * ln_t(x))

# sinh_t(x) - Aproximación de la función seno hiperbólico
def sinh_t(x):
    return div_t(exp_t(x) - exp_t(-x), 2)

# cosh_t(x) - Aproximación de la función coseno hiperbólico
def cosh_t(x):
    return div_t(exp_t(x) + exp_t(-x), 2)

# tanh_t(x) - Aproximación de la función tangente hiperbólica
def tanh_t(x):
    return div_t(sinh_t(x), cosh_t(x))

# sqrt_t(x) - Aproximación de la raíz cuadrada
def sqrt_t(x):
    if x < 0:
        raise ValueError("sqrt_t(x) solo está definido para x >= 0")
    return power_t(x, 0.5)

# root_t(x, y) - Aproximación de la raíz y-ésima de x
def root_t(x, y):
    return power_t(x, div_t(1, y))

# asin_t(x) - Aproximación de la función arco seno
def asin_t(x, tol=1e-8, max_iter=2500):
    if x < -1 or x > 1:
        raise ValueError("asin_t(x) está definido para -1 <= x <= 1")
    sum_val, term, sign = x, x, 1
    for n in range(1, max_iter):
        term *= div_t(x * x, (2 * n) * (2 * n + 1))
        sum_val += sign * term
        sign *= -1
        if abs(term) < tol:
            break
    return sum_val

# atan_t(x) - Aproximación de la función arco tangente
def atan_t(x, tol=1e-8, max_iter=2500):
    sum_val, term, sign = x, x, -1
    for n in range(1, max_iter):
        term *= div_t(x * x, (2 * n + 1))
        sum_val += sign * term
        sign *= -1
        if abs(term) < tol:
            break
    return sum_val

# acos_t(x) - Aproximación de la función arco coseno
def acos_t(x):
    return div_t(math.pi, 2) - asin_t(x)

# sec_t(x) - Aproximación de la función secante
def sec_t(x):
    return div_t(1, cos_t(x))

# cot_t(x) - Aproximación de la función cotangente
def cot_t(x):
    return div_t(1, tan_t(x))

# csc_t(x) - Aproximación de la función cosecante
def csc_t(x):
    return div_t(1, sin_t(x))

# factorial(n) - Aproximación del factorial de n
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result








