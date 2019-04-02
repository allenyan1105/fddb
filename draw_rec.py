
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np

im = np.array(Image.open('FDDB/images/2002/08/11/big/img_591.jpg'), dtype=np.uint8)

# Create figure and axes
fig,ax = plt.subplots(1)

# Display the image
ax.imshow(im)

# Create a Rectangle patch
rect = patches.Rectangle((180.05081678,41.1339610644),359.33598322 - 180.05081678,282.428438936 - 41.1339610644,linewidth=1,edgecolor='w',facecolor='none')
rect1 = patches.Rectangle((174.75, 25.6206),190.25,268.896,linewidth=1,edgecolor='r',facecolor='none')
# Add the patch to the Axes
ax.add_patch(rect)

ax.add_patch(rect1)

plt.show()
