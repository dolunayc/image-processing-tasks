import cv2
import numpy as np

# Load the image
image_path = '/Users/dolunaycimen/Downloads/taylor-swift.jpg'
image = cv2.imread(image_path)
# Convert the image to grayscale for simplicity
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Reduce the intensity levels by scaling
scaled_image = (gray_image // 32) * 32  # Reducing intensity levels to 8 (0-255 to 0-7)
# Show the scaled intensity image
cv2.imshow("Intensity Level Reduced Image", scaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
