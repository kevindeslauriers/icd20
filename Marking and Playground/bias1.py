import numpy as np
import matplotlib.pyplot as plt

# Load an image (replace 'path_to_image.jpg' with the actual path)
image = plt.imread('Marking and Playground\person.jpg')

# Extract color histograms using NumPy
hist_red, bins_red = np.histogram(image[:,:,0], bins=256, range=[0, 256])
hist_green, bins_green = np.histogram(image[:,:,1], bins=256, range=[0, 256])
hist_blue, bins_blue = np.histogram(image[:,:,2], bins=256, range=[0, 256])


# Calculate mean, median, and standard deviation for each color channel
mean_red = np.mean(hist_red)
median_green = np.median(hist_green)
std_dev_blue = np.std(hist_blue)


# Plot histograms
plt.figure(figsize=(12, 6))

plt.subplot(131)
plt.plot(hist_red, color='red')
plt.title('Red Channel Histogram')

plt.subplot(132)
plt.plot(hist_green, color='green')
plt.title('Green Channel Histogram')

plt.subplot(133)
plt.plot(hist_blue, color='blue')
plt.title('Blue Channel Histogram')

plt.show()
