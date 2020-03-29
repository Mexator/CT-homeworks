A = [2,1;-3,1];
B = [-1,5;3,1]; 
C = [-2,0]; 
D = [2,4];
% This system has 2 inputs, then, there will be 2
% transfer functions  
[nom,denom]=ss2tf(A,B,C,D,1)
ans1 = tf(nom,denom);
% ans1 =
% 2 s^2 - 4 s + 2
% ---------------
%  s^2 - 3 s + 5
[nom,denom]=ss2tf(A,B,C,D,2)
ans2 = tf(nom,denom);
% ans2 =
% 4 s^2 - 22 s + 28
% -----------------
%   s^2 - 3 s + 5