plot(sim1.time,sim1.data,sim2.time,sim2.data,'LineWidth',2);
hold on;
fplot(sol,'LineWidth',2);
axis([0 10 0 inf]);
legend('Simulink model 1','Simulink model 2',
        'Exact solution')