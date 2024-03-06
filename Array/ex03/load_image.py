from PIL import Image
import numpy as np


def ft_grey(array) -> np.ndarray:
    """
    Applies a grey scale filter to the image received.
    """
    assert isinstance(array, np.ndarray), "ft_grey - Not an array"
    assert array.shape[-1] in [3, 4], "ft_grey - Does not have enough channels"
    g = np.dot(array[..., :3], [0.2989, 0.5870, 0.1140])
    return g


def ft_slice(arr: np.array) -> np.ndarray:
    """
    Slice a photo to a 400x400 dimension
    """
    assert isinstance(arr, np.ndarray), "ft_slice - Not an array"
    assert arr.shape > (520, 850), "ft_slice - Smaller array than necessary"
    arr = arr[120:520, 450:850]
    print(f"New shape after slicing: {arr.shape[-1:]} or {arr.shape}")
    return arr


def ft_load(filename: str) -> list:
    """
    Loads an image in jpg or jpeg format and transform
    it into an array.
    """
    img = Image.open(filename)
    numpydata = np.asarray(img)
    print(f"The shape of image is {numpydata.shape}")
    return numpydata
