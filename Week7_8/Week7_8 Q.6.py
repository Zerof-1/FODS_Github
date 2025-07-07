import pandas as pd

# Read CSV file
df = pd.read_csv("weight_height.csv")

# Clean column names (in case of spaces or case mismatch)
df.columns = df.columns.str.strip().str.lower()

# Check column names to ensure they include 'weight' and 'height'
print("Columns:", df.columns)

# Calculate BMI
df['bmi'] = df['weight'] / df['height']

# Define a function to classify risk based on BMI
def calculate_risk(bmi):
    if bmi < 18.5:
        return "Nutrient deficient"
    elif 18.5 <= bmi <= 24.9:
        return "Lower risk"
    elif 25 <= bmi <= 29.9:
        return "Heart disease risk"
    elif 30 <= bmi <= 34.9:
        return "Higher risk of diabetes, heart disease"
    elif bmi >= 40:
        return "Serious health condition risk"
    else:
        return "Moderate risk"

# Apply the risk function to each BMI
df['risk'] = df['bmi'].apply(calculate_risk)


print(df.head())
df.to_csv("updated_weight_height.csv", index=False)

