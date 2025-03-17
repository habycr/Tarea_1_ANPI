from Pregunta1 import *

def test():
    # Calcular cos(3/7)
    cos_val = cos_t(3/7)
    # Calcular ln(2)
    ln_val = ln_t(2)
    # Sumar y obtener raíz cúbica
    sum_inside = cos_val + ln_val
    root_val = root_t(sum_inside, 3)
    # Calcular arctan(e^-1)
    exp_val = exp_t(-1)
    atan_val = atan_t(exp_val)
    # Sumar resultados
    result = root_val + atan_val
    print(f"Resultado: {result}")

test()