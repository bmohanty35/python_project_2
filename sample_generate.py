import numpy as np

# Define values and their probabilities
values = [1, 2, 3]
probabilities = [0.25, 0.35, 0.4]

# Generate a sample of size 1000
sample = np.random.choice(values, size=1000, p=probabilities)

# Compute statistics
mean = np.mean(sample)
variance = np.var(sample)
std_dev = np.std(sample)

# Print results
print("Empirical Statistics from Sample of Size 1000:")
print(f"Mean:            {mean:.4f}")
print(f"Variance:        {variance:.4f}")
print(f"Std Deviation:   {std_dev:.4f}")
