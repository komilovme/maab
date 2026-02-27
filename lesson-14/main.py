import numpy as np
from PIL import Image
import os

# ==========================================================
# TASK 1 — Fahrenheit → Celsius with numpy.vectorize
# ==========================================================

def fahrenheit_to_celsius(F):
    return (F - 32) * 5 / 9

temps_f = np.array([32, 68, 100, 212, 77])

vectorized_convert = np.vectorize(fahrenheit_to_celsius)
temps_c = vectorized_convert(temps_f)

print("Task 1 - Celsius values:\n", temps_c)


# ==========================================================
# TASK 2 — Custom Power Function with vectorize
# ==========================================================

def power_function(number, power):
    return number ** power

numbers = np.array([2, 3, 4, 5])
powers = np.array([1, 2, 3, 4])

vectorized_power = np.vectorize(power_function)
power_results = vectorized_power(numbers, powers)

print("\nTask 2 - Power results:\n", power_results)


# ==========================================================
# TASK 3 — Solve Linear System
# ==========================================================

A3 = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
])

b3 = np.array([7, 4, 5])

solution3 = np.linalg.solve(A3, b3)

print("\nTask 3 - Solution (x, y, z):\n", solution3)


# ==========================================================
# TASK 4 — Electrical Circuit Currents
# ==========================================================

A4 = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])

b4 = np.array([12, -5, 15])

solution4 = np.linalg.solve(A4, b4)

print("\nTask 4 - Currents (I1, I2, I3):\n", solution4)


# ==========================================================
# IMAGE MANIPULATION SECTION
# ==========================================================

IMAGE_PATH = "images/birds.jpg"


def flip_image(img_array):
    """Flip horizontally and vertically"""
    flipped_horizontal = np.fliplr(img_array)
    flipped_vertical = np.flipud(img_array)
    return flipped_horizontal, flipped_vertical


def add_noise(img_array, noise_level=30):
    """Add random noise"""
    noise = np.random.randint(-noise_level, noise_level, img_array.shape)
    noisy_img = img_array.astype(np.int16) + noise
    return np.clip(noisy_img, 0, 255).astype(np.uint8)


def brighten_channels(img_array, value=40):
    """Increase brightness of red channel"""
    bright_img = img_array.copy().astype(np.int16)
    bright_img[:, :, 0] += value  # Red channel
    return np.clip(bright_img, 0, 255).astype(np.uint8)


def apply_mask(img_array, mask_size=100):
    """Apply black rectangle mask in center"""
    masked_img = img_array.copy()
    h, w, _ = masked_img.shape

    center_h = h // 2
    center_w = w // 2

    start_h = center_h - mask_size // 2
    end_h = center_h + mask_size // 2
    start_w = center_w - mask_size // 2
    end_w = center_w + mask_size // 2

    masked_img[start_h:end_h, start_w:end_w] = [0, 0, 0]

    return masked_img


def process_image():
    if not os.path.exists(IMAGE_PATH):
        print("\nImage not found:", IMAGE_PATH)
        return

    # Read image
    image = Image.open(IMAGE_PATH)
    img_array = np.array(image)

    # Flip
    flip_h, flip_v = flip_image(img_array)
    Image.fromarray(flip_h).save("flipped_horizontal.jpg")
    Image.fromarray(flip_v).save("flipped_vertical.jpg")

    # Add noise
    noisy = add_noise(img_array)
    Image.fromarray(noisy).save("noisy.jpg")

    # Brighten red channel
    bright = brighten_channels(img_array)
    Image.fromarray(bright).save("brightened.jpg")

    # Apply mask
    masked = apply_mask(img_array)
    Image.fromarray(masked).save("masked.jpg")

    print("\nImage processing complete. Files saved.")


# ==========================================================
# MAIN
# ==========================================================

if __name__ == "__main__":
    process_image()