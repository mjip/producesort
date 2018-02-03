import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi

from skimage import io, feature, filters, data, color
from skimage.color import rgb2gray
from scipy import ndimage
from copy import deepcopy


# Generate noisy image of a square
#im = np.zeros((128, 128))
#im[32:-32, 32:-32] = 1

#im = ndi.rotate(im, 15, mode='constant')
#im = ndi.gaussian_filter(im, 4)
#im += 0.2 * np.random.random(im.shape)

im = io.imread('img/good/top.jpg')
im2 = deepcopy(im)

#got rid of red, combined blue + green
im[:,:,0] = 0
im_grey = rgb2gray(im)
im_grey = ndimage.gaussian_filter(im_grey, 2)

# Compute the Canny filter for two values of sigma
# image must be 2d

edges2 = feature.canny(im_grey, sigma=3)

mask2 = ndi.binary_fill_holes(edges2)

# Applying mask to original image to subtract background

for c in range(3):
	im_edges2 = im2[:,:,c] * (mask2!=0)

# display results
fig, (ax1, ax3) = plt.subplots(nrows=1, ncols=2, figsize=(8, 2),
                                    sharex=True, sharey=True)

ax1.imshow(im2, cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('noisy image', fontsize=20)


ax3.imshow(im_edges2, cmap=plt.cm.gray)
ax3.axis('off')
ax3.set_title('Canny filter, $\sigma=3$', fontsize=20)

fig.tight_layout()

plt.show()
