import cv2
import numpy as np

def contra_harmonic_mean_filter(image_path, output_path, filter_size, Q):
    # Read the input image
    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply the contra-harmonic mean filter
    filtered_image = cv2.filter2D(original_image, -1, np.ones((filter_size, filter_size), np.float32) / (filter_size**2),
                                  borderType=cv2.BORDER_CONSTANT)

    numerator = cv2.filter2D(original_image ** (Q + 1), -1, np.ones((filter_size, filter_size), np.float32), borderType=cv2.BORDER_CONSTANT)
    denominator = cv2.filter2D(original_image ** Q, -1, np.ones((filter_size, filter_size), np.float32), borderType=cv2.BORDER_CONSTANT)

    # Avoid division by zero
    filtered_image = np.divide(numerator, denominator, out=np.zeros_like(numerator), where=denominator != 0)

    # Convert the result to 8-bit for display
    filtered_image = np.uint8(filtered_image)

    # Save the filtered image
    cv2.imwrite(output_path, filtered_image)

if __name__ == "__main__":
    # Replace 'input_image.jpg' with the path to your input image
    input_image_path = 'input_image.jpg'

    # Replace 'output_image_contra_harmonic.jpg' with the desired output path
    output_image_path = 'output_image_contra_harmonic.jpg'

    # Set the filter size (must be an odd number)
    filter_size = 3

    # Set the Q parameter (positive for reducing salt-and-pepper noise, negative for reducing Gaussian noise)
    Q = 1

    # Apply the contra-harmonic mean filter
    contra_harmonic_mean_filter(input_image_path, output_image_path, filter_size, Q)

    print("Contra-harmonic mean filter applied successfully. Output saved to:", output_image_path)
