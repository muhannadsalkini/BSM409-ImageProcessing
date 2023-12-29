import cv2

def apply_on_off_operations(image, threshold_value):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply binary thresholding
    _, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

    return binary_image

def main():
    # Read an image
    image_path = 'path/to/your/image.jpg'
    original_image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if original_image is None:
        print(f"Error: Unable to read the image at {image_path}")
        return

    # Set the threshold value for on/off operations (adjust as needed)
    threshold_value = 128

    # Apply on/off operations
    binary_image = apply_on_off_operations(original_image, threshold_value)

    # Display the original and binary images
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Binary Image (On/Off Operations)', binary_image)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
