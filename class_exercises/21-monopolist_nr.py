import numpy as np
import warnings

def newton_raphson(df, d2f, x0, tol=10**-6, max_iter=1000):
    
    n_iter = 0
    x_last = np.inf
    x_current = x0

    while np.abs(x_current - x_last) >= tol:

        if n_iter >= max_iter:
            warnings.warn(f"Did not converge after {n_iter=}!")
            return x_current, n_iter


        x_next = x_current - (1 / d2f(x_current)) * df(x_current)

        x_last = x_current
        x_current = x_next

        n_iter = n_iter + 1

    return x_current, n_iter

if __name__ == "__main__":
    
    df = lambda q: -(90 - 3 * q ** 2)
    d2f = lambda q: -(-6 * q)

    argmin, n_iter = newton_raphson(
        df=df,
        d2f=d2f,
        x0=0.1
    )
    
    print(f"{argmin=}")
    print(f"{n_iter=}")
