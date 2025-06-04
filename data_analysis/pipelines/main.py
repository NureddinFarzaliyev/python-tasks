import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

# CSV faylını oxu
data = pd.read_csv('melb_data.csv')

# İstifadə olunacaq sütunlar
num_cols = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt']
cat_cols = ['Regionname']

# Numerical sütunlarda boşluqları orta ilə doldur
num_imputer = SimpleImputer(strategy='mean')
data[num_cols] = num_imputer.fit_transform(data[num_cols])

# Categorical sütunlarda boşluqları ən çox təkrarlanan dəyərlə doldur
cat_imputer = SimpleImputer(strategy='most_frequent')
data[cat_cols] = cat_imputer.fit_transform(data[cat_cols])

# One-hot encoding
encoder = OneHotEncoder(sparse=False)
encoded = encoder.fit_transform(data[cat_cols])
encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(cat_cols), index=data.index)

# Numerical və encoded categorical sütunları birləşdir
final_data = pd.concat([data[num_cols], encoded_df], axis=1)

print(final_data.head())