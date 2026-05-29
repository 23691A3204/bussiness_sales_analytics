import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_csv(r"C:\Users\Admin\OneDrive\Desktop\bussiness_sales_analytics\Dataset\train.csv")

print(df.head())

# Show first 5 rows
print("FIRST 5 ROWS")
print(df.head())

# Show column names
print("\nCOLUMNS")
print(df.columns)

# Dataset information
print("\nDATASET INFO")
print(df.info())

# Missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Statistical summary
print("\nDATA SUMMARY")
print(df.describe())

# If Sales column exists
if 'Sales' in df.columns:
    
    # Sales graph
    df['Sales'].plot(kind='hist')

    
state_sales = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(10)

state_sales.plot(kind='bar')

plt.title("Top 10 States by Sales")

plt.xlabel("State")

plt.ylabel("Sales")

plt.show()