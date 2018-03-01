"""
Created on Thu Mar  1 10:42:08 2018

@author: ssy
"""
import os
import pandas as pd
import time
from tqdm import tqdm



class data_cleaning:

    def __init__(self, dir = "dataset/ICPR_text_train_part1_20180211/txt_1000", char = "###"):

        self.dir = dir #输入文件位置#
        self.char = char #删除尾部带char的行#
        self.labels = ["X1", "Y1", "X2", "Y2", "X3", "Y3", "X4", "Y4", "文本"]

    def delete_char(self):

        total_filenames = os.listdir(self.dir)
        for i in tqdm(range(len(total_filenames))):
            filename = self.dir+ "/"+ total_filenames[i]
            openfile = open(filename, "r+")
            lines = openfile.read().splitlines()
            newlines = []
#            print (i)

            for j in lines:
                wordslist = j.split(",")
                #TB12V4ULXXXXXacXXXXunYpLFXX.txt中包含文本里面有逗号的情况，所以行数增加了，把文本重新合并#
                if len(wordslist) != 9:
                    for k in range(9,len(wordslist)):
                        wordslist[8] = wordslist[8] + ","+ wordslist[k]
                    wordslist = wordslist[:9]
                #去掉含###的行#
                if self.char not in wordslist:
                    newlines.append(wordslist)

            df = pd.DataFrame(newlines, columns = self.labels)
            #保存dataframe为excel格式#
            name = total_filenames[i][:-4]+".xls"
            newdir = self.dir[:-8] + "new_txt"
            df.to_excel(newdir+ "/"+ name)
            # print((total_filenames.index(i)+1)/len(total_filenames))



#test一下#
if __name__ == "__main__":
    print("cleaning and saving data txt as excels")
    data_cleaning().delete_char()
else:
    print("data_cleaning.py is being imported into another module")










