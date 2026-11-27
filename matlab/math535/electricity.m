S = csvread('data/leleccum.csv');
data = S;
len = size(data);
num_basis = 5;
poly_name= 'laguerre';

switch lower(poly_name)
    case 'hermite'
        basisfun = @(n, x) hermite(n, x);
    case 'laguerre'
        basisfun = @(n, x) laguerre(n,x);
    otherwise
        error('Unsupported poly_name: %s', poly_name);
end
%num_samples = size(data,2)/2^N;
%num_pieces = floor(numel(data) / num_samples);
%data_sample = data(1:num_pieces*num_samples);
%pieces = reshape(data_sample,num_samples,num_pieces);

%num_basis = 3;
%sols = zeros(num_basis,num_pieces);
%yfit = zeros(num_samples,num_pieces);
%for j=1:num_pieces
%    y = pieces(:,j);
%    t = linspace(0,num_samples-1,num_samples);
%    X = zeros(num_samples,num_basis);
%    for i=1:num_basis
%    X(:,i) = laguerre(i-1,t);
%    end
%    sol = X \ y;
%    sols(:,j) = sol;
%    yfit(:,j) = X*sol;
%end

%ylong = reshape(yfit,1,num_samples*num_pieces);

%error = mse(ylong,data);

fig = figure('visible','off');
set(fig, 'PaperUnits', 'inches', 'PaperPosition', [0 0 10 12]);
for N=1:5
    num_samples = size(data,1)/2^N;
    num_pieces = floor(numel(data) / num_samples);
    data_sample = data(1:num_pieces*num_samples);
    pieces = reshape(data_sample,num_samples,num_pieces);
    sols = zeros(num_basis,num_pieces);
    yfit = zeros(num_samples,num_pieces);
    rs = zeros(num_pieces,1);
    t = linspace(0,num_samples-1,num_samples);
    X = zeros(num_samples,num_basis);
    for i=1:num_basis
        X(:,i) = basisfun(i-1,t);
    end
    for j=1:num_pieces
        y = pieces(:,j);
        sol = X \ y;
        sols(:,j) = sol;
        yfit(:,j) = X*sol;
        rs(j) = rsquare(X*sol,y);
    end

    ylong = reshape(yfit,1,num_samples*num_pieces);

    subplot(5,1,N);
    hold on;
    p1 = plot(ylong,'DisplayName',sprintf(['' ...
        'window size %d \n'],N));
    p2 =plot(data,'DisplayName','Data');
    legend([p1,p2]);
endfor
title(sprintf('%s approximate order %d',poly_name,num_basis));
print(fig, sprintf('figures/%s_fit_result.png',poly_name),'-dpng','-r300');


