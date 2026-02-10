import pandas as pd

import statsmodels.formula.api as smf
from statsmodels.stats.diagnostic import linear_reset
from statsmodels.stats.anova import anova_lm

if __name__ == "__main__":

    df = pd.read_csv("data/advertising.csv").set_index("id")

    liner_model = smf.ols("sales ~ tv + radio + newspaper", data=df)
    linear_res = liner_model.fit()
    print(linear_res.summary())

    reset_res = linear_reset(linear_res, power=2, test_type='exog', use_f=True)
    print(reset_res)

    interactions_model = smf.ols("sales ~ tv*radio*newspaper", data=df)
    interactions_res =interactions_model.fit()
    print(interactions_res.summary())

    print(anova_lm(linear_res, interactions_res))


    squared_model = smf.ols("sales ~ tv + radio + newspaper + tv**2 + radio**2 + newspaper**2", data=df)
    squared_res =interactions_model.fit()
    print(interactions_res.summary())

    print(anova_lm(linear_res, squared_res))

    two_way_model = smf.ols("sales ~ tv*radio*newspaper - tv:radio:newspaper", data=df)
    two_way_res = two_way_model.fit()
    print(two_way_res.summary())

    print(anova_lm(two_way_res, interactions_res))

    
    

