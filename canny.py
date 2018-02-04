from scipy import ndimage as ndi

from skimage import io, feature
from skimage.color import rgb2gray
from scipy import ndimage
from copy import deepcopy


def edge(filename):
        im = io.imread(filename)

        # Zeroing red channel, combined blue + green channels into
        # single grayscale channel.
        im[:, :, 0] = 0
        im_grey = ndimage.gaussian_filter(rgb2gray(im), 2)

        # Compute the Canny filter for two values of sigma

        edges = feature.canny(im_grey, sigma=3)

        mask = ndi.binary_fill_holes(edges)
        return mask


def rm_back(mask, filename):
        im = io.imread(filename)
        no_back = deepcopy(im)
        for x in range(mask.shape[0]):
                for y in range(mask.shape[1]):
                        if (mask[x, y] == 0):
                                no_back[x, y] = im[x, y] * mask[x, y]
        return no_back
