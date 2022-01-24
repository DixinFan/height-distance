% data = importdata('C:\Users\dixin\Documents\Code\height-distance\3d_data.csv');
data = readtable('3d_data.csv');
% scatter3(data.s, data.d, data.h);

x = data.s;
y = data.d;
z = data.h;

surffit = fit([x,y],z,'poly23','normalize','on');
% surffit = fit([x,y],z,'lowess');
plot(surffit,[x,y],z);

% f = fit([s d],h,'lowess');
% plot(f,[s d],h);

