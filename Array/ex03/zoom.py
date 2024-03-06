from load_image import ft_load, ft_slice, ft_grey
from matplotlib import pyplot as plt


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
        data = ft_grey(data)
        data = ft_slice(data)
        plt.imshow(data, cmap=plt.get_cmap('gray'))
        plt.show()
        print(data)
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
    except FileNotFoundError:
        print("File not Found")
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
