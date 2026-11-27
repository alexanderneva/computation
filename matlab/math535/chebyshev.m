function [P,w] = chebyshev(n,x)
  if (n==0)
    P=1;
  elseif (n==1)
    P=x;
  else
    P = 2*x.*chebyshev(n-1,x) - chebyshev(n-2,x);
  endif
  w = 1 ./ sqrt(1-x.^2);
endfunction

