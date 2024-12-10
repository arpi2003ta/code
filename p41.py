import numpy as np

# Step 1: Create a NumPy array of 9 equi-spaced numbers between 1 and 3
nparr = np.linspace(1, 3, 9)
print("nparr:", nparr)

# Step 2: Take the last six elements of 'nparr' in reverse order
revarr = nparr[-1:-7:-1]
print("revarr:", revarr)

# Step 3: Create an array with 6 random numbers between 0 and 1
randarr = np.random.rand(6)
print("randarr:", randarr)

# Step 4: Create a Boolean array where the element is True if corresponding element in randarr * 10 >= 5
boolarr = randarr * 10 >= 5
print("boolarr:", boolarr)

# Step 5: Take from 'revarr' only those elements where corresponding 'boolarr' element is True
finarr = revarr[boolarr]
print("finarr:", finarr)

# Step 6: Calculate and display statistics of 'finarr'
min_value = np.min(finarr)
max_value = np.max(finarr)
mean_value = np.mean(finarr)
median_value = np.median(finarr)
variance_value = np.var(finarr)
std_deviation_value = np.std(finarr)

print("\nStatistics of finarr:")
print("Minimum:", min_value)
print("Maximum:", max_value)
print("Mean:", mean_value)
print("Median:", median_value)
print("Variance:", variance_value)
print("Standard Deviation:", std_deviation_value)
