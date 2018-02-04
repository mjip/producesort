import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from math import sqrt

from skimage.feature import blob_dog
from skimage import io, feature, color
from skimage.color import rgb2gray
from scipy import ndimage
from copy import deepcopy

im = io.imread('rot.jpg')
im2 = deepcopy(im)

#got rid of red, combined blue + green
im[:,:,0] = 0
im_grey = rgb2gray(im)
im_grey = ndimage.gaussian_filter(im_grey, 2)

# Compute the Canny filter for two values of sigma
# image must be 2d

edges2 = feature.canny(im_grey, sigma=3)

mask2 = ndi.binary_fill_holes(edges2) 

im_edges2 = deepcopy(im2)

for x in range(mask2.shape[0]):
	for y in range(mask2.shape[1]):
		if (mask2[x,y] == 0):
			im_edges2[x,y] = im[x,y] * mask2[x,y]


def in_range(x, y):
	# 40% hard coded
	centerx = mask2.shape[0]/2
	centery = mask2.shape[1]/2
	realx = abs(x-centerx)
	realy = abs(y-centery)
	if (realx**2 + realy**2 < (0.5*centerx)**2):
		return True
	else:
		return False



im_edges2 = rgb2gray(im_edges2)

blobs_dog = blob_dog(im_edges2, min_sigma=2, threshold=0.6)
blobs_dog[:, 2] = blobs_dog[:, 2] * sqrt(2)

blobs_list = [blobs_dog]

colors = ['lime']
titles = ['Difference of Gaussian']
sequence = zip(blobs_list, colors, titles)

fig, ax = plt.subplots(1, 1, figsize=(9, 3), sharex=True, sharey=True,
                         subplot_kw={'adjustable': 'box-forced'})

for (blobs, color, title) in (sequence):
    ax.set_title(title)
    ax.imshow(im2, interpolation='nearest')
    for blob in blobs:
        y, x, r = blob
        c = plt.Circle((x, y), r, color=color, linewidth=2, fill=False)
        if (in_range(x,y)):
        	ax.add_patch(c)
    ax.set_axis_off()


plt.tight_layout()
plt.show() 
