from PIL import Image, ImageFont, ImageDraw


def add_watermark(input_image_path, output_image_path, watermark_text):
    # Open the input image
    image = Image.open(input_image_path)
    resize_image = image.resize((1000, 1200))

    # Create a drawing context
    draw = ImageDraw.Draw(resize_image)

    # Get the width and height of the image
    width, height = resize_image.size

    # Choose a font and font size for the watermark
    font = ImageFont.truetype("arial.ttf", 30)

    # Calculate the height of each row
    row_height = height // 3

    # Calculate the width of each column
    col_width = width // 4

    # Iterate over each row and column and place a "Care" watermark
    for i in range(3):
        for j in range(4):
            # Calculate the position to place the watermark in the center of the cell
            position = ((col_width * j) + (col_width - draw.textlength(watermark_text, font)) // 2,
                        (row_height * i) + (row_height - font.size) // 2)

            # Draw the watermark text on the image
            draw.text(position, watermark_text, font=font, fill=(211, 211, 211))

    # Save image with the watermark
    resize_image.save(output_image_path)
    resize_image.show()


if __name__ == '__main__':
    # Example
    input_image_path = r"C:\Users\gtush\Desktop\SayaCsv\FirebaseStorage\FirebaseDownloadedImages\45\66\2.webp"
    destination_path = r"C:\Users\gtush\Desktop\water_mark_image\output_image5.png"
    water_mark_text = "SayaCare"
    add_watermark(input_image_path, destination_path, water_mark_text)
