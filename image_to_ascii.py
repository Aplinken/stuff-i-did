import sys
from PIL import Image

chars = ["B","S","#","&","@","$","%","*","!",":","."]

def main():
	img = get_image()

	resized_img = resize_image(img)
	resized_img = resized_img.convert('L') # converts image into greyscale format
	
	pixels = convert_into_ascii(resized_img)
	width = 120

	# splits string of chars into multiple strings of length equal to new width and create a list
	pixels_count = len(pixels)
	ascii_image = [pixels[index:index + width] for index in range(0, pixels_count, width)]
	ascii_image = "\n".join(ascii_image)
	print(ascii_image)

	# write to a text file.
	with open("ascii_image.txt", "w") as f:
	 f.write(ascii_image)

def get_image():
	image_path = input("Please enter a valid path to desired image file!\n>")
	try:
		img = Image.open(image_path)
		return img
	except:
		print("Invalid Path")
		return False


def resize_image(image):
	width, height = image.size
	aspect_ratio = height/width
	new_width = 120
	new_height = aspect_ratio * new_width * 0.55
	img = image.resize((new_width, int(new_height)))

	return img

def convert_into_ascii(image):
	# replaces each pixel with a character from array
	pixels = image.getdata()
	converted_pixels = "".join([chars[pixel//25] for pixel in pixels])

	return converted_pixels

main()