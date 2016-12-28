# -*- coding: UTF-8 -*-
'''
This code generate document image and putt altogether in picle file

'''
import numpy as np
import cv2
import codecs,subprocess,os,sys,glob
import random
random.seed()
import h5py
import ipdb
import pickle
def createData(start,count):
        annfile = open('words.txt','r')
        words = annfile.read().split()
        numsamples = len(words)
        # Write some Text
        font = cv2.FONT_HERSHEY_SIMPLEX
        imgWidth=598
        imgHeight=838
        inputs = []
        bBox=[]
        for i in range(start,(start+count)):
                img = cv2.imread('bac.png',cv2.IMREAD_GRAYSCALE)
                textSize = cv2.getTextSize(words[i], font,1, 1);
                width = textSize[0][0]
                height = textSize[0][1]
                x=random.randint(30, (imgWidth-width-5))
                y=random.randint(30, imgHeight-height-5)
                if (x+width>=imgWidth):
                        print "poyimone",i,words[i]
                cv2.putText(img,words[i],(x,y), font, 1,(random.randint(1, 100)),2)
                #cv2.rectangle(img,(x,y-height),(x+width,y), (255,0,255),1)
                img1D=img.reshape(imgWidth*imgHeight)
                inputs.append(img1D.T)
                bBox.append((x,y-height,width,height))
        images=np.asarray(inputs)
        labels=np.asarray(bBox)
        annfile.close()
        return images, labels
print('train data creation ...')
train_xy = createData(10000,5000)
print('test data creation ...')
test_xy = createData(20000,1000)
print('validation data creation ...')
valid_xy = createData(30000,1000)
data={'train' : train_xy,
        'test' : test_xy,
        'valid' : valid_xy }

output = open('data.pkl', 'wb')
pickle.dump(data, output)
output.close()

pkl_file = open('data.pkl', 'rb')
data1 = pickle.load(pkl_file)
test =  data1['test'][0].shape
