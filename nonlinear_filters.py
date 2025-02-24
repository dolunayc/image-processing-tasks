import cv2
import numpy as np

# Load the image
image_path = '/Users/dolunaycimen/Downloads/taylor-swift.jpg'
image = cv2.imread(image_path)

# Apply a non-linear filter (Order Static) - Example: Erosion and Dilation
kernel = np.ones((5, 5), np.uint8)
image_eroded = cv2.erode(image, kernel, iterations=1)
image_dilated = cv2.dilate(image, kernel, iterations=1)

# Display the original and filtered images
cv2.imshow("Original Image", image)
cv2.imshow("Eroded Image", image_eroded)
cv2.imshow("Dilated Image", image_dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()
