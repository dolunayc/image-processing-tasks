import cv2
import numpy as np

# Load the image
image_path = '/Users/dolunaycimen/Downloads/taylor-swift.jpg'
image = cv2.imread(image_path)

# Apply a Gaussian blur filter (Lowpass filter)
filtered_image_gaussian = cv2.GaussianBlur(image, (5, 5), 0)  # 5x5 kernel

# Display the original and filtered images
cv2.imshow("Original Image", image)
cv2.imshow("Lowpass Gaussian Filtered Image", filtered_image_gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()
