import pandas as pd

# Load the dataset
df = pd.read_csv("data/E-commerce_Orders.csv")

print("==== BASIC INFO ====")
print(df.info())

print("==== HEAD ====")
print(df.head())

print("\n==== SHAPE ====")
print(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")

print("\n ==== DESCRIBE ====")
print(df.describe())

# Check null values
print("\n ==== NULL VALUES ====")
print(df.isnull().sum())

# check Duplicate values
print("\n==== DUPLICATE VALUES ====")
print(df.duplicated().sum())

# Check OrderID uniquesness
print("\n ==== UNIQUE OrderID ====")
print(f"(Total OrderIDs: df['OrderID'].count()")
print(f"Unique OrderIDs: df['OrderID'].nunique()")

if(df['OrderID'].nunique() != df['OrderID'].count()):
    print("Warning: There are duplicate OrderIDs in the dataset.")
else:
    print("All OrderIDs are unique.")

# Convert Date for analysis
df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors = 'coerce')
print("\n DATE CHECK ====")
print(f"Minimum Order Date: {df['OrderDate'].min()}")
print(f"Maximum Order Date: {df['OrderDate'].max()}")

# Future Date Check
future_dates = df[df['OrderDate'] > pd.Timestamp.now()]
print("\n==== FUTURE DATE RECORDS ====")
print(f"Number of future date records: {future_dates.shape[0]}")

# Check TotalAmount type and stats
df['TotalAmount'] = pd.to_numeric(df['TotalAmount'], errors='coerce')
print("\n==== TotalAmount STATS ====")
print(df['TotalAmount'].describe())

# Check for negative TotalAmount 
negative_amounts = df[df['TotalAmount']< 0]
print("\n==== NEGATIVE TotalAmount RECORDS ====")
print(f"Number of negative TotalAmount records: {negative_amounts.shape[0]}")

# Order Status discription
print("\n==== Order Status Discription ====")
print(df['OrderStatus'].value_counts())
