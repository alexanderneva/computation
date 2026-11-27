function P = laguerre_prime(n,x)
  if (n==0)
    P = 0;
  elseif (n==1)
    P = -1;
  else
    P = (1/n) * ((2*n-x-1).*laguerre_prime(n-1,x) - laguerre(n-1,x) - (n-1)*laguerre_prime(n-2,x));
  end
end

