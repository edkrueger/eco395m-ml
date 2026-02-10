import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import statsmodels.formula.api as smf
from scipy.stats import shapiro
import statsmodels.api as sm

if __name__ == "__main__":

    raw_df = pd.read_csv("data/advertising.csv").set_index("id")
    df = raw_df.drop(128, axis="rows")


    liner_model = smf.ols("np.log(sales) ~ np.log(tv) + np.log(radio) + np.log(newspaper)", data=df)
    linear_res = liner_model.fit()
    print(linear_res.summary())

    e = linear_res.resid
    std_resid = (e- e.mean()) / e.std()

    print(std_resid)

    plt.hist(std_resid)
    plt.savefig("std_resid.png")

    print(shapiro(e))

    sm.qqplot(std_resid, line="45")
    plt.savefig("qqplot.png")

