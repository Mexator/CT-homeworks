syms s;
W1 = (s+3)/(s+1);
W2 = 1/(s+2);
W3 = 1/(s+0.1);
W4 = 1/(2*s+3);
expr = W1*W3*W2/(1+W2*W4);
result = simplifyFraction(expr,'Expand',true);