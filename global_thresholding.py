import cv2
import numpy as np
# Load the image
image_path = '/Users/dolunaycimen/Downloads/taylor-swift.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
# Apply global thresholding
 thresholded_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
# Display the original and thresholded images
cv2.imshow("Original Image", image)
cv2.imshow("Global Thresholded Image", thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
