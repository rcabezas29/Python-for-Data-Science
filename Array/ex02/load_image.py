from PIL import Image
import numpy as np


def ft_load(filename: str) -> list:
    """
    Loads an image in jpg or jpeg format and transform
    it into an array.
    """
    img = Image.open(filename)
    numpydata = np.asarray(img)
    print(f"The shape of image is {numpydata.shape}")
    return numpydata
