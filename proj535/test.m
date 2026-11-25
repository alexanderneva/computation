N = 50
y = rand(N,1);
t = linspace(0,4*pi,N);
y = y + sin(t)';
x = rand(N,1);
x = linspace(0,2*pi,N)';



R = rand(N,N);
W = R'*R;
w = rand(N,1);
X = [ones(size(x)),sin(x),cos(x),sin(2*x),cos(2*x)];
%X = [ones(size(x,1),1) , x(:,1),x(:,2)];

sol = X \ y;
sol_2 = X'*W*X \ X'*W*y;
sol_3 = (X'*(w.*X)) \ X'*(w.*y);

hold on;
plot(x,y,'.','MarkerSize', 15);
plot(x,X*sol);
plot(x,X*sol_2);
plot(x,X*sol_3);

%hold on;
%plot3(x(:,1),x(:,2), y,'.','MarkerSize',15);
%plot3(x(:,1),x(:,2),X*sol);
%plot3(x(:,1),x(:,2),X*sol_2);
