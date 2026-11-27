N = 50;
y = rand(N,1);
x = linspace(0,1,N);
y = y + sin(sqrt(t))';
%x = rand(N,1);
%x = linspace(0,2*pi,N)';



R = rand(N,N);
W = R'*R;
%w = rand(N,1);
%X = [ones(size(x)),sin(x),cos(x),sin(2*x),cos(2*x)];
%X = [ones(size(x,1),1) , x(:,1),x(:,2)];
X = zeros(numel(x),5);
%w = exp(-x);
w = exp(-x.^2);
for j=1:7
    X(:,j) = hermite(j-1,x(:));
endfor

sol = [X;X+1] \ [y;y+1];
%sol_2 = X'*W*X \ X'*W*y;
sol_3 = (X'*(w(:).*X)) \ X'*(w(:).*y);

hold on;
plot(x,y,'.','MarkerSize', 15);
p1 = plot(x,X*sol,'DisplayName', 'Unweighted solution');
%plot(x,X*sol_2);
p2 = plot(x,X*sol_3,'DisplayName', 'Weighted solution');
legend([p1,p2]);
%hold on;
%plot3(x(:,1),x(:,2), y,'.','MarkerSize',15);
%plot3(x(:,1),x(:,2),X*sol);
%plot3(x(:,1),x(:,2),X*sol_2);

%disp(hermite(0));
