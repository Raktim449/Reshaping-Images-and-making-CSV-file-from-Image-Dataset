import csv
from PIL import Image
import os

fields = ["Image", "Word"]
rows = []
file2 = "train.csv"

file1 = open('words.txt', 'r')
Lines = file1.readlines()
file1.close()
for line in Lines:
    l1 = line.split()
    img_name = l1[0]
    l2 = img_name.split("-")
    img_name = img_name + ".png"
    img_src_path = "words\\" + l2[0] + "\\" + l2[0] + "-" + l2[1] + "\\" + img_name
    img_des_path = "train\\" + img_name
    img_word = l1[-1]
    if(("." not in  img_word) and ("<" not in img_word) and (">" not in img_word) and ("," not in img_word) and ("?" not in img_word) and (";" not in img_word) and ("\'" not in img_word) and ("\"" not in img_word) and ("\\" not in img_word) and ("/" not in img_word) and ("{" not in img_word) and ("}" not in img_word) and ("[" not in img_word) and ("]" not in img_word) and ("(" not in img_word) and (")" not in img_word) and ("_" not in img_word) and ("-" not in img_word) and ("+" not in img_word) and ("=" not in img_word) and ("!" not in img_word) and ("@" not in img_word) and ("#" not in img_word) and ("$" not in img_word) and ("%" not in img_word) and ("^" not in img_word) and ("*" not in img_word) and ("&" not in img_word) and ("1" not in img_word) and ("2" not in img_word) and ("3" not in img_word) and ("4" not in img_word) and ("5" not in img_word) and ("6" not in img_word) and ("7" not in img_word) and ("8" not in img_word) and ("9" not in img_word) and ("0" not in img_word) and ("|" not in img_word) and (":" not in img_word)):
       if os.path.isfile(img_src_path):
           if os.path.getsize(img_src_path)>0:
               img = Image.open(img_src_path)
               re_img = img.resize((320, 240), Image.ANTIALIAS)
               re_img.save(img_des_path)        
               data = [img_name, img_word]
               rows.append(data)

with open(file2, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)