% data = importdata('C:\Users\dixin\Documents\Code\height-distance\3d_data.csv');
data = readtable('monocular_data.xlsx');
% scatter3(data.s, data.d, data.h);

x = data.scale_y;
y = data.area;
% z = data.height;
z = data.real_distance;

surffit = fit([x,y],z,'poly23','normalize','on');
% surffit = fit([x,y],z,'lowess');
plot(surffit,[x,y],z);

% f = fit([s d],h,'lowess');
% plot(f,[s d],h);

