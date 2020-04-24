syms z_2 z_4 u
% X dot derivative
expr = (- 7.298 * sin(z_2)*(z_4)^2 + 80.442*sin(z_2)*cos(z_2))/(11.6 - 8.2*cos(z_2)^2) +   u/(11.6 - 8.2*cos(z_2)^2);
int1 = diff(expr,z_2);
int2 = diff(expr,z_4);
int3 = diff(expr,u);
z_2=0;
z_4=0;
u=0;
subs(int1)
subs(int2)
subs(int3)

expr = (113.796 * sin(z_2) - 7.298 * sin(z_2)*(z_4)^2)/(10.324 - 7.298*cos(z_2)^2) + cos(z_2) * u/(11.6 - 8.2*cos(z_2)^2);
int1 = diff(expr,z_2);
int2 = diff(expr,z_4);
int3 = diff(expr,u);
z_2=0;
z_4=0;
u=0;
subs(int1)
subs(int2)
subs(int3)