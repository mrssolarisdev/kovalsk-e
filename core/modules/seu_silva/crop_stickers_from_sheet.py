import sys
import time
import zipfile

import cv2
import logging
import numpy as np

def crop_stickers_from_sheet(contoured_image_path: str, original_image_path: str, save_into: str) -> None:
    """
    Gets an image having contoured objects to be identified and saved individually as png files.
    param: contoured_image_path: The image containing the contoured objects.
    param: original_image_path: The original image that doesn't have contoured objects. The 
    identified objects from the contoured image will be cut out from the original one, in order
    to let the contours out.
    param: save_into: Path to the folder in which the new files are going to be saved.
    return: None
    """
    # The image containing the contoured objects makes possible that we find them
    contoured_image = cv2.imread(contoured_image_path, cv2.IMREAD_UNCHANGED)
    # We will cut the objects found in the specific positions in the contoured image, from the original one, so that we don't bring the contours.
    original_image = cv2.imread(original_image_path)
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2BGRA)

    # Converting to gray to find the contours easier.
    gray = cv2.cvtColor(contoured_image, cv2.COLOR_BGR2GRAY)
    # Getting the binary
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # Finding the contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    cv2.drawContours(binary, contours, -1, color=30, thickness=cv2.FILLED)
    # Numpy is implicitly making possible that we use the syntax bellow:
    # Setting every black index as True in the new matrix, and False for every white one.
    black_indexes = binary == 0

    # Masking. The matrix that represents the original image is "overlapped" by the matrix of "Trues" and "Falses"
    # For every True element, the corresponding pixel in the original image is replaced by an array of 4 dimensions:
    # 0 for red, green, blue and alpha. With the alpha being 0, the background is turned from what it was, into transparent. 
    # So, every black pixel in the binary image represents now a transparent pixel in the original one.
    original_image[black_indexes] = [0, 0, 0, 0]
    logging.info(f"{len(contours)} objects found, writting objects..")
    timestamp = time.time()
    with zipfile.ZipFile(f"{save_into}/stickers_zip.zip", mode="w") as stickers_zip:
        for i, cnt in enumerate(contours):
            # Positions of the found contoured object
            x, y, w, h = cv2.boundingRect(cnt)
            # Cropping the object from the original image, but using the found positions from the contoured one.
            crop = original_image[y:y+h, x:x+w]
            # Size of the image
            height, width, _ = crop.shape
            # Writting the object into an image.
            if height > 10 and width > 10:
                # Encoding the subimage as a png one.
                _, buffer = cv2.imencode('.png', crop)
                # Writing the image into the zip.
                stickers_zip.writestr(f"sticker{i}_{timestamp}.png", buffer)

if __name__ == "__main__":
    # Taking off the name of the script and passing in the rest
    crop_stickers_from_sheet(*sys.argv[1:])