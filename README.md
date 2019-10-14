# ASCII Creator

ASCII Creator is a way to create ASCII text art from image , written in python.

## Installation

You need numpy and opencv in order to  run this.

```bash
pip install numpy opencv-python
```

## Usage

```bash
python ASCII.py --file FilePath
```
Additional options:

- -h --help ==  help 
- --cols number(int) = set the number of colums 
- --scale number(float) =  set the aspect ratio
- --out name(file name) = file name for out file txt
- --moreGray = Crisper ASCII art as larger greyscale range ramp is taken

Example

```bash
python ASCII.py --file ubuntu.png --cols 100 --moreGray
```

![cmd output](https://github.com/Blaze2305/ASCII-art/blob/master/Example-Ubuntu.png)


