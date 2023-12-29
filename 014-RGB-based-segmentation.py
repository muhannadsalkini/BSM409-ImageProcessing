import cv2
import numpy as np

def segment_image_by_color(image, lower_bound, upper_bound):
    # Convert the image from BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Create a mask based on the specified color range
    mask = cv2.inRange(image_rgb, lower_bound, upper_bound)

    # Apply the mask to extract the segmented region
    segmented_image = cv2.bitwise_and(image, image, mask=mask)

    return segmented_image

def main():
    # Read an image
    image_path = 'path/to/your/image.jpg'
    original_image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if original_image is None:
        print(f"Error: Unable to read the image at {image_path}")
        return

    # Define the color range for segmentation (adjust as needed)
    lower_color_bound = np.array([0, 0, 100], dtype=np.uint8)  # lower bound in RGB
    upper_color_bound = np.array([100, 100, 255], dtype=np.uint8)  # upper bound in RGB

    # Apply segmentation based on color
    segmented_image = segment_image_by_color(original_image, lower_color_bound, upper_color_bound)

    # Display the original and segmented images
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Segmented Image', segmented_image)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
