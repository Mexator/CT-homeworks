% X dot derivative
syms z_2 z_4 u
M = 15.1; 
m = 1.2;
l = 0.35;
g = 9.81;
expr = ((-m*l*sin(z_2)*z_4^2) + m*g*sin(z_2)*cos(z_2))/((M+m) - m*cos(z_2)^2) + u/((M+m)-m*cos(z_2)^2);
subs(expr);
% Theta dot derivative

int1 = diff(expr,z_2);
int2 = diff(expr,z_4);
int3 = diff(expr,u);

z_2=0;
z_4=0;
u=0;

subs(int1)
subs(int2)
subs(int3)

syms z_2 z_4 u

expr2 = ((M+m)*g*sin(z_2) - m*l*cos(z_2)*sin(z_2)*z_4^2)/(l*((M+m)-m*cos(z_2)^2)) + u*cos(z_2)/((M+m)-m*cos(z_2)^2);
subs(expr2);

int4 = diff(expr2,z_2);
int5 = diff(expr2,z_4);
int6 = diff(expr2,u);

z_2=0;
z_4=0;
u=0;

subs(int4)
subs(int5)
subs(int6)