from PIL import Image as pil


class ImageModel:
    @staticmethod
    def image_file(image_path):
        open_image = pil.open(image_path)
        open_image.show()

    def resize_image(self, open_image, new_width):
        pass
        # width, heigth = open_image.size
        # ratio = heigth / width
        # new_height = int(ratio * new_width)
        # resize_image = open_image.resize((new_width, new_height))
        # return resize_image

    def resize_image(self, open_image, new_width):
        if open_image is None:
            return None  # Return None if the image is not loaded properly
        width, height = open_image.size
        ratio = height / width
        new_height = int(ratio * new_width)
        resize_image = open_image.resize((new_width, new_height))
        return resize_image

    def crop_center(self, open_image, crop_width, crop_height):
        if open_image is None:
            return None  # Return None if the image is not loaded properly

        width, height = open_image.size

        # Calculate the center coordinates dynamically
        center_x = width // 2
        center_y = height // 2

        # Calculate the maximum crop dimensions that fit the whole image
        max_crop_width = min(width, crop_width)
        max_crop_height = min(height, crop_height)

        # Calculate the cropping box boundaries
        left = max(0, center_x - max_crop_width // 2)
        top = max(0, center_y - max_crop_height // 2)
        right = min(width, center_x + max_crop_width // 2)
        bottom = min(height, center_y + max_crop_height // 2)

        # Crop the image without resizing it
        cropped_image = open_image.crop((left, top, right, bottom))

        return cropped_image






