import cv2
import numpy as np

def apply_gaussian_filter(image_path, output_path, kernel_size, sigma):
    # Read the input image
    original_image = cv2.imread(image_path)

    # Apply the Gaussian filter
    gaussian_image = cv2.GaussianBlur(original_image, (kernel_size, kernel_size), sigmaX=sigma)

    # Save the filtered image
    cv2.imwrite(output_path, gaussian_image)

if __name__ == "__main__":
    # Replace 'input_image.jpg' with the path to your input image
    input_image_path = 'input_image.jpg'

    # Replace 'output_image_gaussian.jpg' with the desired output path
    output_image_path = 'output_image_gaussian.jpg'

    # Set the kernel size for the Gaussian filter (must be an odd number)
    kernel_size = 3

    # Set the standard deviation (sigma) for the Gaussian filter
    sigma = 1.0

    # Apply the Gaussian filter
    apply_gaussian_filter(input_image_path, output_image_path, kernel_size, sigma)

    print("Gaussian filter applied successfully. Output saved to:", output_image_path)
