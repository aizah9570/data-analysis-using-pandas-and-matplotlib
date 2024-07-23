import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Item': ['Chicken Wing', 'Burger', 'French Fries', 'Nuggets', 'Coleslaw', 'Mashed Potatoes', 'Pepsi', 'Chicken Sandwich'],
    'Category': ['Chicken', 'Burger', 'Side', 'Chicken', 'Side', 'Side', 'Drink', 'Burger'],
    'Calories': [290, 450, 320, 270, 180, 120, 150, 500],
    'Protein (g)': [18, 28, 4, 15, 1, 3, 0, 25],
    'Carbs (g)': [0, 40, 45, 15, 25, 22, 41, 46],
    'Fat (g)': [21, 25, 15, 17, 8, 5, 0, 28],
    'Price ($)': [3.5, 4.2, 2.5, 3.0, 2.0, 2.2, 1.5, 4.8]
}

df = pd.DataFrame(data)

print(df.info())
print(df.describe())

plt.figure(figsize=(8, 5))
sns.histplot(df['Calories'], bins=8, kde=True, color='skyblue')
plt.title('Calories Distribution')
plt.xlabel('Calories')
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(x='Calories', y='Protein (g)', data=df, hue='Category', s=80)
plt.title('Protein vs Calories')
plt.show()

avg_nutrients = df.groupby('Category').mean()[['Protein (g)', 'Carbs (g)', 'Fat (g)']]
avg_nutrients.plot(kind='bar', stacked=True, figsize=(8, 5))
plt.title('Average Macronutrient Composition')
plt.ylabel('Grams')
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x='Category', y='Price ($)', data=df, palette='pastel')
plt.title('Prices by Category')
plt.show()

plt.figure(figsize=(6, 5))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".1f")
plt.title('Nutritional & Price Correlations')
plt.show()
