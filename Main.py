import matplotlib.pyplot as plt
from canny import edge, rm_back

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

print(filename)

# Generate mask image
mask = edge(filename)

# Using mask, subtract background from image
im_no_back = rm_back(mask, filename)

# blobs = blobs(im_no_back)


# Displaying generated images
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3),
                                    sharex=True, sharey=True)
# Displaying mask
ax1.imshow(mask, cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('Edge mask', fontsize=20)

# Displaying background subtraction
ax2.imshow(im_no_back, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('Background subtracted', fontsize=20)

# Displaying blob detected
# ax3.imshow(blobs, cmap=plt.cm.gray)
# ax3.axis('off')
# ax3.set_title('Blobs selected', fontsize=20)

fig.tight_layout()
plt.show()
