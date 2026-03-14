import pandas as pd


# Load the dataset
df = pd.read_csv('data/raw/netflix_titles.csv')

# Display the first 5 rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())


# Display the Datset structure
print("\nDataset structure:")
print(df.info())


# Check For missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Display the column names
print("\nColumn Names:")
print(df.columns)

# Display the shape of the dataset
print("\nDataset Shape:")
print(df.shape)

# Display the number of unique values in each column
print("\nUnique Values per Column:")
print(df.nunique())