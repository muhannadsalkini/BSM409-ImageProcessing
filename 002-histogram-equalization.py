import cv2
import numpy as np

# Load the image
image = cv2.imread('input_image.jpg', 0)  # Load the image in grayscale

# Calculate the histogram
hist, bins = np.histogram(image.flatten(), 256, [0, 256])

# Calculate the cumulative distribution function (CDF)
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()

# Perform histogram equalization
equalized_image = np.interp(image, bins[:-1], cdf_normalized)

# Convert the resulting image back to 8-bit unsigned integer
equalized_image = np.uint8(equalized_image)

# Save the equalized image
cv2.imwrite('equalized_image.jpg', equalized_image)

# Display the original and equalized images
cv2.imshow('Original Image', image)
cv2.imshow('Equalized Image', equalized_image)

# Wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
