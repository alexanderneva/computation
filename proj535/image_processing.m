im = imread('misc/house.tiff');
gr = rgb2gray(im);
gr_scaled = double(gr)/255.;
%fig = figure();
%subplot(2,2,1);
%imshow(im);
%subplot(2,2,2);
%imshow(gr);

f = [0,1,0;1,-4,1;0,1,0];

%subplot(2,2,3);
%imshow(conv2(gr,f));




n_basis = 15;
%% global fit
N = size(gr,1);
X_1 = zeros(N,n_basis);
X_2 = zeros(N,n_basis);
x = linspace(0,1,N);
y = linspace(0,1,N);
tprod = zeros(N,n_basis^2);
for j=1:n_basis
  X_1(:,j) = chebyshev(j-1,x);
  X_2(:,j) = chebyshev(j-1,y);
endfor
for i=1:n_basis
  for j=1:n_basis
    col = n_basis*(i-1) + j;
    tprod(:,col) = X_1(:,i).*X_2(:,j);
 endfor
endfor
c = tprod \ gr_scaled;
fit_global = tprod*c;



tile_size = 128;
tile_x = size(gr,1)/tile_size;
N = tile_size;
tprod = zeros(N,n_basis^2);
X_1 = zeros(N,n_basis);
X_2 = zeros(N,n_basis);
x = linspace(0,1,N);
y = linspace(0,1,N);
for j=1:n_basis
  X_1(:,j) = chebyshev(j-1,x);
  X_2(:,j) = chebyshev(j-1,y);
endfor
for i=1:n_basis
  for j=1:n_basis
    col = n_basis*(i-1) + j;
    tprod(:,col) = X_1(:,i).*X_2(:,j);
 endfor
endfor

fl = reshape(gr_scaled, tile_size,tile_x,tile_size,tile_x);
fl = permute(fl,[1 3 2 4]);
%fl = reshape(fl,128,128,16);

fits = zeros(tile_size,tile_size,tile_x,tile_x);
for i=1:4
  for j=1:4
    c = tprod \ fl(:,:,i,j);
    imfit = tprod*c;
    fits(:,:,i,j) = imfit;
  end
end

fig = figure('Units', 'inches', 'Position', [1, 1, 10, 5.2], 'Color', 'w');
set(fig, 'PaperPositionMode', 'auto');
subplot(1,3,1)
hold on;
imshow(gr_scaled);
title("Grayscale image");
subplot(1,3,2)
imshow(fit_global);
title("Global fit");
fits = permute(fits,[1 3 2 4]);
fits = reshape(fits,512,512);
subplot(1,3,3)
imshow(fits);
title(sprintf("Tiled chebyshev deg %d fit",n_basis));
print(fig, sprintf('figures/image_ls_%d',n_basis),'-dpng','-r300');








%gr_scaled_filtered = conv2(gr_scaled,f,'same');

%c = tprod \ gr_scaled;


%imfit = tprod*c;
%subplot(2,2,4);
%imshow(imfit,[]);
%title(sprintf('Chebyshev fit %d',n_basis));

