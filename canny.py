from scipy import ndimage as ndi

from skimage import io, feature
from skimage.color import rgb2gray
from skimage.feature import blob_dog
from scipy import ndimage
from copy import deepcopy


def img_open(filename):
        im = io.imread(filename)
        return im


def edge(filename):
        im = img_open(filename)

        # Zeroing red channel, combined blue + green channels into
        # single grayscale channel.
        im[:, :, 0] = 0
        im_grey = ndimage.gaussian_filter(rgb2gray(im), 2)

        # Compute the Canny filter for two values of sigma

        edges = feature.canny(im_grey, sigma=3)

        mask = ndi.binary_fill_holes(edges)
        return mask


def rm_back(mask, filename):
        im = img_open(filename)
        no_back = deepcopy(im)
        for x in range(mask.shape[0]):
                for y in range(mask.shape[1]):
                        if (mask[x, y] == 0):
                                no_back[x, y] = im[x, y] * mask[x, y]
        return no_back


def in_range(x, y, mask):
        # 40% hard coded
        centerx = mask.shape[0]/2
        centery = mask.shape[1]/2
        realx = abs(x-centerx)
        realy = abs(y-centery)
        if(realx**2 + realy**2 < (0.5*centerx)**2):
                return True
        else:
                return False


def blobs(im_no_back):
        im_no_back = rgb2gray(im_no_back)
        blob_list = blob_dog(im_no_back, min_sigma=2, threshold=0.6)
        blob_list[:, 2] = blob_list[:, 2] * 2**0.5
        return [blob_list]
