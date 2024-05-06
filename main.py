from ImageProcess.image_process_algo import ImageModel
from PIL import Image as pil

if __name__ == '__main__':
    # ImageModel.image_file(r"C:\Users\gtush\Desktop\SayaCsv\FirebaseStorage\FirebaseDownloadedImages\1\25\1.webp")
    file_path = r"C:\Users\gtush\Desktop\SayaCsv\FirebaseStorage\FirebaseDownloadedImages\1\25\1.webp"
    img = ImageModel()
    open_image = pil.open(file_path)
    # resized_image = img.resize_image(open_image, 200)
    cropped_image = img.crop_center(open_image,50, 50)
    cropped_image.show()
