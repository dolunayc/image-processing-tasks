import cv2
import numpy as np

# Load the image
image_path = '/Users/dolunaycimen/Downloads/taylor-swift.jpg'
image = cv2.imread(image_path)

# Check if the image is loaded
if image is None:
    print("Error: Image not found or unable to read.")
else:
    print("Image loaded successfully.")
    print(f"Image shape: {image.shape}, Data type: {image.dtype}")

    # Ensure the image is in unsigned 8-bit integer format
    if image.dtype != np.uint8:
        image = np.asarray(image, dtype=np.uint8)

    # Print pixel values before transformation (first 5 pixels of the first row)
    print("First 5 pixels before transformation:", image[0, :5])

    # Create the negative image
    negative_image = cv2.bitwise_not(image)

    # Print pixel values after transformation (first 5 pixels of the first row)
    print("First 5 pixels after transformation:", negative_image[0, :5])

    # Save the results for manual verification
    cv2.imwrite("debug_original_image.jpg", image)
    cv2.imwrite("debug_negative_image.jpg", negative_image)
    # Display the images
    cv2.imshow("Original Image", image)
    cv2.imshow("Negative Image", negative_image)
    cv2.waitKey(0)

   cv2.destroyAllWindows()
