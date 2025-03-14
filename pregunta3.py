import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Definir la variable simbólica
x = sp.symbols('x')

# Definir la función f(x)
f = (x**3 - 3*x**2 + 3*x - 1) / (x**2 - 2*x)

# (a) Calcular el dominio de la función
dominio = sp.calculus.util.function_range(f, x, domain=sp.S.Reals)
print(f"Dominio de la función: {dominio}")

# (b) Calcular las intersecciones con los ejes X y Y
interseccion_x = sp.solveset(f, x, domain=sp.S.Reals)
interseccion_y = f.subs(x, 0)
print(f"Intersección con el eje X: {interseccion_x}")
print(f"Intersección con el eje Y: {interseccion_y}")

# (c) Calcular las asíntotas verticales, horizontales y oblicuas
# Asíntotas verticales (donde el denominador se hace cero)
asintotas_verticales = sp.solveset(x**2 - 2*x, x, domain=sp.S.Reals)
# Asíntotas horizontales
limite_inf_pos = sp.limit(f, x, sp.oo)
limite_inf_neg = sp.limit(f, x, -sp.oo)
# Asíntotas oblicuas (si existen)
asintota_oblicua = sp.simplify(x**2 / (x**2 - 2*x) - 3*x / (x**2 - 2*x) + 3 / (x**2 - 2*x))

print(f"Asíntotas verticales en: {asintotas_verticales}")
print(f"Asíntotas horizontales: f(x) tiende a {limite_inf_pos} cuando x tiende a infinito.")
print(f"Asíntotas horizontales: f(x) tiende a {limite_inf_neg} cuando x tiende a menos infinito.")
print(f"Asíntota oblicua: {asintota_oblicua}")

# (d) Calcular la primera y segunda derivada de f(x)
f_primera = sp.diff(f, x)
f_segunda = sp.diff(f_primera, x)

# Simplificar las derivadas para una mejor visualización
f_primera_simplificada = sp.simplify(f_primera)
f_segunda_simplificada = sp.simplify(f_segunda)

print(f"Primera derivada simplificada: {f_primera_simplificada}")
print(f"Segunda derivada simplificada: {f_segunda_simplificada}")

# (e) Graficar f(x), f'(x) y f''(x)

# Convertir las funciones simplificadas a funciones de numpy
f_lambdified = sp.lambdify(x, f, 'numpy')
f_primera_lambdified_simplificada = sp.lambdify(x, f_primera_simplificada, 'numpy')
f_segunda_lambdified_simplificada = sp.lambdify(x, f_segunda_simplificada, 'numpy')

# Crear un rango de valores para x
x_vals = np.linspace(-10, 10, 400)

# Evaluar las funciones en esos valores
y_vals = f_lambdified(x_vals)
y_vals_primera_simplificada = f_primera_lambdified_simplificada(x_vals)
y_vals_segunda_simplificada = f_segunda_lambdified_simplificada(x_vals)

# Graficar la función f(x)
plt.figure()
plt.plot(x_vals, y_vals, label=r'$f(x)$')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.title('Gráfica de $f(x)$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()

# Graficar la derivada f'(x)
plt.figure()
plt.plot(x_vals, y_vals_primera_simplificada, label=r"$f'(x)$", color='r')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.title('Gráfica de $f\'(x)$')
plt.xlabel('x')
plt.ylabel('f\'(x)')
plt.grid(True)
plt.legend()
plt.show()

# Graficar la segunda derivada f''(x)
plt.figure()
plt.plot(x_vals, y_vals_segunda_simplificada, label=r"$f''(x)$", color='g')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.title('Gráfica de $f\'\'(x)$')
plt.xlabel('x')
plt.ylabel('f\'\'(x)')
plt.grid(True)
plt.legend()
plt.show()

# (f) Intervalos donde la función es creciente o decreciente

# Calcular los puntos críticos (donde f'(x) = 0)
puntos_criticos = sp.solveset(f_primera, x, domain=sp.S.Reals)
print(f"Puntos críticos (donde f'(x) = 0): {puntos_criticos}")

# Evaluar la segunda derivada en los puntos críticos para determinar la concavidad
intervalos_crecientes = sp.Interval.open(-sp.oo, 1 - sp.sqrt(3)) | sp.Interval.open(1 + sp.sqrt(3), sp.oo)
intervalos_decrecientes = sp.Interval.open(0, 1) | sp.Interval.open(1, 2) | sp.Interval.open(2, 1 + sp.sqrt(3)) | sp.Interval.open(1 - sp.sqrt(3), 0)

print(f"Intervalos donde la función es creciente: {intervalos_crecientes}")
print(f"Intervalos donde la función es decreciente: {intervalos_decrecientes}")
