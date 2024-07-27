import os
from PIL import Image, ExifTags

def resize_and_crop(image_path, output_path, target_size):
    with Image.open(image_path) as img:
        # Ensure EXIF orientation tag is considered
        try:
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break
            exif = img._getexif()
            if exif is not None:
                orientation = exif.get(orientation, 1)
                if orientation == 3:
                    img = img.rotate(180, expand=True)
                elif orientation == 6:
                    img = img.rotate(270, expand=True)
                elif orientation == 8:
                    img = img.rotate(90, expand=True)
        except (AttributeError, KeyError, IndexError):
            # Cases: image don't have getexif
            pass

        img_ratio = img.width / img.height
        target_width, target_height = target_size
        target_ratio = target_width / target_height

        if img_ratio > target_ratio:
            # Image is wider than target
            new_height = target_height
            new_width = int(new_height * img_ratio)
        else:
            # Image is taller than target
            new_width = target_width
            new_height = int(new_width / img_ratio)

        img = img.resize((new_width, new_height), Image.LANCZOS)

        # Crop the center of the image
        left = (new_width - target_width) / 2
        top = (new_height - target_height) / 2
        right = (new_width + target_width) / 2
        bottom = (new_height + target_height) / 2

        img = img.crop((left, top, right, bottom))
        img.save(output_path)

def main():
    directory = input("Enter the directory containing the images: ")
    output_name = input("Enter the base name for the resized images: ")

    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
        return

    output_directory = os.path.join(directory, "resized")
    os.makedirs(output_directory, exist_ok=True)

    target_size = (825, 550)
    images = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    image_count = len(images)

    for idx, image_file in enumerate(images):
        image_path = os.path.join(directory, image_file)
        output_path = os.path.join(output_directory, f"{output_name}-{idx}.jpg")
        resize_and_crop(image_path, output_path, target_size)
        print(f"Resized and saved {image_file} as {output_name}-{idx}.jpg")

    print(f"Processed {image_count} images and saved them in {output_directory}")

if __name__ == "__main__":
    main()

