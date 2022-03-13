# Simple_ExifTools_python3
  This Simple_ExifTools_python3 can see Image information (If you download Image from socialMedia maybe it already encrypt image information)
**this script use For Education Purpose Only**
## Exif?
  Exif is Exchangeable image file format (officially Exif, according to JEIDA/JEITA/CIPA specifications) is a standard that specifies the formats for images, sound, and ancillary tags used by digital cameras (including smartphones), scanners and other systems handling image and sound files recorded by digital cameras. The specification uses the following existing file formats with the addition of specific metadata tags: JPEG discrete cosine transform (DCT) for compressed image files, TIFF Rev. 6.0 (RGB or YCbCr) for uncompressed image files, and RIFF WAV for audio files (Linear PCM or ITU-T G.711 μ-Law PCM for uncompressed audio data, and IMA-ADPCM for compressed audio data). It is not used in JPEG 2000 or GIF. This standard consists of the Exif image file specification
## What Is Photo Metadata?
Definition, Types, and Relevance
Photo metadata is a set of data describing and providing information about rights and administration of an image.

It allows information to be transported with an image file, in a way that can be understood by other software and human.

The pixels of image files are created by automated capture from cameras or scanners. Metadata is stored in two main places:

Internally – embedded in the image file, in formats such as JPEG, DNG, PNG, TIFF …
Externally – outside the image file in a digital asset management system (DAM) or in a “sidecar” file (such as for XMP data) or an external news exchange format document as specified by the IPTC.
There are 3 main categories of data:

Descriptive – information about the visual content. This may include headline, caption, keywords. Further persons, locations, companies, artwork or products shown in the image . This can be done using free text or codes from a controlled vocabulary or other identifiers.

Rights – identification of the creator, copyright information, credits and underlying rights in the visual content including model and property rights. Further rights usage terms and other data for licensing the use of the image.

Administrative – creation date and location, instructions for the users, job identifiers, and other details.
## Intruction
 - install PIL first
 ```
 pip install pillow
 ```
 - Run simple_Exiftools
 ```
 python3 Simple_EXIFTools.py
 ```
 - Select Images folder

## Select Folder method
```
import os
import sys
from PIL import *
from PIL import Image
from PIL.ExifTags import TAGS
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()
cwd = os.getcwd()
os.chdir(os.path.join(cwd, folder_selected))
files = os.listdir(folder_selected)
```
in this case folder_selected store directory path if you print(folder_selected) it show directory path :
```
C:/Users/boeing/Desktop/New folder
```
and if you print(files) it show list of files in folder :
```
['51712571073_9f48dc36a5_o.jpg', 'boeing.jpg', 'WindowsXP.jpg']
```

## Demo
use command python3 [file.py] then Select folder(in folder that contain images)   
 >> ![exif1](https://user-images.githubusercontent.com/100425084/155878940-59fce713-9368-4baf-94c9-9b6d936b9b11.jpg)

Result
 >> ![exif2](https://user-images.githubusercontent.com/100425084/155879093-591b1ff5-bca5-4d87-b968-579a4bcda296.jpg)

