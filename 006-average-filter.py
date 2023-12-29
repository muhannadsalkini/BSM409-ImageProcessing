import cv2
import numpy as np

def apply_average_filter(image_path, output_path, kernel_size):
    # Read the input image
    original_image = cv2.imread(image_path)

    # Apply the average filter
    averaged_image = cv2.blur(original_image, (kernel_size, kernel_size))

    # Save the filtered image
    cv2.imwrite(output_path, averaged_image)

if __name__ == "__main__":
    # Replace 'input_image.jpg' with the path to your input image
    input_image_path = 'input_image.jpg'

    # Replace 'output_image_averaged.jpg' with the desired output path
    output_image_path = 'output_image_averaged.jpg'

    # Set the kernel size for the average filter (must be an odd number)
    kernel_size = 3

    # Apply the average filter
    apply_average_filter(input_image_path, output_image_path, kernel_size)

    print("Average filter applied successfully. Output saved to:", output_image_path)
