import cv2
import numpy as np

# Load the image
image_path = '/Users/dolunaycimen/Downloads/taylor-swift.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply adaptive thresholding using Gaussian mean method
adaptive_threshold_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                                cv2.THRESH_BINARY, 11, 2)

# Display the original and thresholded images
cv2.imshow("Original Image", image)
cv2.imshow("Adaptive Thresholded Image", adaptive_threshold_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
