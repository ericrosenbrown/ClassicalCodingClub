import os, sys
from PIL import Image

"""
The main function to turn images into ascii art.
This function takes in a string, which is the filepath to the image
"""
class ASCIIart:
    cursor = 0
    quote = "I'm-ready!"
    
    def main(self,fileImage):

        #These next two lines are for loading the picture into python
        im = Image.open(fileImage).convert("L")
        pix = im.load()

        #Creates an empty list to hold the ascii strings
        pictures = []

        
        #These two for loops loop through the pixels in the image from top-down left-right
        for x in range(im.size[1]):
            for y in range(im.size[0]):
<<<<<<< HEAD
                pictures.append(self.shading(pix[y,x])) #Assign an ascii value to each pixel
            pictures.append("\n") #Add blankspace in string to add new row of ascii characters

        f = open("eric.txt",'wb') #Open the .txt file to write to
=======
                pictures.append(self.blackAndWhite(pix[y,x])) #Assign an ascii value to each pixel
            pictures.append("\n") #Add blankspace in string to add new row of ascii characters

        f = open("example.txt",'wb') #Open the .txt file to write to
>>>>>>> 30d020d4ef0598616cc8d69ee42e1b066b0a6f65
        for x in range(len(pictures)): #For each of the rows in the ascii art, write them to file
            f.write(pictures[x])
        
    def shading(self,value):
        if value == 0:
            return "W"
        elif (value > 0) and (value <=25):
            return "B"
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

    def wFill(self,v):
        if v > 120:
            return " "
        else:
            return "W"

    def blackAndWhite(self,v):
        if v == 255:
            return "W"
        elif v == 0:
            return "B"
        else:
            return "G"


    def quoteFill(self,v):
        if v < 120:
            if self.cursor == len(self.quote) - 1:
                self.cursor = 0
            else:
                self.cursor += 1
            return self.quote[self.cursor]
        else:
            return " "
        

    def customValueFunction(self,v):
        #Put in your own code here and replace the return function
        return 1
