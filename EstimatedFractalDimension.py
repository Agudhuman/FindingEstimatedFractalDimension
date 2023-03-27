import numpy as np
from PIL import Image

filename = 'Concentration_Paint_2.png'  # name of the image file
box_sizes = np.arange(1, 20, 1)  # array of box sizes to use

img = Image.open(filename).convert('L')  # convert image to grayscale
width, height = img.size
area = width * height

num_boxes = 50  # number of boxes to use in each dimension

counts = np.zeros(len(box_sizes))  # array to store box count values
x_min = np.floor(np.linspace(0, width, num_boxes+1)).astype(int)[:-1]
y_min = np.floor(np.linspace(0, height, num_boxes+1)).astype(int)[:-1]
for i in range(len(y_min)-1):
    for j in range(len(x_min)-1):
        for k, box_size in enumerate(box_sizes):
            box = img.crop((x_min[j], y_min[i], x_min[j+1], y_min[i+1]))
            box = box.resize((box_size, box_size))
            if np.sum(np.array(box)) > 0:
                counts[k] += 1

# Fit a line to the log-log plot of box count vs. box size
coeffs = np.polyfit(np.log(box_sizes), np.log(counts), 1)
print(f"Fractal dimension = {coeffs[0]}")
