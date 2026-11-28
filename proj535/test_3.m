N = 100;
n_basis =3;
x = randn(N,2);
xmin = min(x, [], 1);
xmax = max(x, [], 1);

x_scaled = 2 .* (x - xmin) ./ (xmax - xmin) - 1;
t_1 = linspace(min(x(:,1)),max(x(:,1)),N/2);
t_2 = linspace(min(x(:,2)),max(x(:,2)),N/2);
t1_scaled = 2 .* (t_1 - xmin(1)) ./ (xmax(1) - xmin(1)) - 1;
t2_scaled = 2 .* (t_2 - xmin(2)) ./ (xmax(2) - xmin(2)) - 1;
x = x_scaled;
[U, V] = meshgrid(t1_scaled, t2_scaled);
%[U,V] = meshgrid(t_1,t_2);
y = sin(5*x(:,1))+x(:,2).^2+randn(N,1);

X_1 = zeros(N,n_basis);
X_2 = zeros(N,n_basis);
H1 = zeros(numel(U),n_basis);
H2 = zeros(numel(V),n_basis);
for j=1:n_basis
  X_1(:,j) = legendr(j-1,x(:,1));
  X_2(:,j) = legendr(j-1,x(:,2));
  H1(:,j) = legendr(j-1,U(:));
  H2(:,j) = legendr(j-1,V(:));
endfor
X = [X_1,X_2(:,2:end)];
sol = X\ y;

z = H1*sol(1:n_basis) + H2(:,2:n_basis)*sol(n_basis+1:end);
scatter3(x(:,1),x(:,2),y,'.');
zlabel("y");
hold on;
%surf(t1_scaled,t2_scaled,reshape(z,size(U)));
tprod = zeros(N,n_basis*2);

for i=1:n_basis
  for j=1:n_basis
    col = n_basis*(i-1) + j;
    tprod(:,col) = X_1(:,i).*X_2(:,j);
  endfor
endfor

sol_2 = tprod \ y;

z_2 = zeros(numel(U), n_basis);

for i = 1:n_basis
  for j = 1:n_basis
    col = (i-1)*n_basis + j;
    z_2(:,col) = H1(:,i) .* H2(:,j);
  endfor
endfor


Z = reshape(z_2 * sol_2, size(U));
scatter3(x(:,1),x(:,2),y,100);
zlabel("y");
hold on;
surf(t1_scaled, t2_scaled, Z);


