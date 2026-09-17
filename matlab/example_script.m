f = @(x,y) y;
g = @(x,y) -x -y;

[X, Y] = meshgrid(-3:0.3:3, -3:0.3:3);
DX = f(X, Y);
DY = g(X, Y);

L = hypot(DX, DY);
L(L==0) = 1;
DX = DX ./ L;
DY = DY ./ L;

figure;
quiver(X, Y, DX, DY, 0.5, 'k');
hold on;
grid on;
xlabel('x'); ylabel('y');
title('Vector Field u1 = y, u2 = -x -y');

sol = @(t, z) [f(z(1), z(2)); g(z(1),z(2))];
tspan = [0 10];

initial_conditions = [-1 1; 1, 1; -1, -1; 2, -2];
for k= 1:rows(initial_conditions);
  [t, z] = ode45(sol, tspan, initial_conditions(k, :));
  plot(z(:,1), z(:,2), 'LineWidth',1);
  plot(z(1,1), z(1,2),'ro', 'MarkerFaceColor','r')
end


print -djpg ../fields/matlab_example_fig.jpg;
hold off;

