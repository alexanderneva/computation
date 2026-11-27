function r = rsquare (x,y)
  x = x(:);
  y = y(:);
    sse = (x-y)'*(x-y);
    ybar = mean(y);
    sst = (y-ybar)'*(y-ybar);
    r = 1 - sse/sst;
end
