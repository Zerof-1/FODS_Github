import pandas as pd
import matplotlib.pyplot as plt

# Load and clean data
df = pd.read_csv("weight_height.csv")
df.columns = df.columns.str.strip().str.lower()
df['gendercode'] = df['gender'].astype('category').cat.codes

# Create scatter plots
plt.figure(figsize=(15, 8))

plt.subplot(2, 3, 1)
plt.scatter(df['weight'], df['height'])
plt.title('Weight vs Height')

plt.subplot(2, 3, 2)
plt.scatter(df['age'], df['weight'])
plt.title('Age vs Weight')

plt.subplot(2, 3, 3)
plt.scatter(df['age'], df['height'])
plt.title('Height vs Age')

plt.subplot(2, 3, 4)
plt.scatter(df['gendercode'], df['height'])
plt.title('Gender vs Height')

plt.subplot(2, 3, 5)
plt.scatter(df['gendercode'], df['weight'])
plt.title('Gender vs Weight')

plt.tight_layout()
plt.show()
