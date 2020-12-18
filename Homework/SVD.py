import matplotlib.pyplot as plt
import numpy as np
import time

from PIL import Image

la = np.linalg

#Import image
img = Image.open('C://Users//nefle//stat5810hw63.1.jpg')
imggray = img.convert('LA')
plt.figure(figsize=(90, 60))
plt.imshow(imggray);

#convert the image data into a numpy matrix, plot to show img is unchanged
imgmat = np.array(list(imggray.getdata(band=0)), float)
imgmat.shape = (imggray.size[1], imggray.size[0])
imgmat = np.matrix(imgmat)
a = imgmat
plt.figure(figsize=(9,6))
plt.imshow(imgmat, cmap='gray');

#perform SVD on imgmat
U, sigma, V = np.linalg.svd(imgmat)

reconstimg = np.matrix(U[:, :1]) * np.diag(sigma[:1]) * np.matrix(V[:1, :])
plt.imshow(reconstimg, cmap='gray');

print("Singular Values List: ")
for i in range(len(reconstimg)):
    for j in range(len(reconstimg[0])):
        # Condition for principal diagonal
        if (i == j):
            print(reconstimg[i][j], end=", ")
print()

#Now do the same for n = 2,3,4,5
xrange = [1,2,3,4,5,10,35]
for i in xrange:
    reconstimg = np.matrix(U[:, :i]) * np.diag(sigma[:i]) * np.matrix(V[:i, :])
    plt.imshow(reconstimg, cmap='gray')
    title = "n = %s" % i
    # get value of b for error calculation
    c = la.norm(imgmat - reconstimg)
    print("In loop", i, "Error: ", c)
    plt.title(title)
    plt.show()
