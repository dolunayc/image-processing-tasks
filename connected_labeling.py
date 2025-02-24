import cv2
import numpy as np

# Load the image
image_path = '/Users/dolunaycimen/Downloads/taylor-swift.jpg'
image = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold the image to get a binary image
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Perform connected components analysis
num_labels, labels = cv2.connectedComponents(binary)

# Visualize the results
output_image = cv2.applyColorMap(np.uint8(labels * 255 / num_labels), cv2.COLORMAP_JET)

# Show the output image
cv2.imshow("Connected Components", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
