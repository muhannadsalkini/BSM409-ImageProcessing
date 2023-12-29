import cv2
import numpy as np

def bit_plane_slice(image, bit):
    # Extract the bit-plane from the image
    bit_plane = (image >> bit) & 1
    # Multiply by 255 to convert to grayscale
    bit_plane *= 255
    return bit_plane.astype(np.uint8)

def main():
    # Read an image
    image_path = 'path/to/your/image.jpg'
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image is loaded successfully
    if image is None:
        print(f"Error: Unable to read the image at {image_path}")
        return

    # Get the number of bits in the image
    num_bits = 8

    # Display the original image
    cv2.imshow('Original Image', image)

    # Perform bit-plane slicing and display each bit-plane
    for bit in range(num_bits):
        bit_plane = bit_plane_slice(image, bit)
        cv2.imshow(f'Bit-Plane {bit}', bit_plane)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
