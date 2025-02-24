import cv2
# Load the image
image_path = '/Users/dolunaycimen/Downloads/taylor-swift.jpg'
image = cv2.imread(image_path)
# Downsize the image for sampling
resized_image = cv2.resize(image, (100, 100))  # Reducing resolution for sampling
# Convert image to grayscale for quantization
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
# Apply quantization by reducing intensity levels
quantized_image = gray_image // 32 * 32  # Reducing intensity levels
# Show the quantized image
cv2.imshow("Quantized Image", quantized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
