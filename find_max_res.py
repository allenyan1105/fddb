import os
import pygame

#path = '/home/ubnt/datasets/ms-coco/train2017'
path = '/home/ubnt/datasets/fddb/train/images'
x_max = 0
y_max = 0
files = []

def find_max_res(xmax, ymax):
    for r, d, f in os.walk(path):
        for file in f:
            if '.jpg' in file:
                files.append(os.path.join(r, file))

    for f in files:
        #print('path: ' + f)
        img = pygame.image.load(f)
        width = img.get_width()
        height = img.get_height()
        if (width > xmax):
            xmax = width
        if (height > ymax):
            ymax = height
        print(xmax)
        print(ymax)

if __name__ == '__main__':
    xmax = 0
    ymax = 0
    find_max_res(xmax, ymax)
    print(xmax)
    print(ymax)
        
