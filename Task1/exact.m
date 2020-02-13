syms x(t);
equation = diff(x,t,2) == diff(x,t) + 7*x + t + 3;
% Adding conditions for given IVP
cond1 = x(0) == 3;
Dx=diff(x,t);
cond2 = Dx(0) == 4;
cond = [cond1,cond2];
% Using dsolve to obtain exact symbolic solution
sol = dsolve(equation,cond);
% Plotting solution
fplot(sol,[0 10]);