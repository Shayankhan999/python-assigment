import pandas as pd
import numpy as np

print("--- Step 1: Data Load Ho Raha Hy ---")
df = pd.read_csv('supermarket_sales_case_study.csv')


rows_initial, cols_initial = df.shape
print(f"Shuru mein Rows: {rows_initial}, Columns: {cols_initial}\n")


print("--- Step 2: Data Ka Audit ---")
print("Missing values har column mein:\n", df.isnull().sum())
print("\nExact duplicate rows ki tadad:", df.duplicated().sum())
print("Duplicate Invoice IDs ki tadad:", df.duplicated(subset=['Invoice ID']).sum())
print("Gender columns ki unique values:", df['Gender'].unique())
print("Payment columns ki unique values:", df['Payment'].unique())


print("--- Step 3: Exact Duplicate Rows Ko Delete Karna ---")

df = df.drop_duplicates()

print("Rows bache:", len(df))


print("--- Step 4: Duplicate Invoice IDs Theek Karna ---")


df = df.drop_duplicates(subset=['Invoice ID'], keep='last')

print("Rows bache:", len(df))


print("--- Step 5: Text Columns Ko Standardise Karna ---")

df['Gender'] = df['Gender'].astype(str).str.strip().str.lower()
df['Payment'] = df['Payment'].astype(str).str.strip().str.lower()

# Sahi spellings par map karna
gender_map = {'male': 'Male', 'female': 'Female'}
payment_map = {'cash': 'Cash', 'credit card': 'Credit card', 'ewallet': 'Ewallet'}

df['Gender'] = df['Gender'].map(gender_map)
df['Payment'] = df['Payment'].map(payment_map)
print("Text cleaning mukammal!\n")


print("--- Step 6: Negative Quantities Ko Positive Karna ---")
df['Quantity'] = df['Quantity'].abs()
print("Quantities theek ho gayin!\n")


print("--- Step 7: Mixed Dates Ko Format Karna ---")

date_format_1 = pd.to_datetime(df['Date'], format='%m/%d/%Y', errors='coerce')
date_format_2 = pd.to_datetime(df['Date'], format='%d-%m-%Y', errors='coerce')

df['Clean_Date'] = date_format_1.fillna(date_format_2)
print("Dates parse ho gayin!\n")


