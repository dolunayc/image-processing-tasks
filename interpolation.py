import cv2
# Load the image
image_path = '/Users/dolunaycimen/Downloads/taylor-swift.jpg'
image = cv2.imread(image_path)
# Resize the image using different interpolation methods
# Nearest neighbor interpolation
nearest_image = cv2.resize(image, (800, 800), interpolation=cv2.INTER_NEAREST)

# Bilinear interpolation
bilinear_image = cv2.resize(image, (800, 800), interpolation=cv2.INTER_LINEAR)

# Bicubic interpolation
bicubic_image = cv2.resize(image, (800, 800), interpolation=cv2.INTER_CUBIC)

# Show the images
cv2.imshow("Original Image", image)
cv2.imshow("Nearest Neighbor Interpolation", nearest_image)
cv2.imshow("Bilinear Interpolation", bilinear_image)
cv2.imshow("Bicubic Interpolation", bicubic_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
