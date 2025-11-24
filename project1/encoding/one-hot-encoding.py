import pandas as pd


# Create a DataFrame with the given categorical data
data = {
    'color': ["red", "green", "blue"]
}

df = pd.DataFrame(data)

# Perform one-hot encoding
one_hot_encoded_df = pd.get_dummies(df, columns=['color'])

# Convert boolean values to integers
one_hot_encoded_df = one_hot_encoded_df.astype(int)

print(one_hot_encoded_df)