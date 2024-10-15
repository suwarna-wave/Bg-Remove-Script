from rembg import remove
from PIL import Image

def remove_background(input_path, output_path):
    try:
        # Open the input image
        input_image = Image.open(input_path)
        
        # Remove the background
        output_image = remove(input_image)
        
        # Save the output image
        output_image.save(output_path)
        print(f"Background removed and saved to {output_path}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Actual paths
input_path = "D:\\Python stuffs\\Script to remove bg\\suwarnac.png"
output_path = "D:\\Python stuffs\\Script to remove bg\\suwarnac_removed_bg.png"

# Example usage
remove_background(input_path, output_path)
