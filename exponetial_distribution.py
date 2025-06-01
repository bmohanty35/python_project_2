import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# Parameters
mean = 5
scale = mean  # For exponential distribution in NumPy, scale = mean
samples = 2000

# Generate samples
data = np.random.exponential(scale=scale, size=samples)

# Histogram
plt.hist(data, bins=50, density=True, alpha=0.6, color='skyblue', label='Histogram')

# PDF Overlay
x = np.linspace(0, np.max(data), 1000)
pdf = expon.pdf(x, scale=scale)
plt.plot(x, pdf, 'r-', lw=2, label='PDF (mean=5)')

# Labels and legend
plt.title('Exponential Distribution (Mean = 5)')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()

# Show plot
plt.grid(True)
plt.show()
