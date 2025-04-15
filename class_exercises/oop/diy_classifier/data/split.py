import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

df = pd.read_csv("Caravan.csv").assign(Purchase=lambda df_: np.where(df_["Purchase"] == "Yes", 1, 0))

train_df, test_df = train_test_split(df, random_state=3)

train_df.to_csv("caravan_train.csv", index=False)
test_df.to_csv("caravan_test.csv", index=False)