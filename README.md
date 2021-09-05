# Reshaping-Images-and-making-CSV-file-from-Image-Dataset
For training Automatic Model we need CSV file of given Image Dataset and need to reshape the images as well. So, this code can be used to reshape the images and make CSV from the given huge Dataset and its Meta Data.


Modules Needed :
1.	OS
2.	CSV
3.	PIL


Setup : 
1.	Input-> Put the Meta Data File (text file) in the same directory where the code file is located and name it “words.txt”. Put the image folder in the same directory and name it “words”.
2.	Output-> Make a empty CSV file with name “train.csv” and empty folder with name “train” in same directory.

From meta data we read the image names and word in the corresponding images. Then check the image is present in “words” folder or not. If present, then reshape the image (320*240) and save it on “train” folder and save the image name and word in image on the “train.csv”
