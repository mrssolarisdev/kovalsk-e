import cv2
import logging

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
    contoured_image = cv2.imread(contoured_image_path)
    # We will cut the objects found in the specific positions in the contoured image, from the original one, so that we don't bring the contours.
    original_image = cv2.imread(original_image_path)

    # Converting to gray to find the contours easier.
    gray = cv2.cvtColor(contoured_image, cv2.COLOR_BGR2GRAY)
    # Getting the binary
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # Finding the contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    logging.info(f"{len(contours)} objects found, writting objects..")
    for i, cnt in enumerate(contours):
        # Positions of the found contoured object
        x, y, w, h = cv2.boundingRect(cnt)
        # Cropping the object from the original image, but using the found positions from the contoured one.
        crop = original_image[y:y+h, x:x+w]
        # Writting the object into an image.
        cv2.imwrite(f"{save_into}/sticker{i}.png", crop)
