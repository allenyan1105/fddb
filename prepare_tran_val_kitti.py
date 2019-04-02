import sys, os
import numpy as np
import random
import dircache
from math import *
from PIL import Image
from pathlib import Path

def filterCoordinate(c,m):
	if c < 0:
		return 0
	elif c > m:
		return m
	else:
		return c


 os.system('rm -rf train/images/* ;rm -rf train/labels/*')
 os.system('rm -rf val/images/* ;rm -rf val/labels/*')


train_file_lists = ['FDDB-folds/FDDB-fold-01-ellipseList.txt', 'FDDB-folds/FDDB-fold-02-ellipseList.txt', \
'FDDB-folds/FDDB-fold-03-ellipseList.txt', 'FDDB-folds/FDDB-fold-04-ellipseList.txt', \
'FDDB-folds/FDDB-fold-05-ellipseList.txt', 'FDDB-folds/FDDB-fold-06-ellipseList.txt', \
'FDDB-folds/FDDB-fold-07-ellipseList.txt', 'FDDB-folds/FDDB-fold-08-ellipseList.txt', \
'FDDB-folds/FDDB-fold-09-ellipseList.txt', 'FDDB-folds/FDDB-fold-10-ellipseList.txt']

#with open(ellipse_filename) as f:
#	lines = [line.rstrip('\n') for line in f]

def prepare_train_val(filename, tran_val):

    with open(filename) as f:
        lines = [line.rstrip('\n') for line in f]

    i = 0
    while i < len(lines):
	    img_file = 'FDDB/images/' + lines[i] + '.jpg'
            #print lines[i]
            tokens = lines[i].split('/')
            #print tokens
            f = open(tran_val + '/labels/' + \
                tokens[0] + '-' + tokens[1] + '-' + tokens[2] + '-' + tokens[3] + '-' + tokens[4] + '.txt','a')
 
            my_file = Path(tran_val + '/images/' + tokens[4] + '.jpg')
            if my_file.is_file() == False:
                os.symlink('/home/ubnt/datasets/fddb/FDDB/images/' + lines[i] + '.jpg', \
                    tran_val + '/images/' + tokens[0] + '-' + tokens[1] + '-' + tokens[2] + '-' + tokens[3] + '-' + tokens[4] + '.jpg')

            img = Image.open(img_file)
	    w = img.size[0]
	    h = img.size[1]
	    num_faces = int(lines[i+1])
	    for j in range(num_faces):
		    ellipse = lines[i+2+j].split()[0:5]
		    a = float(ellipse[0])
		    b = float(ellipse[1])
		    angle = float(ellipse[2])
		    centre_x = float(ellipse[3])
		    centre_y = float(ellipse[4])

		    tan_t = -(b/a)*tan(angle)
		    t = atan(tan_t)
		    x1 = centre_x + (a*cos(t)*cos(angle) - b*sin(t)*sin(angle))
		    x2 = centre_x + (a*cos(t+pi)*cos(angle) - b*sin(t+pi)*sin(angle))
		    x_max = filterCoordinate(max(x1,x2),w)
		    x_min = filterCoordinate(min(x1,x2),w)

		    if tan(angle) != 0:
			    tan_t = (b/a)*(1/tan(angle))
		    else:
			    tan_t = (b/a)*(1/(tan(angle)+0.0001))
		    t = atan(tan_t)
		    y1 = centre_y + (b*sin(t)*cos(angle) + a*cos(t)*sin(angle))
		    y2 = centre_y + (b*sin(t+pi)*cos(angle) + a*cos(t+pi)*sin(angle))
		    y_max = filterCoordinate(max(y1,y2),h)
		    y_min = filterCoordinate(min(y1,y2),h)

		    text = "face 0 0 0" + ' '  + str(x_min) + ' ' + str(y_min) + ' ' + str(x_max) + ' ' + str(y_max) + ' ' + '0 0 0 0 0 0 0''\n'
		    f.write(text)

	    i = i + num_faces + 2

    f.close()

train_img_dir = '/home/ubnt/datasets/fddb/train/images/'
train_label_dir = '/home/ubnt/datasets/fddb/train/labels/'
val_img_dir = '/home/ubnt/datasets/fddb/val/images/'
val_label_dir = '/home/ubnt/datasets/fddb/val/labels/'

def prepare_val(num):
    i = 0
    while i < num:
        # choose random file
        filename = random.choice(os.listdir(train_img_dir))
        # print filename
        # move .jpg
        # print train_img_dir + filename
        os.rename(train_img_dir + filename, val_img_dir + filename)
        # move label
        os.rename(train_label_dir + filename.split('.')[0] + '.txt', val_label_dir + filename.split('.')[0] + '.txt')
        i = i + 1

# prepare train data
for file_name in train_file_lists:
    prepare_train_val(file_name, 'train')

# prepare val data: move 500 sets from train data
prepare_val(500)



