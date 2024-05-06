import cv2
from rembg import remove
from PIL import Image


def remove_background(image_path, output_path):
    read_image = Image.open(image_path)
    remove_bg = remove(read_image)
    # Convert the image to grayscale
    remove_bg_gray = remove_bg.convert('L')
    # Apply a threshold to make the background black
    threshold = 128
    remove_bg_bw = remove_bg_gray.point(lambda p: p < threshold and 255)
    remove_bg_bw.show()


if __name__ == '__main__':
    remove_background(r"C:\Users\gtush\Desktop\water_mark_image\Logo.png",
                      r"C:\Users\gtush\Desktop\water_mark_image\log1.png")
