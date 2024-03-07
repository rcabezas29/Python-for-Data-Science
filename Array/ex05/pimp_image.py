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
    g[:, :, 0] = g[:, :, 1]
    g[:, :, 2] = g[:, :, 1]
    return g
