import os
import shutil
from os import path


def writepost(Title,imagelink,description):

    ##Making a duplicate of the format page
    ##Adding the title img and description to the duplicate format file
    
    imagelink = "./{}".format(imagelink)
    fin = open("format.txt", "rt")
    fout = open("out.txt", "wt")
    
    changes = {
        "title1":Title,
        "pic1":imagelink,
        "description1":description
        }

    for line in fin:
        for item,replacement in changes.items():
            if item in line:
                line = line.replace(item,replacement)

        fout.write(line)    
    
    fin.close()
    fout.close()


Title = input("Enter the Title:")
Image = input("Enter the Name of the image with its extension:")
Description = input("Enter the Name of the file with the description:")

writepost(Title,Image,Description)


