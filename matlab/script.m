t = y = linspace(-5,5,41);

[tt,yy] = meshgrid (t,y);

%tz = vectorField(tt,yy);
f = @(t,y) [t-y];

tz = f(tt,yy);


quiver (tt,yy,tt+0.5,0.5*tz+yy);
title("t - y");

print -djpg figure.jpg;

f_2 = @(t,y) [1 - t.^2 - y.^2];

tz = f_2 (tt, yy);
quiver (tt,yy,tt+0.5,0.5*tz+yy);
title("1 - t^2 - y^2")
print -djpg figure2.jpg;

f_3 = @(t,y) [sin(t)-cos(y)];

tz = f_3 (tt, yy);

quiver(tt,yy,tt+0.5,0.5*tz+yy);
title("sin(t)-cos(y)");
print -djpg figure3.jpg;

f_4 = @(t,y) [t.^2 + y.^2];

tz = f_4 (tt,yy);
h = quiver(tt,yy,tt+0.5,0.5*tz+yy);
set(h, "maxheadsize", 0.25);
title(" x^2 + y^2")
print -djpg figure4.jpg
