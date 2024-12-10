import pandas as pd

# Step 1: Create the initial dictionary with population data
data = {
    'City': ['Delhi', 'Kolkata', 'Mumbai'],
    '2021': [3.118, 1.497, 1.497],
    '2020': [3.029, 1.485, 2.041]
}

# Step 2: Create the DataFrame from the dictionary
df = pd.DataFrame(data)

# Step 3: Add the population data for 2019
df['2019'] = [2.94, 1.476, 2.019]

# Step 4: Calculate the average population for each city
df['Average'] = df[['2021', '2020', '2019']].mean(axis=1)

# Step 5: Display the final DataFrame
print(df)
