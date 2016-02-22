import os, sys
from PIL import Image


"""
The main function to turn images into ascii art.
This function takes in a string, which is the filepath to the image
"""
def main(fileImage):

    #These next two lines are for loading the picture into python
    im = Image.open(fileImage).convert("L")
    pix = im.load()

    #Creates an empty list to hold the ascii strings
    pictures = []

    
    #These two for loops loop through the pixels in the image from top-down left-right
    for x in range(im.size[1]):
        for y in range(im.size[0]):
            pictures.append(blackAndWhite(pix[y,x])) #Assign an ascii value to each pixel
        pictures.append("\n") #Add blankspace in string to add new row of ascii characters

    f = open("obama.txt",'wb') #Open the .txt file to write to
    for x in range(len(pictures)): #For each of the rows in the ascii art, write them to file
        f.write(pictures[x])
    
def shading(value):
    if value == 0:
        return "B"
    elif (value > 0) and (value <=25):
        return "W"
    elif (value > 25) and (value <=50):
        return "X"
    elif (value > 50) and (value <=75):
        return "D"
    elif (value > 75) and (value <=100):
        return "A"
    elif (value > 100) and (value <=125):
        return "E"
    elif (value > 125) and (value <=150):
        return "O"
    elif (value > 150) and (value <=175):
        return "["
    elif (value > 175) and (value <=200):
        return "}"
    elif (value > 200) and (value <=225):
        return "~"
    elif (value > 225) and (value <=250):
        return "*"
    else:
        return " "

def wFill(v):
    if v > 120:
        return " "
    else:
        return "W"

def blackAndWhite(v):
    if v == 255:
        return "W"
    elif v == 0:
        return "B"
    else:
        return "G"

def customValueFunction(v):
    #Put in your own code here and replace the return function
    return 1

        
    
