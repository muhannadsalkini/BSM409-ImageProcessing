import cv2

def apply_gaussian_filter(image, kernel_size):
    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    return blurred_image

def main():
    # Read an image
    image_path = 'path/to/your/image.jpg'
    original_image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if original_image is None:
        print(f"Error: Unable to read the image at {image_path}")
        return

    # Set the kernel size for the Gaussian filter (should be an odd number)
    kernel_size = 5

    # Apply Gaussian filter
    blurred_image = apply_gaussian_filter(original_image, kernel_size)

    # Display the original and blurred images
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Blurred Image', blurred_image)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
