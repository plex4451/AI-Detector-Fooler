import cv2
import numpy as np
import time
import piexif
import os
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


def make_dark_pixels_brighter(image, brightness_increase=10, threshold=20):
    # This method creates a black image mask an adds a brightness value to the mask and image
    # This should emulate a camera which makes an image in the dark
    dark_pixel_mask = np.all(image < threshold, axis=2)
    image[dark_pixel_mask] = np.minimum(255, image[dark_pixel_mask] + brightness_increase)
    return image


def light_sharpening(image, kernel_size=(5, 5), sigma=1.0, amount=1.0, threshold=0):
    """Return a sharpened version of the image, using an unsharp mask."""
    blurred = cv2.GaussianBlur(image, kernel_size, sigma)
    sharpened = float(amount + 1) * image - float(amount) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)
    if threshold > 0:
        low_contrast_mask = np.absolute(image - blurred) < threshold
        np.copyto(sharpened, image, where=low_contrast_mask)
    return sharpened


def extreme_sharpening(image):
    # Warning use with caution extreme sharping!
    # Create a sharpening kernel
    kernel = np.array([[-1, -1, -1],
                       [-1,  9, -1],
                       [-1, -1, -1]])

    # Apply the kernel to the image using filter2D
    sharpened_image = cv2.filter2D(image, -1, kernel)

    return sharpened_image


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
    print_image_metadata(path)

    modified_image = cv2.imread(path)
    modified_image = make_dark_pixels_brighter(modified_image, 5, 10)
    modified_image = add_blur_to_image(modified_image, 3)
    modified_image = add_noise_to_image(modified_image, 0, 15)

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


def use_algo_on_folder(folder_path):
    # List all files in the folder
    all_files = os.listdir(folder_path)

    # Filter out only the image files (jpg, png)
    image_files = [file for file in all_files if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Create full paths for each image file
    image_paths = [os.path.join(folder_path, file) for file in image_files]
    for image_path in image_paths:
        use_alog_on_image(image_path)


def save_image(image):
    path = "/Users/loukielhorn/Downloads/output.jpg"
    cv2.imwrite(path, image)
    return path


