from PIL import Image, ImageFont, ImageDraw


def add_watermark_with_logo(input_image_path, output_image_path, watermark_text, logo_path):
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

    # Iterate over each row and column and place a watermark text and logo
    for i in range(3):
        for j in range(4):
            # Calculate the position to place the watermark text in the center of the cell
            text_position = ((col_width * j) + (col_width - draw.textlength(watermark_text, font)) // 2,
                             (row_height * i) + (row_height - font.size) // 2)

            # Draw the watermark text on the image
            draw.text(text_position, watermark_text, font=font, fill=(211, 211, 211))

            # Load and resize the logo
            logo = Image.open(logo_path)
            logo_width = col_width // 8
            logo_height = row_height // 8
            logo_resized = logo.resize((logo_width, logo_height))

            # Calculate the position to place the logo in the center of the cell
            logo_position = ((col_width * j) + (col_width - logo_width) // 2,
                             (row_height * i) + (row_height - logo_height) // 2)

            # Check if logo position overlaps with watermark text
            if (text_position[0] < logo_position[0] + logo_width and
                    text_position[0] + draw.textlength(watermark_text, font) > logo_position[0] and
                    text_position[1] < logo_position[1] + logo_height and
                    text_position[1] + font.size > logo_position[1]):
                # Shift logo downwards if there's overlap
                logo_position = (logo_position[0] - font.size-60, ((row_height * i) + (row_height - font.size) // 2)-10)

            # Paste the logo onto the image
            resize_image.paste(logo_resized, logo_position, logo_resized)

    # Save image with watermark and logo
    resize_image.save(output_image_path)
    resize_image.show()


if __name__ == '__main__':
    # Example
    input_image_path = r"C:\Users\gtush\Desktop\SayaCsv\FirebaseStorage\FirebaseDownloadedImages\45\66\2.webp"
    destination_path = r"C:\Users\gtush\Desktop\water_mark_image\output_image9.png"
    water_mark_text = "SayaCare"
    add_watermark_with_logo(input_image_path, destination_path, water_mark_text,
                            r"C:\Users\gtush\Desktop\water_mark_image\Logo_Grayscale.png")
