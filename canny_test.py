import matplotlib.pyplot as plt
from canny import edge

mask, im_edges = edge("/Users/johanan/Pictures/photos/Screencaps/unknown-1.png")

fig, (ax1, ax3) = plt.subplots(nrows=1, ncols=2, figsize=(8, 3),
                               sharex=True, sharey=True)

ax1.imshow(mask, cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('mask', fontsize=20)


ax3.imshow(im_edges, cmap=plt.cm.gray)
ax3.axis('off')
ax3.set_title('No background, $\sigma=3$', fontsize=20)

fig.tight_layout()

plt.show()
