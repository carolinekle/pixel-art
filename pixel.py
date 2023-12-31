from skimage import io
from pyxelate import Pyx

# load image with 'skimage.io.imread()'
image = io.imread("eyes.jpg")  

downsample_by = 10  # new image will be 1/14th of the original in size
palette = 5  # find 7 colors
dither = "floyd"

# 1) Instantiate Pyx transformer
pyx = Pyx(factor=downsample_by, palette=palette, dither=dither)

# 2) fit an image, allow Pyxelate to learn the color palette
pyx.fit(image)

# 3) transform image to pixel art using the learned color palette
new_image = pyx.transform(image)

# save new image with 'skimage.io.imsave()'
io.imsave("pixel.png", new_image)