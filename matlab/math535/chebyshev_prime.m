function P = chebyshev_prime(n,x)
  if (n==0)
    P=0;
  elseif (n==1)
    P=1;
  else
    P = 2*chebyshev(n-1,x) + 2*x.*chebyshev_prime(n-1,x) - chebyshev_prime(n-2,x);
  endif
endfunction
