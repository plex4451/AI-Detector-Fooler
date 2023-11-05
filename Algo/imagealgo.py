import cv2
import numpy as np
import time
from PIL import Image, ExifTags
from APIs.ai_image_detector import get_ai_image_scores


def add_noise_to_image(image, mean=0, stddev=25):
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
    return cv2.GaussianBlur(image, (strength, strength), 0)


def print_image_metadata(path):
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
                            value = value.decode("utf-16")
                        print(f"{tag_name}: {value}")
            else:
                print(f"{key}: {value}")
    else:
        print("This image has no metadata.")


def use_alog_on_image(path):
    start_time = time.time()
    print_image_metadata(path)

    old_image = cv2.imread(path)
    new_image = add_blur_to_image(old_image, 5)
    new_image = add_noise_to_image(new_image, 0, 25)

    # Calculate elapsed time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Algo used in: ", elapsed_time)

    save_image(new_image)

    print()
    print("Original image scores:")
    get_ai_image_scores(old_image)
    print()
    print("New image scores:")
    get_ai_image_scores(new_image)


def save_image(image):
    cv2.imwrite("/Users/loukielhorn/Downloads/output.png", image)


print_image_metadata("/Users/loukielhorn/Downloads/airplane.jpg")
use_alog_on_image("/Users/loukielhorn/Downloads/breakfast.jpg")
