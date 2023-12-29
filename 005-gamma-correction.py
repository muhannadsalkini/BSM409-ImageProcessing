import cv2
import numpy as np

def apply_gamma_correction(image, gamma):
    # Normalize pixel values to the range [0, 1]
    normalized_image = image / 255.0
    # Apply gamma correction
    gamma_corrected_image = np.power(normalized_image, gamma)
    # Scale the values back to the range [0, 255]
    gamma_corrected_image = (gamma_corrected_image * 255).astype(np.uint8)
    return gamma_corrected_image

def main():
    # Read an image
    image_path = 'path/to/your/image.jpg'
    original_image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if original_image is None:
        print(f"Error: Unable to read the image at {image_path}")
        return

    # Set the gamma parameter (adjust as needed)
    gamma = 1.5

    # Apply gamma correction
    gamma_corrected_image = apply_gamma_correction(original_image, gamma)

    # Display the original and gamma-corrected images
    cv2.imshow('Original Image', original_image)
    cv2.imshow(f'Gamma Corrected (gamma={gamma})', gamma_corrected_image)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
