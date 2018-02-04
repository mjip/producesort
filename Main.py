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
                                                      ("all files", "*.*")))

root.update()
root.destroy()

print(filename)

mask = edge(filename)

im_no_back = rm_back(mask, filename)

fig, (ax1, ax3) = plt.subplots(nrows=1, ncols=2, figsize=(8, 3),
                               sharex=True, sharey=True)

ax1.imshow(mask, cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('Edge mask', fontsize=20)


ax3.imshow(im_no_back, cmap=plt.cm.gray)
ax3.axis('off')
ax3.set_title('Background subtracted', fontsize=20)

fig.tight_layout()

plt.show()
