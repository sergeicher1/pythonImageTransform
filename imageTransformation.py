# Importing necessary modules from the PIL (Pillow) library
from PIL import Image, UnidentifiedImageError
from PIL.ImageOps import grayscale


def transform_image():
    """
    Transform an image based on user input:
    resizing, rotating, and converting it to grayscale

    This function demonstrates how to handle image files,
    manipulate them using Python, and save
    the results with error handling.
    """
    try:
        #Step 1: Ask the user for input image path
        input_path = input("Enter the path to the input image file: ")
        print("Attempting to open the image...")

        # Try to load the image from the specified path
        image = Image.open(input_path)
        print(f"Image successfully loaded from: {input_path}")
        # Output the original image size
        print(f"Original image dimensions: {image.size}")

        # Step 2: Ask the user for the new size
        # width and height to resize the image
        print("Enter the new size for the image (width and height) as integers.")
        width = int(input("Enter the new width: "))
        height = int(input("Enter the new height: "))
        # Create a tuple for the new dimensions
        new_size = (width, height)

        print(f"Resizing the image to {new_size}...")
        resized_image = image.resize(new_size)
        print("Image resized successfully.")

        # Step 3: Ask the user for the rotation angle

        rotation_angle = int(input("Enter the rotation angle in degrees (e.g., 90 for a 90 rotation: "))
        print(f"Rotating the image by {rotation_angle} degrees...")
        rotated_image = resized_image.rotate(rotation_angle)
        print("Image rotated successfully.")

        # Step 4: Convert the image to grayscale
        print("Converting the image to grayscale...")
        # "L" mode is used to convert to grayscale
        grayscale_image = rotated_image.convert("L")
        print("Image converted to grayscale successfully.")

        # Step 5: Ask the user for the output image path
        output_path = input("Enter the path to save the image: ")
        print(f"Saving the transformed image to: {output_path}...")
        # Save the final image
        grayscale_image.save(output_path)
        print("Image saved successfully!")

    # Handling file not found errors
    except FileNotFoundError:
        print(f"Error: The file not found at path: {input_path}.")

    # Handling errors related to invalid image files
    except UnidentifiedImageError:
        print(f"Error: The image at path: {input_path} is not valid image.")

    # Handling any other unexpected errors
    except Exception as e:
        print(f"An unexpected error occurred: {e}.")

# Call the function to run the program
transform_image()