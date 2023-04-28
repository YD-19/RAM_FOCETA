import pandas as pd
import pybboxes as pbx
# data = pd.read_csv('output_list.txt', header = None)
import numpy as np
import os


path = "data/FOCETA/label/"
wpath = "data/FOCETA/labels/"
files = os.listdir(path)
files.sort()
classes = ['     Car', '   Motor', '   Truck','   Human',' Trailer','DontCare']
s = []
W, H = 1280, 960
for file_ in files:
    if not os.path.isdir(path + file_):
        f_name = str(file_)
        f = open("data/FOCETA/labels/test_name.txt",'w')
        data = pd.read_table(path+f_name, header = None,sep = '\t', engine='python')
        newlabels = []
        for i in range(data.shape[0]):
            voc_bbox_temp = (data.values[i][4],data.values[i][5],data.values[i][6],data.values[i][7])
            label = pbx.convert_bbox(voc_bbox_temp, from_type="voc", to_type="yolo", image_size=(W,H))
            # print(classes.index(data.values[i][0]))
            temp = [classes.index(data.values[i][0]),label[0],label[1],label[2],label[3]]
            newlabels.append(temp)
        
        with open(wpath+f_name, 'w') as f:
            for i in range(len(newlabels)):
                f.write(" ".join(map(str, newlabels[i])) + '\n')

# print(s)
