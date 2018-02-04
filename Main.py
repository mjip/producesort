import matplotlib.pyplot as plt
import numpy as np
from canny import edge, rm_back, blobs, img_open, in_range

from tkinter import filedialog
from tkinter import Tk

# File selector
root = Tk()
root.withdraw()
filename = filedialog.askopenfilename(initialdir="./img/",
                                      title="Select file",
                                      filetypes=(("jpeg files", "*.jpg"),
                                                 ("png files", "*.png"),
                                                 ("all files", "*.*")))
root.update()
root.destroy()

# Generate original image
orig = img_open(filename)

# Generate mask image
mask = edge(filename)

# Using mask, subtract background from image
im_no_back = rm_back(mask, filename)

# Finding blemishes in background-subtracted image
blobs = blobs(im_no_back)


# Displaying input image and output
colors = ['lime']
sequence = zip(blobs, colors)

fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(9, 3),
                                         sharex=True, sharey=True,
                                         subplot_kw={'adjustable':
                                                     'box-forced'})
# Displaying blobs
for (blobs, color) in (sequence):
    ax4.imshow(orig, interpolation='nearest')
    for blob in blobs:
        y, x, r = blob
        c = plt.Circle((x, y), r, color=color, linewidth=2, fill=False)
        if (in_range(x, y, mask)):
            ax4.add_patch(c)
    ax4.set_axis_off()

# Displaying original input image
ax1.imshow(orig, cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('Original Image', fontsize=12)

# Displaying edge mask
ax2.imshow(mask, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('Detected edge mask', fontsize=12)

# Displaying background-subtracted image
ax3.imshow(im_no_back, cmap=plt.cm.gray)
ax3.axis('off')
ax3.set_title('Background subtracted', fontsize=12)

ax4.set_title('Blobs selected', fontsize=12)

fig.tight_layout()

plt.show()

