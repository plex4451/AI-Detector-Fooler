import cv2
import numpy as np
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


def use_alog_on_image(path):
    old_image = cv2.imread(path)
    new_image = add_noise_to_image(old_image, 0, 15)
    print("Alog used")
    get_ai_image_scores(new_image)


use_alog_on_image("/Users/loukielhorn/Downloads/duck.png")
