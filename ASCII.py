import cv2
import numpy as np
import argparse


# gray scale ramp obtained from :
# http://paulbourke.net/dataformats/asciiart/ 
gray_ramp1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`'. "
gray_ramp2 = "@%#*+=-:. "

# Convert the input image to grayscale.
# Split the image into M×N tiles.
# Correct M (the number of rows) to match the image and font aspect ratio.
# Compute the average brightness for each image tile and then look up a suitable ASCII character for each.
# Assemble rows of ASCII character strings and print them to a file to form the final image.


def convertToASCII(file,cols=50,scale=0.43,gray_scale_depth=0):
    image=cv2.imread(file,0)
    w,h=image.shape

    tile_width=w/cols
    tile_height=tile_width/scale
    rows=h//tile_height

    if(cols>w  or rows>h):
        print("DIMENSIONS TOO SMALL\n Try changing the scale")
        exit(0)

    ascii_img=[]

    for j in range(rows):
        y1=int(j*tile_height)
        y2=int((j+1)*tile_height)

        if(j==rows-1):
            y2=h
        ascii_img.append('')

        for i in range(cols):
            x1=int(i*tile_width)
            x2=int((i+1)*tile_width)

            if(i==cols-1):
                x2=w
            img=image[y1:y2,x1:x2]
            avg=int(np.average(img))

            if(not gray_scale_depth):
                gray_val=gray_ramp1[int(avg*69/255)]
            else:
                gray_val=gray_ramp2[int(avg*9/255)]
            ascii_img.append(gray_val)
        ascii_img.append('\n')
    return(ascii_img)
