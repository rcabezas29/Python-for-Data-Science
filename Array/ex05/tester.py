from load_image import ft_load
from pimp_image import ft_invert, ft_grey, ft_blue, ft_green, ft_red
import matplotlib.pyplot as plt


original = ft_load("../images/landscape.jpg")

plt.imshow(original)
plt.show()

array = ft_invert(original)

plt.imshow(array)
plt.show()

array = ft_red(original)

plt.imshow(array)
plt.show()

array = ft_green(original)

plt.imshow(array)
plt.show()

array = ft_blue(original)

plt.imshow(array)
plt.show()

array = ft_grey(original)

plt.imshow(array)
plt.show()

print(ft_invert.__doc__)
print(ft_red.__doc__)
print(ft_green.__doc__)
print(ft_blue.__doc__)
print(ft_grey.__doc__)
