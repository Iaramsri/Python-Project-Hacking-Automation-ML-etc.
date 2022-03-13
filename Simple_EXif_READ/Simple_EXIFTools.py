from multiprocessing import Value
import os
import sys
from PIL import *
from PIL import Image
from PIL.ExifTags import GPSTAGS, TAGS
import tkinter as tk
from tkinter import filedialog
#from tkinter import *

root = tk.Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()
cwd = os.getcwd()
os.chdir(os.path.join(cwd, folder_selected))
files = os.listdir(folder_selected)
#uncomment print(folder_selected) to see directorty path (folder path)
#print(folder_selected)
#uncomment print(files) to see list of files in folder
#print(files)

if len(files) == 0:
    print("You don't have any files in folder.")
    exit()

print(
    '''
    ███████╗██╗███╗   ███╗██████╗ ██╗     ███████╗    ███████╗██╗  ██╗██╗███████╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗           
    ██╔════╝██║████╗ ████║██╔══██╗██║     ██╔════╝    ██╔════╝╚██╗██╔╝██║██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝           
    ███████╗██║██╔████╔██║██████╔╝██║     █████╗      █████╗   ╚███╔╝ ██║█████╗         ██║   ██║   ██║██║   ██║██║     ███████╗           
    ╚════██║██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝      ██╔══╝   ██╔██╗ ██║██╔══╝         ██║   ██║   ██║██║   ██║██║     ╚════██║           
    ███████║██║██║ ╚═╝ ██║██║     ███████╗███████╗    ███████╗██╔╝ ██╗██║██║            ██║   ╚██████╔╝╚██████╔╝███████╗███████║           
    ╚══════╝╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝    ╚══════╝╚═╝  ╚═╝╚═╝╚═╝            ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝           
                                                                                                                                       
    ██████╗ ██╗   ██╗    ██╗████████╗████████╗██╗  ██╗██╗██████╗ ███████╗     ██╗     █████╗ ██████╗  █████╗ ███╗   ███╗███████╗██████╗ ██╗
    ██╔══██╗╚██╗ ██╔╝    ██║╚══██╔══╝╚══██╔══╝██║  ██║██║██╔══██╗██╔════╝     ██║    ██╔══██╗██╔══██╗██╔══██╗████╗ ████║██╔════╝██╔══██╗██║
    ██████╔╝ ╚████╔╝     ██║   ██║      ██║   ███████║██║██║  ██║█████╗       ██║    ███████║██████╔╝███████║██╔████╔██║███████╗██████╔╝██║
    ██╔══██╗  ╚██╔╝      ██║   ██║      ██║   ██╔══██║██║██║  ██║██╔══╝  ██   ██║    ██╔══██║██╔══██╗██╔══██║██║╚██╔╝██║╚════██║██╔══██╗██║
    ██████╔╝   ██║       ██║   ██║      ██║   ██║  ██║██║██████╔╝███████╗╚█████╔╝    ██║  ██║██║  ██║██║  ██║██║ ╚═╝ ██║███████║██║  ██║██║
    ╚═════╝    ╚═╝       ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝ ╚════╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝
    '''
)

while True:
    choice = input("1 - File.txt\n2 - Terminal\n\nEnter your choice here: ")
    try:
        choice_val = int(choice)
        if choice_val == 1:
            #save .txt in images path you selected
            sys.stdout = open("Exif_data.txt", "w")
            break
        elif choice_val == 2:
            #It default Terminal just break to stop loop
            break
        else:
            #only 2 choice so... no break here to choose choice again
            print("You entered an incorrect option, please try again.")
    except:
        print("You entered an invalid option, please try again.")

#REF https://auth0.com/blog/read-edit-exif-metadata-in-photos-with-python/
def google_maps_url(gps):            
    dec_deg_lat = decimal_degrees(float(gps["lat"][0]),  float(gps["lat"][1]), float(gps["lat"][2]), gps["lat_ref"])
    dec_deg_lon = decimal_degrees(float(gps["lon"][0]),  float(gps["lon"][1]), float(gps["lon"][2]), gps["lon_ref"])
    return f"https://maps.google.com/?q={dec_deg_lat},{dec_deg_lon}"

def decimal_degrees(degree, minutes, seconds, direction):
    decimal_degrees = degree + minutes / 60 + seconds / 3600
    if direction == "S" or direction == "W":
        decimal_degrees *= -1
    return decimal_degrees

for file in files:
    # except wrong file format
    try:
        image = Image.open(file)
        line = "=" * 60
        print(f"{line}{file}{line}")
        gps = {}
        # Check exif data are defined for the image. 
        if image._getexif() == None:
            print(f"{file} contains no exif data.")
        else:
            for tag, val in image._getexif().items():
                tagName = TAGS.get(tag)
                underline = "-" * 60
                if tagName == "GPSInfo":
                    for key, value in val.items():
                        print(f"{GPSTAGS.get(key)} - {value}")
                        print(f"{underline}")
                        if GPSTAGS.get(key) == "GPSLatitude":
                            gps["lat"] = value  
                        elif GPSTAGS.get(key) == "GPSLongitude":
                            gps["lon"] = value                     
                        elif GPSTAGS.get(key) == "GPSLatitudeRef":
                            gps["lat_ref"] = value
                        elif GPSTAGS.get(key) == "GPSLongitudeRef":
                            gps["lon_ref"] = value 
                else:
                    print(f"{tagName} - {val}")
                    print(f"{underline}")
            if gps:
                print(google_maps_url(gps))
    except IOError:
        print("")
