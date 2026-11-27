data = csvread('data/leleccum.csv');
%periodogram(data);
var(data);
poly_name = 'laguerre';
factor = 3;
t = linspace(1,numel(data),numel(data))';
ts = t(1:factor:end);
segment = floor(numel(data)/factor);
datadc = data - mean(data);
tday = reshape(t,segment,factor);
dataday = reshape(datadc,segment,factor);
data_s = data(1:factor:end);
%plot(norm_data);
%X = [ones(numel(data),1), t'];
%hold on;
%plot(t,data);
%for deg=1:9
%    P = poly_design(data,'laguerre',deg);
%    c = P \ data;
%    yfit = P*c;
%    plot(t,yfit);
%end
%fig = figure();
%colors = lines(3);
%hold on;
%for i=1:3
%    plot(tday(:,i),dataday(:,i),'Color',colors(i,:));
%end
%hold off;
%close fig;

%fig = figure();
%for i=1:3
%subplot(3,1,i)
%x = dataday(:,i);
%transform = fftshift(fft(x));
%N = numel(x);
%f = (-N/2:N/2 -1) / N
%hold on;
%plot(f,log(abs(transform)+eps));
%title(sprintf("day %d",i));
%end

T = fft(dataday);
phases = imag(T);
L = log(abs(T)+eps);
hold on;
subplot(2,1,1)
plot(L);
lam = 10;
L(L>lam)=lam;
subplot(2,1,2)
plot(L);
title(sprintf('Hard Thresholded lam = %d',lam));
hold off;
datahard = real(ifft(exp(L).*exp(1i*phases)))+mean(data);
threshold = 1;
if threshold
  data = datahard;
else
  data = dataday;
endif

fig = figure('visible','off');
set(fig, 'PaperUnits', 'inches', 'PaperPosition', [0 0 10 12]);
colors = lines(3);
order = 7;
hold on;
for i=1:3
    plot(tday(:,i),data(:,i),'Color',colors(i,:));
    [A_1,~] = poly_design(tday(:,i),'laguerre',order);
    c_1 = A_1 \ data(:,i);
    yfit = A_1*c_1;
    plot(tday(:,i),yfit,'LineWidth',1.2);
end
title(sprintf("Piecewise-fit %s order %d Thresholded Data: %d",poly_name,order,threshold));
print(fig, sprintf('figures/piecewise_%s_%d_%d.png',poly_name,order,threshold),'-dpng','-r300');
