N = 100;
%num_basis = 10;
data = linspace(-2*pi,2*pi,N)';
A = zeros(N,num_basis);
trials = 30;
errors = zeros(trials,1);
y = sin(data) + 0.2*randn(N,1);
for trial=1:trials
  num_basis = trial;
    for i=1:num_basis
      if (i==1)
        A(:,i) = 1;
      elseif (i==2)
        A(:,i) = data;
      else
        A(:,i) = 2*data.*A(:,i-1) - A(:,i-2);
      end
    end
  c = A \ y;
  yfit = A*c;
  errors(trial) = rmse(y,yfit);
end





