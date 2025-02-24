import cv2
# Load the image
image_path = '/Users/dolunaycimen/Downloads/taylor-swift.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Convert to grayscale

# Check if the image is loaded correctly
if image is None:
    print("Error: Image not found at the specified path.")
else:
    # Threshold the image to create a binary version
    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    # Find contours
    contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Draw contours on the original image
    contour_image = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2BGR)  # Convert binary to BGR for visualization
    cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)
    # Save and display results
    cv2.imwrite("binary_image.jpg", binary_image)
    cv2.imwrite("contour_image.jpg", contour_image)
    cv2.imshow("Binary Image", binary_image)
    cv2.imshow("Contours Detected", contour_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()