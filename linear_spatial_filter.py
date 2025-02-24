import cv2
import numpy as np
# Load the image
image_path = '/Users/dolunaycimen/Downloads/taylor-swift.jpg'
image = cv2.imread(image_path)

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define a simple 3x3 linear kernel (e.g., an averaging filter)
kernel = np.ones((3, 3), np.float32) / 9

# Apply the linear filter using cv2.filter2D
filtered_image = cv2.filter2D(gray_image, -1, kernel)

# Show the result
cv2.imshow("Original Image", gray_image)
cv2.imshow("Filtered Image (Linear)", filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
