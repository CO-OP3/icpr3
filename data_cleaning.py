"""
Created on Thu Mar  1 10:42:08 2018

@author: ssy
"""
import os
import cv2 #mac下用：sudo pip install opencv-python==3.3.0.10#
import pandas as pd
import time
from tqdm import tqdm

#建立预处理类,dir输入的是单个jpg文件或txt文件地址#
class data_preprocessing:

    def __init__(self, txt_dir, image_dir, out_txtdir=None, out_image_dir=None):

        self.txt_dir = txt_dir
        self.image_dir = image_dir
        self.out_txtdir = out_txtdir
        self.out_image_dir = out_image_dir

    #去掉尾部带某些char的行#
    def txt_del_char(self, char="###"):

        labels = ["X1", "Y1", "X2", "Y2", "X3", "Y3", "X4", "Y4", "文本"]
        txt_file = open(self.txt_dir, "r+")
        lines = txt_file.read().splitlines()
        newlines = []
        for j in lines:
            wordslist = j.split(",")
            #TB12V4ULXXXXXacXXXXunYpLFXX.txt中包含文本里面有逗号的情况，所以行数增加了，把文本重新合并#
            if len(wordslist) != 9:
                for k in range(9,len(wordslist)):
                    wordslist[8] = wordslist[8] + ","+ wordslist[k]
                wordslist = wordslist[:9]
            #去掉含###的行#
            if char not in wordslist:
                newlines.append(wordslist)
        txt_df = pd.DataFrame(newlines, columns = labels)
        return txt_df

    def output_txt(self, char="###"):

        txt_df = self.txt_del_char(char)
        txt_df.to_excel(self.out_txtdir)


    # 图像预处理 http://www.danvk.org/2015/01/07/finding-blocks-of-text-in-an-image-using-python-opencv-and-numpy.html#
    def pic_process(self, par1, par2):

        #灰度化读入#
        img = cv2.imread(self.image_dir,cv2.IMREAD_GRAYSCALE)
        #提取边缘化图#
        canny = cv2.Canny(img, par1, par2)









#test一下#
if __name__ == "__main__":
    print("cleaning and saving data txt as excels")
    #data_cleaning().delete_char()
else:
    print("data_cleaning.py is being imported into another module")










