import cv2
import numpy as np
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


def add_gray_noise_to_image(image, mean=0, stddev=25):
    # Adds gray noise to a cv2 image with the specified mean and stddev
    # Load the image
    image = image.astype(np.float32)

    # Generate gray noise with the same shape as the image
    gray_noise = np.random.randint(low=mean - stddev, high=mean + stddev + 1, size=image.shape).astype(np.float32)

    # Add the gray noise to the image
    noisy_image = cv2.add(image, gray_noise)

    # Clip values to the valid range
    noisy_image = np.clip(noisy_image, 0, 255)

    # Convert back to uint8
    noisy_image = noisy_image.astype(np.uint8)
    return noisy_image


def add_median_color_noise_to_image(image, stddev=25, scale=0.5):
    # Adds noise to a cv2 image with the color of the median color of the image and the specified stddev

    # Calculate the median color of the image
    median_color = np.median(image, axis=(0, 1))

    # Generate noise with the same shape as the image
    noise = np.random.normal(loc=0, scale=stddev, size=image.shape).astype(np.float32)

    # Add the median color to the noise to maintain the color consistency and scale it
    colored_noise = scale * (noise + median_color)

    # Add the colored noise to the image
    noisy_image = image + colored_noise

    # Clip values to the valid range
    noisy_image = np.clip(noisy_image, 0, 255)

    # Convert back to uint8
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


def add_white_brush_with_alpha(image):
    # Create a white brush with alpha
    brush_color = (255, 255, 255)
    alpha = 0.05

    # Create a transparent white brush
    brush = np.zeros_like(image, dtype=np.uint8)
    brush[:] = brush_color
    brush = (alpha * brush).astype(np.uint8)

    # Add the brush to the entire image
    image = cv2.addWeighted(image, 1 - alpha, brush, alpha, 0)
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


def add_copyright_text(background_img):
    overlay_img = cv2.imread("../resources/Copyright.png", cv2.IMREAD_UNCHANGED)

    scale_percent = max(background_img.shape[0] / overlay_img.shape[0], background_img.shape[1] / overlay_img.shape[1]) + 50
    width = int(overlay_img.shape[1] * scale_percent / 100)
    height = int(overlay_img.shape[0] * scale_percent / 100)
    dim = (width, height)
    overlay_img = cv2.resize(overlay_img, dim, interpolation=cv2.INTER_AREA)

    # Extract the alpha channel from the overlay image
    alpha_channel = overlay_img[:, :, 3]

    # Invert the alpha channel to create a mask
    mask = cv2.bitwise_not(alpha_channel)

    # Define the position to paste the overlay image
    y_offset = 10
    x_offset = 10

    # Region of interest (ROI) in the background image
    roi = background_img[y_offset:y_offset + overlay_img.shape[0], x_offset:x_offset + overlay_img.shape[1]]

    # Use the mask to create the inverse of the overlay
    background_roi = cv2.bitwise_and(roi, roi, mask=mask)

    # Use the alpha channel to extract the overlay
    overlay_roi = cv2.bitwise_and(overlay_img[:, :, 0:3], overlay_img[:, :, 0:3], mask=alpha_channel)

    # Add the background ROI and overlay ROI to get the final result
    result = cv2.add(background_roi, overlay_roi)

    # Update the background image with the result
    background_img[y_offset:y_offset + overlay_img.shape[0], x_offset:x_offset + overlay_img.shape[1]] = result

    return background_img


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

    exif_ifd = {piexif.ExifIFD.UserComment: 'Author: Max Mustermann'.encode()}

    exif_dict = {"0th": {}, "Exif": exif_ifd, "1st": {},
                 "thumbnail": None, "GPS": {}}

    exif_dat = piexif.dump(exif_dict)
    image.save(path, exif=exif_dat)


def use_alog_on_image(image):
    #TODO: COPYRIGHT_TEXT
    """
    This function applies modifications (such as blur and noise) to an image, adds fake metadata,
    and evaluates both the original and the modified images. The function calculates
    and prints the time taken for the image modification operations.
    """
    # print_image_metadata(path)
    modified_image = make_dark_pixels_brighter(image, 5, 100)
    modified_image = add_gray_noise_to_image(modified_image,  10, 25)
    modified_image = add_noise_to_image(modified_image, 10, 20)
    modified_image = add_white_brush_with_alpha(modified_image)
    modified_image = light_sharpening(modified_image)
    #modified_image = add_copyright_text(modified_image)
    # modified_image = add_blur_to_image(modified_image, 5)
    return modified_image


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

def test_main():
    path = "/Users/loukielhorn/Library/Mobile Documents/com~apple~CloudDocs/Studium/3. Semester/Programmier-Challenge/Ai-Generated-Images/old_car.jpg"
    image = cv2.imread(path)
    modified_image = use_alog_on_image(image)
    image_name = os.path.basename(path)
    print("New image scores from " + image_name + ":")
    get_ai_image_scores(save_image(modified_image))


if __name__ == '__main__':
    test_main()
