import cv2
import numpy as np

# Load the image
image_path = '/Users/dolunaycimen/Downloads/taylor-swift.jpg'
image = cv2.imread(image_path)

# Create a kernel for the weighted filter (Gaussian-like kernel)
kernel = np.ones((5, 5), np.float32) / 25  # A simple average filter kernel

# Apply the weighted smoothing filter
image_weighted_filtered = cv2.filter2D(image, -1, kernel)

# Display the original and weighted filtered images
cv2.imshow("Original Image", image)
cv2.imshow("Weighted Filtered Image", image_weighted_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
