from PIL import Image

# Open an image
image = Image.open("web_colors\\post_gold.png")

# Get the color of a pixel at a specific location (x, y)
pixel_color = image.getpixel((3,3))
print("Pixel color at (x, y):", pixel_color)