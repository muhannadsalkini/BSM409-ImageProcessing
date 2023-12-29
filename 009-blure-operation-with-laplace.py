import cv2
import numpy as np

def apply_blur_and_laplace(image_path, output_path, kernel_size, sigma, laplace_ksize):
    # Read the input image
    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(original_image, (kernel_size, kernel_size), sigma)

    # Apply Laplacian filter
    laplacian_image = cv2.Laplacian(blurred_image, cv2.CV_64F, ksize=laplace_ksize)

    # Convert the result to 8-bit for display
    laplacian_image = np.uint8(np.abs(laplacian_image))

    # Save the filtered image
    cv2.imwrite(output_path, laplacian_image)

if __name__ == "__main__":
    # Replace 'input_image.jpg' with the path to your input image
    input_image_path = 'input_image.jpg'

    # Replace 'output_image_blur_laplace.jpg' with the desired output path
    output_image_path = 'output_image_blur_laplace.jpg'

    # Set the kernel size for the Gaussian blur (must be an odd number)
    kernel_size = 3

    # Set the standard deviation (sigma) for the Gaussian blur
    sigma = 1.0

    # Set the kernel size for the Laplacian filter (must be an odd number)
    laplace_ksize = 3

    # Apply blur and Laplace
    apply_blur_and_laplace(input_image_path, output_image_path, kernel_size, sigma, laplace_ksize)

    print("Blur and Laplace applied successfully. Output saved to:", output_image_path)
