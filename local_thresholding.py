import cv2
import numpy as np

# Load the image
image_path = '/Users/dolunaycimen/Downloads/taylor-swift.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply local thresholding using adaptive mean method
thresholded_image_local = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                                cv2.THRESH_BINARY, 11, 2)

# Display the original and thresholded images
cv2.imshow("Original Image", image)
cv2.imshow("Local Thresholded Image", thresholded_image_local)
cv2.waitKey(0)
cv2.destroyAllWindows()
