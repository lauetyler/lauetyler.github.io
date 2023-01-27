from PIL import Image

# Open the image

import os
print("opening image")
file_path = "H:\Coding\Personal\lauetyler.github.io\lightbulb.jpg"
# file_path = os.path.join(os.getcwd(), 'linkedin.png')

print("Trying to retrieve image from: ", file_path)
image = Image.open(file_path)
# print("opening image")
# image = Image.open("linkedin.png")

if image == None:
    print("Image was None")
else:
    # Convert the image to grayscale
    gray_image = image.convert("L")

    # Set a threshold value for black pixels
    threshold = 64

    # Iterate through each pixel in the image
    print("Iterating through pixels")
    for x in range(gray_image.width):
        for y in range(gray_image.height):
            # Get the pixel value at (x, y)
            pixel = gray_image.getpixel((x, y))

            # If the pixel is mostly black (below the threshold)
            if pixel < threshold:
                # Set the pixel to black (0)
                gray_image.putpixel((x, y), 0)

    # Save the modified image
    print("Saving Image")
    gray_image.save("lightbulb_black.jpg")
