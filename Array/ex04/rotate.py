from load_image import ft_load
from matplotlib import pyplot as plt
import numpy as np


def ft_rotate(arr: np.ndarray) -> np.ndarray:
    """
    Rotates an array transposed
    """
    assert isinstance(arr, np.ndarray), "ft_slice - Not an array"
    print(f"New shape after Transpose: {arr.shape}")
    return np.asarray(
            [
                [arr[j][i] for j in range(len(arr))]
                for i in range(len(arr[0]))
            ]
        )


def main():
    """
    Loads an image, print some information about it and display
    it after "zooming".
    • The size in pixel on both X and Y axis.

    • The number of channel.

    • The pixel content of the image.

    • Display the scale on the x and y axis on the image.
    """
    try:
        data = ft_load("../images/animal.jpeg")
        print(data)
        data = ft_rotate(data)
        print(data)
        plt.imshow(data, interpolation='nearest')
        plt.show()
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
