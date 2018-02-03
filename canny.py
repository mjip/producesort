from scipy import ndimage as ndi

from skimage import io, feature
from skimage.color import rgb2gray
from scipy import ndimage
from copy import deepcopy


def edge(filename):
        im = io.imread(filename)
        im_copy = deepcopy(im)

        # Zeroing red channel, combined blue + green channels into
        # single grayscale channel.
        im[:, :, 0] = 0
        im_grey = ndimage.gaussian_filter(rgb2gray(im), 2)

        # Compute the Canny filter for two values of sigma
        # image must be 2d

        edges = feature.canny(im_grey, sigma=3)

        mask = ndi.binary_fill_holes(edges)

        im_edges = im_copy
        for x in range(mask.shape[0]):
                for y in range(mask.shape[1]):
                        if (mask[x, y] == 0):
                                im_edges[x, y] = im[x, y] * mask[x, y]
        return mask, im_edges


# Uncomment below lines to test output

# import matplotlib.pyplot as plt

# mask, im_edges = edge("img/good/top.jpg")

# fig, (ax1, ax3) = plt.subplots(nrows=1, ncols=2, figsize=(8, 3),
#                                     sharex=True, sharey=True)

# ax1.imshow(mask, cmap=plt.cm.gray)
# ax1.axis('off')
# ax1.set_title('mask', fontsize=20)


# ax3.imshow(im_edges, cmap=plt.cm.gray)
# ax3.axis('off')
# ax3.set_title('No background, $\sigma=3$', fontsize=20)

# fig.tight_layout()

# plt.show()
