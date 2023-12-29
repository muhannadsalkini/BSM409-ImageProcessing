import cv2
import numpy as np

def contrast_stretching(image_path, output_path, min_output=0, max_output=255):
    # Read the input image
    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Get the minimum and maximum pixel values in the original image
    min_original = np.min(original_image)
    max_original = np.max(original_image)

    # Perform contrast stretching
    stretched_image = (original_image - min_original) * ((max_output - min_output) / (max_original - min_original)) + min_output

    # Convert the image to 8-bit unsigned integer type
    stretched_image = np.clip(stretched_image, 0, 255).astype(np.uint8)

    # Save the contrast-stretched image
    cv2.imwrite(output_path, stretched_image)

if __name__ == "__main__":
    # Replace 'input_image.jpg' with the path to your input image
    input_image_path = 'input_image.jpg'
    
    # Replace 'output_image_stretched.jpg' with the desired output path
    output_image_path = 'output_image_stretched.jpg'

    # Specify the desired output range (default is 0 to 255)
    min_output_value = 0
    max_output_value = 255

    # Apply contrast stretching
    contrast_stretching(input_image_path, output_image_path, min_output_value, max_output_value)

    print("Contrast stretching applied successfully. Output saved to:", output_image_path)
