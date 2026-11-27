function P = laguerre (n,x)
  P = 1;
  if (n==0)
    P=1;
  elseif (n==1)
    P = 1-x;
  else
    P = 1/n .* ((2*n-x-1 ).*laguerre(n-1,x) - (n-1).*laguerre(n-2,x));
  endif
endfunction
