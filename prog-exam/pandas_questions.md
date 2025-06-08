### 45

```python
import pandas as pd

df = pd.DataFrame({
	'Brand': ['Maruti', 'Hyundai', 'Tata'],
	'Year': [2012, 2014, 2021],
	'Kms Driven': [50000, 30000, 40000],
	'City': ['Delhi', 'Mumbai', 'Chennai'],
	'Mileage': [28, 27, 25]
})
```

```python
print(df.loc[1])
```

```python
print(df.loc[2: 5])
```

```python
print(df.loc[ (df.Brand == 'Maruti') & (df.Mileage > 25) ])
```

```python
print(df.iloc[2])
```

```python
print(df.iloc[1, 5, 10, 23])
```

```python
display(data.iloc[1: 5])
display(data.iloc[1: 5, 2: 5])
```
