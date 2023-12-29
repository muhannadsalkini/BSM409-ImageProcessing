import cv2
import numpy as np

def apply_smoothing(image, kernel_size):
    # Apply Gaussian blur for smoothing
    smoothed_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    return smoothed_image

def apply_sharpening(image, alpha, beta):
    # Apply Laplacian filter for sharpening
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    sharpened_image = image + alpha * laplacian

    # Clip pixel values to the valid range [0, 255]
    sharpened_image = np.clip(sharpened_image, 0, 255).astype(np.uint8)

    # Add beta for brightness adjustment
    sharpened_image = cv2.addWeighted(image, 1 + beta, sharpened_image, -beta, 0)
    return sharpened_image

def main():
    # Read an image
    image_path = 'path/to/your/image.jpg'
    original_image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if original_image is None:
        print(f"Error: Unable to read the image at {image_path}")
        return

    # Set parameters for smoothing
    smoothing_kernel_size = 5

    # Apply smoothing
    smoothed_image = apply_smoothing(original_image, smoothing_kernel_size)

    # Set parameters for sharpening
    sharpening_alpha = 1.5  # Scaling factor for the Laplacian
    sharpening_beta = 0.5   # Brightness adjustment

    # Apply sharpening
    sharpened_image = apply_sharpening(smoothed_image, sharpening_alpha, sharpening_beta)

    # Display the original, smoothed, and sharpened images
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Smoothed Image', smoothed_image)
    cv2.imshow('Sharpened Image', sharpened_image)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
