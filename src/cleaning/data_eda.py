import pandas as pd
DATA_PATH = "../../data/data.csv"


df = pd.read_csv(DATA_PATH)
# print(df.head())
# data runs perfectly


# print("shape", df.shape)
# print("columns", df.columns)

# cleaning columns
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("(", "").str.replace(")", "")
# print("columns after cleaning", df.columns)


# print("info", df.info())
# print("describe", df.describe())


# print("null values", df.isnull().sum())
# no null values in the dataset

# print("duplicated values", df.duplicated().sum())
# no duplicated values in the dataset

# print(df.head()) 
print("Data cleaning and EDA completed successfully.")
df.to_csv("../../data/cleaned_data.csv", index=False)
