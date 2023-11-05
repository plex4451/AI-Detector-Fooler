import cv2
import numpy as np
import time
import piexif
from PIL import Image, ExifTags
from APIs.ai_image_detector import get_ai_image_scores


def add_noise_to_image(image, mean=0, stddev=25):
    # Adds noise to a cv2 image with the standard value 25
    # Load the image
    image = image.astype(np.float32)

    # Generate Gaussian noise with the same shape as the image
    gaussian_noise = np.random.normal(mean, stddev, image.shape).astype(np.float32)

    # Add the Gaussian noise to the image
    noisy_image = cv2.add(image, gaussian_noise)
    noisy_image = np.clip(noisy_image, 0, 255)
    noisy_image = noisy_image.astype(np.uint8)
    return noisy_image


def add_blur_to_image(image, strength=35):
    # Adds blur to a cv2 image with the standard value 35
    return cv2.GaussianBlur(image, (strength, strength), 0)


def print_image_metadata(path):
    # Prints all available metadata
    image = Image.open(path)

    # Get all available image metadata
    metadata = image.info

    if metadata:
        for key, value in metadata.items():
            if key == "exif":
                exif_data = image._getexif()
                if exif_data is not None:
                    for tag, value in exif_data.items():
                        tag_name = ExifTags.TAGS.get(tag, tag)
                        if tag_name == 'UserComment':
                            value = value.decode("utf-8")
                        print(f"{tag_name}: {value}")
            else:
                print(f"{key}: {value}")
    else:
        print("This image has no metadata.")


def add_fake_metadata(path):
    # This function adds fake metadata to an image path
    image = Image.open(path)

    exif_ifd = {piexif.ExifIFD.UserComment: 'Author: Lou Kielhorn'.encode()}

    exif_dict = {"0th": {}, "Exif": exif_ifd, "1st": {},
                 "thumbnail": None, "GPS": {}}

    exif_dat = piexif.dump(exif_dict)
    image.save(path, exif=exif_dat)


def use_alog_on_image(path):
    """
    This function applies modifications (such as blur and noise) to an image, adds fake metadata,
    and evaluates both the original and the modified images. The function calculates
    and prints the time taken for the image modification operations.

    Args:
        path (str): The path to the input image.

    Returns:
        None.

    Usage:
        use_alog_on_image('./path_to_your_image.jpg')
    """
    start_time = time.time()
    # print_image_metadata(path)

    modified_image = cv2.imread(path)
    modified_image = add_blur_to_image(modified_image, 5)
    modified_image = add_noise_to_image(modified_image, 0, 25)

    modified_image_path = save_image(modified_image)
    add_fake_metadata(modified_image_path)
    print_image_metadata(modified_image_path)

    # Calculate elapsed time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Algo used in: ", elapsed_time)

    print()
    print("Original image scores:")
    get_ai_image_scores(path)
    print()
    print("New image scores:")
    get_ai_image_scores(modified_image_path)


def save_image(image):
    path = "/Users/loukielhorn/Downloads/output.jpg"
    cv2.imwrite(path, image)
    return path


use_alog_on_image("/Users/loukielhorn/Downloads/breakfast.jpg")
