import cv2

# Load the image
image_path = '/Users/dolunaycimen/Downloads/taylor-swift.jpg'
image = cv2.imread(image_path)  # Read the image (Default: color)

# Show the image
cv2.imshow("Original Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
