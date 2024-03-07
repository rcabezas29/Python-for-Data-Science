from PIL import Image
import numpy as np
import PIL


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
