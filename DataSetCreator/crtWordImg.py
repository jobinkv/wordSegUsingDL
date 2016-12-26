# -*- coding: UTF-8 -*-
import numpy as np
import cv2
import codecs,subprocess,os,sys,glob
import random
random.seed()
import h5py
import ipdb


annfile = open('words.txt','r')
words = annfile.read().split()
numsamples = len(words)
# Write some Text
print numsamples
font = cv2.FONT_HERSHEY_SIMPLEX
ipdb.set_trace()
imgWidth=598
imgHeight=838
inputs = []
bBox=[]
text_file = open("lines.txt", "w")
text_file1 = open("eval.txt", "w")
text_file2 = open("train.txt", "w")
text_file3 = open("valid.txt", "w")
for i in range(10000,23376):
        if i%100 == 0:
                print(i)
        #img = cv2.imread('bac.png',cv2.IMREAD_GRAYSCALE)
        textSize = cv2.getTextSize(words[i], font,1, 1);
        width = textSize[0][0]
        height = textSize[0][1]
        x=random.randint(30, (imgWidth-width-5))
        y=random.randint(30, imgHeight-height-5)
        if (x+width>=imgWidth):
                print "poyimone",i,words[i]
                                                                                                                                 17,1          Top
        '''
        cv2.putText(img,words[i],(x,y), font, 1,(random.randint(1, 100)),2)
        #cv2.rectangle(img,(x,y-height),(x+width,y), (255,0,255),1)
        inputs.append(img)
        bBox.append((x,y-height))
        '''
        cv2.imwrite("img_"+str(i+100000)+".png", img)
        text_file.write("img_"+str(i+100000)+" ok "+str(x)+" "+str(y-height)+" "+str(width)+" "+str(height)+" "+str(imgWidth)+" "+str(imgHeight)+" "+ words[i]+"\n")
        if (i<10336):
                text_file1.write("img_"+str(i+100000)+"\n")
        elif (i>10335 and i<16497):
                text_file2.write("img_"+str(i+100000)+"\n")
        elif (i>16497 and i<16614):
                text_file3.write("img_"+str(i+100000)+"\n")
print len(bBox)
text_file.close()
