% Script para resolver el sistema de ecuaciones Ax = h con matriz pentadiagonal

% Definir parámetros
m = 2500;

% Crear los vectores con los valores especificados
a = zeros(m, 1);
for i = 1:m
    a(i) = 2*i;
end

b = zeros(m-1, 1);
for i = 1:m-1
    b(i) = -(i + 1)/3;
end

c = zeros(m-1, 1);
for i = 1:m-1
    c(i) = i/3;
end

d = zeros(m-2, 1);
for i = 1:m-2
    d(i) = -(i + 2)/2;
end

e = zeros(m-2, 1);
for i = 1:m-2
    e(i) = i/2;
end

h = zeros(m, 1);
for i = 1:m
    h(i) = 2*i - 5;
end

% Generar la matriz pentadiagonal A
A = pentadiagonal(m, a, b, c, d, e);

% Resolver el sistema de ecuaciones
x = A\h;

% Calcular el error como ||Ax - h||₂
error_norm = norm(A*x - h, 2);

% Mostrar el error
fprintf('Error = ||Ax - h||₂ = %e\n', error_norm);
