import cv2
# Load the image
image_path = '/Users/dolunaycimen/Downloads/taylor-swift.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Convert to grayscale
# Check if the image is loaded correctly
if image is None:
    print("Error: Image not found at the specified path.")
else:
    # Apply histogram equalization
    equalized_image = cv2.equalizeHist(image)
    # Save and display results
    cv2.imwrite("equalized_image.jpg", equalized_image)
    cv2.imshow("Original Grayscale Image", image)
    cv2.imshow("Equalized Image", equalized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
