A_s = [0 0 0 0; 0 0 0.7796 30.256; 1 0 0 0; 0 1 0 0]
C_s = [1 0; 0 1; 0 0; 0 0]

contr = ctrb(A_s, C_s)
rank(contr)