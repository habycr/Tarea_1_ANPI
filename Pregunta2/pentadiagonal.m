function A = pentadiagonal(m, a, b, c, d, e)
  % Validación de parámetros
  if m < 5 || floor(m) ~= m
    error('m must be a positive integer >= 5');
  endif

  % Validación de tamaños de vectores
  if length(a) ~= m
    error('Vector a must have size m');
  endif
  if length(b) ~= m-1 || length(c) ~= m-1
    error('Vectors b and c must have size m-1');
  endif
  if length(d) ~= m-2 || length(e) ~= m-2
    error('Vectors d and e must have size m-2');
  endif

  % Inicialización de matriz pentadiagonal
  A = zeros(m, m);

  % Completar diagonal principal con vector a
  for i = 1:m
    A(i,i) = a(i);
  endfor

  % Completar primera superdiagonal con vector c
  for i = 1:m-1
    A(i,i+1) = c(i);
  endfor

  % Completar segunda superdiagonal con vector e
  for i = 1:m-2
    A(i,i+2) = e(i);
  endfor

  % Completar primera subdiagonal con vector b
  for i = 2:m
    A(i,i-1) = b(i-1);
  endfor

  % Completar segunda subdiagonal con vector d
  for i = 3:m
    A(i,i-2) = d(i-2);
  endfor
endfunction
