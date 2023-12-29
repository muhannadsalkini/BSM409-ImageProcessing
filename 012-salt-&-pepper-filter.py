import cv2
import numpy as np

def apply_salt_and_pepper(image, salt_prob, pepper_prob):
    noisy_image = np.copy(image)

    # Add salt noise
    salt_mask = np.random.rand(*image.shape[:2]) < salt_prob
    noisy_image[salt_mask] = 255

    # Add pepper noise
    pepper_mask = np.random.rand(*image.shape[:2]) < pepper_prob
    noisy_image[pepper_mask] = 0

    return noisy_image

def main():
    # Read an image
    image_path = 'path/to/your/image.jpg'
    original_image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if original_image is None:
        print(f"Error: Unable to read the image at {image_path}")
        return

    # Set probabilities for salt and pepper noise
    salt_probability = 0.02  # Adjust as needed
    pepper_probability = 0.02  # Adjust as needed

    # Apply salt and pepper noise
    noisy_image = apply_salt_and_pepper(original_image, salt_probability, pepper_probability)

    # Display the original and noisy images
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Noisy Image (Salt and Pepper)', noisy_image)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
