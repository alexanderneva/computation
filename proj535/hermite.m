function P = hermite (n,x)
  P = 0;
  if (n==0)
    P=1;
  elseif (n==1)
    P = 2*x;
  else
    P = 2.*x.*hermite(n-1,x) - 2.*(n-1).*hermite(n-2,x);
  endif
endfunction
