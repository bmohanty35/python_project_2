import numpy as np
import matplotlib.pyplot as plt

# Parameters
population_size = 10000
sample_size = 30
num_samples = 1000

# Step 1: Generate population from a uniform distribution
population = np.random.uniform(low=0.0, high=10.0, size=population_size)

# Step 2: Draw samples and compute sample means
sample_means = []

for _ in range(num_samples):
    sample = np.random.choice(population, size=sample_size)
    sample_means.append(np.mean(sample))

# Convert to numpy array
sample_means = np.array(sample_means)

# Step 3: Plot the original uniform distribution
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(population, bins=50, color='skyblue', density=True)
plt.title("Original Uniform Distribution")
plt.xlabel("Value")
plt.ylabel("Density")

# Step 4: Plot the distribution of sample means
plt.subplot(1, 2, 2)contro
plt.hist(sample_means, bins=40, color='orange', density=True)
plt.title("Distribution of Sample Means (n=30)")
plt.xlabel("Sample Mean")
plt.ylabel("Density")

plt.tight_layout()
plt.show()
