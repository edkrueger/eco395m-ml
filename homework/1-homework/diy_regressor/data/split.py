import pandas as pd

from sklearn.model_selection import train_test_split

df = pd.read_csv("advertising.csv")

train_df, test_df = train_test_split(df, random_state=42)

train_df.to_csv("advertising_train.csv", index=False)
test_df.to_csv("advertising_test.csv", index=False)