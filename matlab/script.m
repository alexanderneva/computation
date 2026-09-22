t = y = linspace(-7,7,50);

[tt,yy] = meshgrid (t,y);

%tz = vectorField(tt,yy);
fs = 't*sin(y.^2)'
gs = 't.^2 + y'
f = @(t,y) [eval(fs)];
g = @(t,y) [eval(gs)];

dx = f(tt,yy);
dy = g(tt,yy);

L = hypot(dx, dy);
L(L==0) = 1;
dx = dx ./ L;
dy = dy ./ L;

figure;
quiver (tt,yy,dx,dy, 1, 'k');
hold on;
grid on;
xlabel('t'); ylabel('y');
title(strcat('Vector Field u1 =',fs,' u2 = ',gs));

sol = @(t, z) [f(z(1), z(2)); g(z(1),z(2))];
tspan = [0 1.5];

initial_conditions = [-1 1; 1, 1; -1, -1; 2, -2; 0, -2; 0, -1; -0.25, -1];
for k= 1:rows(initial_conditions);
  [t, z] = ode45(sol, tspan, initial_conditions(k, :));
  plot(z(:,1), z(:,2), 'LineWidth',1);
  plot(z(1,1), z(1,2),'ro', 'MarkerFaceColor','r');
end

print -djpg ../fields/matlab_figure.jpg;
hold off;


% Lutka-volterra
t = y = linspace(0,7,50);

[tt,yy] = meshgrid (t,y);

%tz = vectorField(tt,yy);
fs = 't*(y-2)'
gs = 'y*(1-t)'
f = @(t,y) [eval(fs)];
g = @(t,y) [eval(gs)];

dx = f(tt,yy);
dy = g(tt,yy);

L = hypot(dx, dy);
L(L==0) = 1;
dx = dx ./ L;
dy = dy ./ L;

figure;
quiver (tt,yy,dx,dy, 1, 'k');
hold on;
grid on;
xlabel('t'); ylabel('y');
title(strcat('Vector Field u1 =',fs,' u2 = ',gs));

sol = @(t, z) [f(z(1), z(2)); g(z(1),z(2))];
tspan = [0 3];

initial_conditions = [0.25 1; 0.5, 1; 1, 1; 1, 0.25; 0, 0.25; 0, 0.5; 1, 2];
for k= 1:rows(initial_conditions);
  [t, z] = ode45(sol, tspan, initial_conditions(k, :));
  plot(z(:,1), z(:,2), 'LineWidth',1);
  plot(z(1,1), z(1,2),'ro', 'MarkerFaceColor','r');
end

print -djpg ../fields/matlab_figure_lutka.jpg;
hold off;
%f_2 = @(t,y) [1 - t.^2 - y.^2];
%
%z = f_2 (tt, yy);
%quiver (tt,yy,tt,z);
%title("1 - t^2 - y^2")
%print -djpg ../fields/matlab_figure2.jpg;
%
%f_3 = @(t,y) [sin(t)-cos(y)];
%
%z = f_3 (tt, yy);
%
%quiver(tt,yy,tt,z);
%title("sin(t)-cos(y)");
%print -djpg ../fields/matlab_figure3.jpg;
%
%f_4 = @(t,y) [t.^2 + y.^2];
%
%z = f_4 (tt,yy);
%h = quiver(tt,yy,tt,z);
%set(h, "maxheadsize", 0.25);
%title(" x^2 + y^2")
%print -djpg ../fields/matlab_figure4.jpg
