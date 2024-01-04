import math
from scipy.optimize import fsolve

u = 2510 #v spalin wzg rakiety [m/s]
M = 2.8 * 10**6 #masa rakiety w momencie oderwania [kg]
m = 13.3 * 10**3 #zużycie paliwa [kg/s]
g = 9.81 #a ziemskie [m/s**2]
v = 335 #[m/s]
#(u*math.log(M/(M-m*t))-g*t)

def fun(t):
    #w(t) - v = 0
    return [u * math.log ( M/( M - m * t[0] ) ) - g * t[0] - v]

root = fsolve(fun,[1])
print(root)
