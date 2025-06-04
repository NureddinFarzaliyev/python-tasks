import pandas as pd

data = pd.read_csv('titanic.csv')

total = len(data)

# Gender Statistics
print("\n-------- Gender Statistics --------")
male_count = data[data['Sex'] == 'male'].shape[0]
male_percent = male_count / total * 100
female_count = data[data['Sex'] == 'female'].shape[0]
female_percent = female_count / total * 100
print(f"Males: {male_count} ({male_percent:.2f}%)")
print(f"Females: {female_count} ({female_percent:.2f}%)")
male_female_ratio = male_count / female_count
print(f"Male to Female Ratio: {male_female_ratio:.2f}")

# Survived People
print("\n-------- Survival Statistics --------")
survived_count = data[data['Survived'] == 1].shape[0]
dead_count = data[data['Survived'] == 0].shape[0]
print(f"Survived: {survived_count}")
print(f"Dead: {dead_count}")
survived_dead_ratio = survived_count / dead_count
print(f"Survived to Dead Ratio: {survived_dead_ratio:.2f}")

# Survived People Based on Gender
print("\n-------- Survival/Gender Statistics --------")
survived_males = data[(data['Survived'] == 1) & (data['Sex'] == 'male')].shape[0]
survived_females = data[(data['Survived'] == 1) & (data['Sex'] == 'female')].shape[0]
survived_male_ratio = survived_males / male_count * 100
print(f"Survived males: {survived_males} ({survived_male_ratio:.2f}%)")
survived_female_ratio = survived_females / female_count * 100
print(f"Survived females: {survived_females} ({survived_female_ratio:.2f}%)")

# Passenger Class Statistics
print("\n-------- Class Statistics --------")
class_counts = data['Pclass'].value_counts()
print(class_counts)

# Survival Rate by Class
print("\n-------- Class/Survival Statistics --------")
survival_by_class = data.groupby('Pclass')['Survived'].mean()
print(survival_by_class)

# Age Distribution
print("\n-------- Age Statistics --------")
average_age = data['Age'].mean()
print(f"Average Age: {average_age:.2f}")
median_age = data['Age'].median()
print(f"Median Age: {median_age:.2f}")

# Ticket Prices
print("\n-------- Ticket Price Statistics --------")
average_fare = data['Fare'].mean()
fare_by_class = data.groupby('Pclass')['Fare'].mean()
print(f"Average Fare: {average_fare:.2f}")
print(fare_by_class)

# Adult / Child Survival Rate
print("\n-------- Age/Survival Statistics --------")
data['IsChild'] = data['Age'] < 18
child_survival_rate = data[data['IsChild']]['Survived'].mean()
adult_survival_rate = data[~data['IsChild']]['Survived'].mean()
print(f"Child Survival Rate: {child_survival_rate:.2f}")
print(f"Adult Survival Rate: {adult_survival_rate:.2f}")

# Missing data
print("\n-------- Missing Data Statistics --------")
missing_data = data.isnull().sum()
print(missing_data)