import cv2
import numpy as np
import argparse


# gray scale ramp obtained from :
# http://paulbourke.net/dataformats/asciiart/ 

# scale goes from Dark ---- > Bright
gray_ramp1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1\{\}[]?-_+~i!lI;:,\"^`'. "
gray_ramp2 = "@%#*+=-:. "

# Convert the input image to grayscale.
# Split the image into M×N tiles.
# Correct M (the number of rows) to match the image and font aspect ratio.
# Compute the average brightness for each image tile and then look up a suitable ASCII character for each.
# Assemble rows of ASCII character strings and print them to a file to form the final image.


def convertToASCII(file,cols,scale,gray_scale_depth=False,save=False):
    image=cv2.imread(file,0)
    w,h=image.shape

    tile_width=w/cols
    tile_height=tile_width/scale
    rows=int(h/tile_height)

    if(cols>w  or rows>h):
        print("DIMENSIONS TOO SMALL\n Try changing the scale")
        exit(0)

    ascii_string=''

    for j in range(rows):
        y1=int(j*tile_height)
        y2=int((j+1)*tile_height)

        if(j==rows-1):
            y2=h
        # ascii_string.append('')

        for i in range(cols):
            x1=int(i*tile_width)
            x2=int((i+1)*tile_width)

            if(i==cols-1):
                x2=w
            img=image[y1:y2,x1:x2]
            if(img.size !=0):  # needed to check if slice is empty or not as empty slice will return NaN average
                avg=int(np.average(img))
                if(not gray_scale_depth):
                    gray_val=gray_ramp1[int((avg*69)/255)]
                else:
                    gray_val=gray_ramp2[int(avg*9/255)]
                ascii_string+=(gray_val)
            else:
                ascii_string+=''
        ascii_string+=('\n')
    return(ascii_string)


if( __name__=='__main__'):
    desc="Convert your iamge to ASCII art :3"
    parser=argparse.ArgumentParser(description=desc)

    parser.add_argument('--file',dest='Img',required=True)
    parser.add_argument('--scale',dest='scale',required=False)
    parser.add_argument('--out',dest='out',required=False)
    parser.add_argument('--cols',dest='cols',required=False)
    parser.add_argument('--moreGray',dest='grayness',action='store_true',required=False)

    args=parser.parse_args()

    imageFile=args.Img

    if(args.scale):
        scale=float(args.scale)
    else:
        scale=0.43

    if(args.cols):
        col=int(args.cols)
    else:
        col=100

    if(args.out):
        out=True
    else:
        out=False

    #Actual conversion to ASCII
    ascii_string=convertToASCII(imageFile,col,scale,args.grayness,out);

    #print to screen
    if(not out):
        print(ascii_string)
        exit(0)
    else:
    # Write to file
        f=open(args.out+'.txt','w+')
        f.write(ascii_string)
        f.close
        print("Written to file {0}".format(args.out+'.txt'))
    
