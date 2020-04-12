A = [0 0 1 0; 0 0 0 1; 0 23.66 0 0; 0 37.6 0 0];
B = [0; 0; .294; .294];
C = [1 0 0 0];
D = [0];
% Simulate the sysstem and view Root-Locus plot
open_loop = ss(A,B,C,D);
rlocus(open_loop);
% Compensator 1 - to eliminate pole in right half-plane
comp1 = tf([1 -6.1319],[1]);
stab1 = minreal(open_loop*comp1);
rlocus(stab1);
% Compensator 2 - to eliminate poles in origin, and 
% add pole in left half-plane, because number of poles 
% and zeroes should be the same
comp2 = tf([1 0 0],[1 15 50]);
stab2 = minreal(stab1*comp2);
rlocus(stab2);
step(stab2)