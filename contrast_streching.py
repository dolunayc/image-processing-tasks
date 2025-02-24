import cv2
import numpy as np

# Load the image
image_path = '/Users/dolunaycimen/Downloads/taylor-swift.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply contrast stretching
min_intensity = np.min(image)
max_intensity = np.max(image)

# Stretch the contrast
stretched_image = (image - min_intensity) * (255 / (max_intensity - min_intensity))

# Convert the result to uint8
stretched_image = np.uint8(stretched_image)

# Display the original and contrast stretched images
cv2.imshow("Original Image", image)
cv2.imshow("Contrast Stretched Image", stretched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
