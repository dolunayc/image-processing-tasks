import cv2
import numpy as np

# Load the image
image_path = '/Users/dolunaycimen/Downloads/taylor-swift.jpg'
image = cv2.imread(image_path)

# Apply a median filter
filtered_image = cv2.medianBlur(image, 5)  # Apply median filter with a kernel size of 5

# Display the original and filtered images
cv2.imshow("Original Image", image)
cv2.imshow("Filtered Image (Median Filter)", filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
