t = (0:0.1:10)';
step(1,1,t);
hold on;
s=tf("s");
c = pid(3000,0,10000);
step(feedback(c*ss(sys),1),t);