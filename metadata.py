"""
Approach:
• Import the pillow module.
• Load the image
• Get the metadata. The metadata so obtained
• Convert it into human-readable form

There are many types of metadata but in this we are only focusing on Exif metadata.

Exif
These metadata, often created by cameras and other capture devices, include technical information
about an image and its capture method, such as exposure settings, capture time, GPS location
information and camera model.

NOTE: Whatsapp strips away all metadata from any image.

Implementation:
Step 1: Importing modules.
Step 2: Load the image and extract the exif data.
Step 3: Convert the exif tag id(denoted by tagid in the code) into human readable form denoted
by tagname in the code and getting its respective value.
"""

from PIL import Image
from PIL.ExifTags import TAGS
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk
import os

def selectfile():
    try:
        filename = fd.askopenfilename(initialdir="/", title="Select File to extract", filetypes=(("All Files", "*.*"),("PNG Files", "*.png"),("JPG Files", "*.jpg"),("JPEG Files", "*.jpeg"),))
        image_path_entry.delete(0, "end")
        image_path_entry.insert(0, filename)
    except AttributeError:
        pass

def extract_metadata():
    #open the image
    image = Image.open(image_path_entry.get())
    #extracting the exif metadata
    exifdata = image.getexif()
    img_filename = os.path.splitext(os.path.basename(image_path_entry.get()))[0]
    f = open(img_filename+'_metadata.txt', 'w')

    #looping through all the tags present in exifdata
    for tagid in exifdata:
        #getting teh tag name instead of tag id
        tagname = TAGS.get(tagid, tagid)

        #passing the tagid to get its respective value
        value = exifdata.get(tagid)

        #printing the final result
        f.write(f"{tagname:25}: {value}\n")
    f.close()

metadata = tk.Tk()
metadata.title("Copier")
metadata.geometry("350x150")
metadata.config(bg="#ffffff")

s = ttk.Style()
s.configure('TLabel', background='#ffffff')

ttk.Label(metadata, text="Metadata", padding=10, font=('Helvetica', 24), style="TLabel").grid(column=1, row=0)
metadata.columnconfigure(0, weight = 1)
metadata.rowconfigure(0, weight = 1)

ttk.Label(metadata, text="Select File", padding=10, font=('Helvetica', 14), style="TLabel").grid(column=0, row=1, sticky=tk.W)

image_path_entry = ttk.Entry(metadata)
image_path_entry.grid(column = 1, row = 1, padx=10, sticky=tk.W)

ttk.Button(metadata, text = "Select", cursor="hand2", command = selectfile).grid(column = 2, row = 1, sticky=tk.W, padx=(0,10))
ttk.Button(metadata, text = "Extract", cursor="hand2", command = extract_metadata).grid(column = 1, row = 2, sticky=tk.W+tk.E, padx=10, pady=10)
