import cv2
import numpy as np

# Load the image in grayscale
image_path = '/Users/dolunaycimen/Downloads/taylor-swift.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Edge detection using Canny
edges = cv2.Canny(image, 50, 150, apertureSize=3)

# ---- Local Processing: Edge Linking ----
# Here, we can perform local processing by applying dilating to strengthen the edges.
dilated_edges = cv2.dilate(edges, None, iterations=1)

# ---- Global Processing: Edge Linking ----
# Global processing involves closing small gaps in edges.
# We can use morphological closing to fill small gaps between detected edges.
kernel = np.ones((5, 5), np.uint8)
closed_edges = cv2.morphologyEx(dilated_edges, cv2.MORPH_CLOSE, kernel)

# Create a copy of the original image to draw the processed edges on
image_with_edges = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

# Draw the final edges after processing
image_with_edges[closed_edges == 255] = [0, 255, 0]  # Green color for detected edges

# Display the processed image
cv2.imshow("Edge Linking (Local + Global)", image_with_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
