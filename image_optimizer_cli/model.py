import PIL
from PIL import Image
import os


def resize(input_path, output_path, fixed_height, fixed_width, quality):

    # Get all image names from the directory
    images = os.listdir(input_path)

    if len(images) == 0:
        return "Provided folder is empty!"

    # Loop through the directory with all images
    for image in images:

        # We use the image name later for printing the file size reduction in %
        full_image_name = image

        # Get only the file name without extension
        image_name = image.split('.', 1)[0]

        try:

            size_old = os.stat(input_path + image).st_size
            image = Image.open(input_path+image)

            # Check if both options are set
            if fixed_height and fixed_width:

                image = image.resize(
                    (fixed_width, fixed_height), PIL.Image.BICUBIC)

            # Calculate the corresponding height if only width is set
            elif fixed_width:

                width_percent = (fixed_width / float(image.size[0]))
                height_size = int(float(image.size[1]) * float(width_percent))
                image = image.resize(
                    (fixed_width, height_size), PIL.Image.BICUBIC)

            # Calculate the corresponding width if only height is set
            elif fixed_height:

                height_percent = (fixed_height / float(image.size[1]))
                width_size = int(
                    float(image.size[0]) * float(height_percent))
                image = image.resize(
                    (width_size, fixed_height), PIL.Image.BICUBIC)
            else:
                pass

            # Save the resized image
            image.save(output_path+image_name + '.webp',
                       'webp', optimize=True, quality=quality)

            size_new = os.stat(output_path + image_name + '.webp').st_size
            reduction_in_percent = (
                float((size_old - size_new) / size_old)*100).__round__(2)
            print(
                f"Files size reduced by {reduction_in_percent}% of {full_image_name}!")

        except Exception as e:
            print(e)
