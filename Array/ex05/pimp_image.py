import numpy as np


def ft_invert(array) -> np.array:
    """
    Inverts the color of the image received.
    """
    inverted = 255 - array
    inverted[..., 3:] = array[..., 3:]
    return inverted


def ft_red(array) -> np.array:
    """
    Applies a red filter to the image received.
    """
    r = array.copy()
    r[:, :, 0] = 0
    r[:, :, 1] = 0
    return r


def ft_green(array) -> np.array:
    """
    Applies a green filter to the image received.
    """
    g = array.copy()
    g[:, :, 0] = 0
    g[:, :, 2] = 0
    return g


def ft_blue(array) -> np.array:
    """
    Applies a blue filter to the image received.
    """
    b = array.copy()
    b[:, :, 1] = 0
    b[:, :, 2] = 0
    return b


def ft_grey(array) -> np.array:
    """
    Applies a grey scale filter to the image received.
    """
    g = array.copy()
    for row in g:
        for col in row:
            grey = col.sum() / 3
            col[0] = grey
            col[1] = grey
            col[2] = grey
    return g
