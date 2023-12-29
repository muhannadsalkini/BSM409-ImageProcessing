import cv2
import numpy as np

def apply_sobel_filter(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply the Sobel filter to the grayscale image
    sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
    
    # Combine the x and y gradients to get the magnitude
    magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    
    # Scale the magnitude to the range [0, 255]
    magnitude = np.uint8(255 * magnitude / np.max(magnitude))
    
    return magnitude

def main():
    # Read an image
    image_path = 'path/to/your/image.jpg'
    original_image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if original_image is None:
        print(f"Error: Unable to read the image at {image_path}")
        return

    # Apply the Sobel filter
    sobel_result = apply_sobel_filter(original_image)

    # Display the original and Sobel-filtered images
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Sobel Filter Result', sobel_result)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
