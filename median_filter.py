import cv2
import numpy as np

# Load the image
image_path = '/Users/dolunaycimen/Downloads/taylor-swift.jpg'
image = cv2.imread(image_path)

# Apply median filter
image_median_filtered = cv2.medianBlur(image, 5)

# Display the original and median filtered images
cv2.imshow("Original Image", image)
cv2.imshow("Median Filtered Image", image_median_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
