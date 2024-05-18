from PIL import Image

# ASCII characters from dark to light
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def scale_image(image, new_width=100):
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width)
    new_image = image.resize((new_width, new_height))
    return new_image

def convert_to_grayscale(image):
    return image.convert("L")

def map_pixels_to_ascii(image, range_width=25):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value//range_width]
    return ascii_str

def convert_image_to_ascii(image):
    image = scale_image(image)
    image = convert_to_grayscale(image)

    ascii_str = map_pixels_to_ascii(image)
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    return ascii_img

def main(image_path):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    ascii_img = convert_image_to_ascii(image)
    print(ascii_img)

if __name__ == "__main__":
    image_path = input("Enter image path: ")
    main(image_path)
