import cv2
import numpy as np
# Load the image
image_path = '/Users/dolunaycimen/Downloads/taylor-swift.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Convert to grayscale
# Check if the image is loaded correctly
if image is None:
    print("Error: Image not found at the specified path.")
else:
    # Apply Sobel edge detection
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  # Gradient in X direction
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  # Gradient in Y direction
   # Convert gradients to absolute values and 8-bit images
    sobel_x = cv2.convertScaleAbs(sobel_x)
    sobel_y = cv2.convertScaleAbs(sobel_y)
    # Combine the two gradients
    sobel_combined = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
    # Save and display results
    cv2.imwrite("sobel_x.jpg", sobel_x)
    cv2.imwrite("sobel_y.jpg", sobel_y)
    cv2.imwrite("sobel_combined.jpg", sobel_combined)
    cv2.imshow("Original Image", image)
    cv2.imshow("Sobel X", sobel_x)
    cv2.imshow("Sobel Y", sobel_y)
    cv2.imshow("Sobel Combined", sobel_combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
