import cv2
import numpy as np

# Load the image
image_path = '/Users/dolunaycimen/Downloads/taylor-swift.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply Gaussian Blur to reduce noise
blurred_image = cv2.GaussianBlur(image, (5, 5), 1)

# Apply the Laplacian filter to detect edges
laplacian = cv2.Laplacian(blurred_image, cv2.CV_64F)

# Convert the result to uint8
laplacian_edges = np.uint8(np.absolute(laplacian))

# Display the original and Marr-Hildreth filtered images
cv2.imshow("Original Image", image)
cv2.imshow("Marr-Hildreth Edge Detection", laplacian_edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
