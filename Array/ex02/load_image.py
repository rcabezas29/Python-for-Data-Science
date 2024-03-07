import PIL
import numpy as np
from PIL import Image


def ft_load(filename: str) -> list:
    """
    Loads an image in jpg or jpeg format and transform
    it into an array.
    """
    try:
        img = Image.open(filename)
        numpydata = np.asarray(img)
        print(f"The shape of image is {numpydata.shape}")
        return numpydata
    except FileNotFoundError:
        print("File not found")
        return []
    except PIL.UnidentifiedImageError:
        print(f"PIL.UnidentifiedImageError: \
              cannot identify image file '{filename}'")
        return []
