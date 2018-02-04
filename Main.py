import matplotlib.pyplot as plt
from canny import *

from tkinter import filedialog
from tkinter import Tk

# Root for this program
root = Tk()
root.withdraw()
filename = filedialog.askopenfilename(initialdir="./img/",
                                           title="Select file",
                                           filetypes=(("jpeg files", "*.jpg"),
                                                      ("png files", "*.png"),
                                                      ("all files", "*.*")))

root.update()
root.destroy()

print(filename)

mask = edge(filename)

im_no_back = rm_back(mask, filename)

# blobs = blobs(im_no_back)

fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3),
                               sharex=True, sharey=True)

ax1.imshow(mask, cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('Edge mask', fontsize=20)


ax2.imshow(im_no_back, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('Background subtracted', fontsize=20)

# ax3.imshow(blobs, cmap=plt.cm.gray)
# ax3.axis('off')
# ax3.set_title('Blobs selected', fontsize=20)

fig.tight_layout()

plt.show()
