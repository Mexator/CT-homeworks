syms t x(t) s X;
% Given equation
dx = diff(x,t);
d2x = diff(x,t,2);
equation = d2x == dx + 7*x + t + 3;
% Laplace transform
trans = laplace(equation,t,s);
% Substituting initial conditions
trans = subs(trans, [laplace(x,t,s), dx(0), x(0)], [X,4,3]);
% Solving for X
sol = solve(trans,X);
% Inverse Laplace transform
sol =  ilaplace(sol, s, t);
% Plotting the solution
fplot(sol, [0 10])