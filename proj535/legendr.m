function P = legendr (n,x)
  if (n==0)
    P = 1;
  elseif (n==1)
    P = x;
  else
    P = 1 / (n+1) .* ((2*n+1).*x.*legendr(n-1,x) - n*legendr(n-2,x));
  endif
endfunction

