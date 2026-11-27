function P = chebyshev_2 (n,x)
  P = 0;
  if (n==0)
    P=1;
  elseif (n==1)
    P = 2*x;
  else
    P = 2.*x.*chebyshev_2(n-1,x) - chebyshev_2(n-2,x);
  endif
endfunction
