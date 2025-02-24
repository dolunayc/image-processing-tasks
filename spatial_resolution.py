import cv2
# Load the image
image_path = '/Users/dolunaycimen/Downloads/taylor-swift.jpg'
image = cv2.imread(image_path)
# Resize the image to demonstrate spatial resolution
resized_image = cv2.resize(image, (200, 200))  # Reducing resolution to 200x200 pixels
# Show the resized image
cv2.imshow("Resized Image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
