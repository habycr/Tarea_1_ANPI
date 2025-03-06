import math
from Pregunta1 import *

def test():
    # Evaluando la expresión: 0.8610377433 * cos(3) + ln(2) + sinh(sqrt(2)) + atan(exp(-1))
    result = div_t(0.8610377433, 1) * cos_t(3) + ln_t(2) + sinh_t(sqrt_t(2)) + atan_t(exp_t(-1))
    print(f"Resultado: {result}")

test()
