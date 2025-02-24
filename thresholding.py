import cv2
# Load the image
image_path = '/Users/dolunaycimen/Downloads/taylor-swift.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Convert to grayscale directly
# Check if the image is loaded correctly
if image is None:
    print("Error: Image not found at the specified path.")
else:
    # Apply a binary threshold
    threshold_value = 127  # Threshold value
    max_value = 255  # Value to assign if the pixel value exceeds the threshold
    _, binary_image = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_BINARY)
    # Save and display the results
    cv2.imwrite("thresholded_image.jpg", binary_image)
    cv2.imshow("Original Grayscale Image", image)
    cv2.imshow("Binary Image", binary_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
