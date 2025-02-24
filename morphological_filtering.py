import cv2
import numpy as np

# Load the image
image_path = '/Users/dolunaycimen/Downloads/taylor-swift.jpg'
image = cv2.imread(image_path)

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detector
edges = cv2.Canny(gray_image, 50, 150)

# Use Hough Transform to detect lines
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)

# Create a copy of the original image to display lines
line_image = np.copy(image)

# Draw the lines on the image
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Display the original image with detected lines
cv2.imshow("Hough Transform - Detected Lines", line_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
