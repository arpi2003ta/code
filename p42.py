import pandas as pd

# Step 1: Create the initial dictionary with student marks in Physics, Chemistry, and Mathematics
data = {
    'Name': ['Abhijit', 'Lata', 'Asha', 'Preetam'],
    'Physics': [85, 80, 89, 88],
    'Chemistry': [90, 92, 80, 93],
    'Mathematics': [92, 99, 82, 95]
}

# Step 2: Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Step 3: Add the Biology marks column
df['Biology'] = [88, 82, 80, 79]

# Step 4: Calculate the Total marks for each student and add it as a new column
df['Total'] = df['Physics'] + df['Chemistry'] + df['Mathematics'] + df['Biology']

# Step 5: Display the descriptive statistics of all the columns
print("Student Marks DataFrame:")
print(df)

# Display the descriptive statistics for all the numerical columns
print("\nDescriptive Statistics:")
print(df.describe())
