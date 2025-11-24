from sklearn.preprocessing import LabelEncoder

# create a sample dataset with a categorical variable
data = ["small", "medium", "large", "small", "large"]

# create a label encoder object
label_encoder = LabelEncoder()

# fit and transform the data using the label encoder
encoded_data = label_encoder.fit_transform(data)

# print the encoded data
print(encoded_data)