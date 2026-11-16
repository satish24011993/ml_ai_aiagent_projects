import pandas as pd

# Load Titanic dataset
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'

df = pd.read_csv(url)

print(df.head())
print(df.info())

categorical_data = df.select_dtypes(include = ['object']).columns

numerical_data = df.select_dtypes(include=['int64','float64']).columns

print('\nCategorical columns:\n',categorical_data.to_list())
print('\nNumerical columns:\n',numerical_data.to_list())

# df[categorical_data].value_counts
print('\n Display summary of categorical features.')
for col in categorical_data:
    print(f'{col}:\n', df[col].value_counts(),'\n')

print('\n Display summary of numerical features.')
print(df[numerical_data].describe())