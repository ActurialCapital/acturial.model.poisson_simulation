import numpy as np
from random import random
from scipy.stats import norm
import pandas as pd

def inverse_poisson(u, l):
    p = np.exp(-l)
    F = p
    n = 0
    while u > F:
        n = n + 1
        p = p * (l / n)
        F = F + p           	
    invpoisson = n
    return invpoisson
    
def with_jumps(
        S0=100,
        rf=0.05,
        sigma=0.2,
        n_iter=100,
        n_simul=100,
        t=1,
        l=2,
        mu_y=0.02,
        var_y=0.25,
        K=100
    ):
    list_simul = []
    list_jumps = []
    dt = t / n_iter
    Sum = 0    
    for m in range(0, n_simul):
        ts=[S0]
        jump = 0
        S = S0
        n_jump = 0
        for i in range(0, n_iter):
            u = random()
            alea_normal = norm.ppf(u)
            alea_poisson = inverse_poisson(u, l * dt)
            if alea_poisson == 0:
                jump = 0
            else:
                for j in range(0, alea_poisson):
                    jump = jump + norm.ppf(random(), loc=mu_y, scale=var_y)
                    
            x = np.log(S) + (rf - sigma**2 * 0.5) * dt + np.sqrt(dt) * sigma * alea_normal + jump
            S = np.exp(x)
            ts.append(S)
            n_jump = n_jump + alea_poisson
            
        list_simul.append(pd.Series(ts))
        
        payoff = np.max(S - K, 0)
        Sum = Sum + np.exp(-rf * t) * payoff
        list_jumps.append(n_jump)
    price = (1 / n_simul) * Sum
    return {'price': price, 'simulation': list_simul, 'jumps': list_jumps}


if __name__ == '__main__':
    
    # calc simulations
    items = with_jumps(
        S0=100,
        rf=0.05,
        sigma=0.2,
        n_iter=100,
        n_simul=100,
        t=1,
        l=2,
        mu_y=0.02,
        var_y=0.25,
        K=100
    )
    
    for i in range(0, 4):
        items['simulation'][i].plot()
        
    pd.DataFrame(items['simulation']).stack().hist(bins=100)
