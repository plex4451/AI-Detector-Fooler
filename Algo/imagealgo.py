import cv2
import numpy as np
from APIs.ai_image_detector import get_scores


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
    image = cv2.imread(path)
    new = add_noise_to_image(image)
    cv2.imwrite("/Users/loukielhorn/Downloads/output.png", new)
    print("Alog used")
    get_scores("/Users/loukielhorn/Downloads/output.png")


use_alog_on_image("/Users/loukielhorn/Downloads/berries.jpg")
