function [A,A_prime] = poly_design (data,poly_name,deg)
data = data(:);
N_elem = numel(data);
t = (1:N_elem)';
x = 2*(t - t(1))/(t(end)-t(1)) -1;
A = zeros(N_elem,deg);
A_prime = zeros(N_elem,deg);
switch lower(poly_name)
    case 'hermite'
        basisfun = @(n, x) hermite(n, x);
    case 'laguerre'
        t0 = t(1);
        tf = t(end);
        x = (t - t0) / (tf - t0);
        basisfun = @(n, x) laguerre(n,x);
    case 'chebyshev'
        basisfun = @(n, x) chebyshev(n,x);
 %       basisfun_prime = @(n,x) chebyshev_prime(n,x);
    otherwise
        error('Unsupported poly_name: %s', poly_name);
end
for i=1:deg
    A(:,i) = basisfun(i-1,x);
%    A_prime(:,i) = basisfun_prime(i-1,x);
end
end
