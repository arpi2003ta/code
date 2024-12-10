import pandas as pd
# Create the data frame
data = {
 'Name': ['Abhishek', 'Usha', 'Shreya', 'Vijay'],
 'Physics': [88, 81, 90, 87],
 'Chemistry': [82, 91, 85, 89],
 'Mathematics': [95, 97, 89, 91],
}
df = pd.DataFrame(data)
# Add the Biology column
df['Biology'] = [82, 79, 90, 80]
# Calculate the Aggregate marks
df['Aggregate'] = df[['Physics', 'Chemistry', 'Mathematics', 'Biology']].sum(axis=1)
# Display the data frame and descriptive statistics
print("Data Frame:")
print(df)
print("\nDescriptive Statistics:")
print(df.describe())
