import os
import shutil
from tkinter.filedialog import askdirectory
import exifread
import datetime
from folder_structure import folder_struc

# MAIN SCRIPT
choice = int(input("Chose the folder structure: \n"
                   "1. YYYY-MM-DD \n"
                   "2. MM-DD \n"
                   "3. YYYY/MM/DD \n"
                   "4. YYYYMMDD \n"))

# Asks for origin and destination folders
origin = askdirectory(title='Select Origin Folder')
destination = askdirectory(title='Select Destination Folder')


def get_exif_date(photo):
    """Get original creation date from EXIF and returns formatted date for
    photos - should work in any OS"""

    with open(photo, 'rb') as ph:
        tags = exifread.process_file(ph, stop_tag="EXIF DateTimeOriginal")
        date_taken = tags["EXIF DateTimeOriginal"]
        datastr = str(date_taken)
        folder = folder_struc(choice, datastr)
        return folder


def get_date_video(video):
    """Get original creation time for videos with 'os.stat' and returns
     formatted date for videos - may not work in non iOS systems"""

    date = os.stat(video)
    c_timestamp = date.st_birthtime
    c_time = datetime.datetime.fromtimestamp(c_timestamp)  # make readable
    str_time = str(c_time)
    folder = folder_struc(choice, str_time)
    return folder


# Iterate files in origin:
for filename in os.listdir(origin):
    f = os.path.join(origin, filename)

    # Picture files (add extensions below as needed)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.raw', '.gif', '.arw', '.nef')):

        if not filename.startswith('.') and os.path.isfile(f):  # Ignore hidden
            # files and checks if filename is an actual file
            real_date = get_exif_date(f)
            folder_name = str(real_date) + '/'
            path = destination + '/' + str(folder_name)

            # Create folder named with real_date if it doesn't exist
            if os.path.exists(path):
                pass
            else:
                os.mkdir(path)

            # Copy files from origin to new directory
            shutil.copy(origin + '/' + filename, path + '/' + filename)
            print(f"{path} / {filename} copied")

    # Video files (add extensions below as needed)
    elif filename.lower().endswith(('.mp4', '.mov')):

        if not filename.startswith('.') and os.path.isfile(f):  # Ignore hidden
            # files and checks if filename is an actual file
            real_date = get_date_video(f)
            folder_name = str(real_date)
            path = destination + '/' + str(folder_name)

            # Create folder named with real_date if it doesn't exist
            if os.path.exists(path):
                pass
            else:
                os.mkdir(path)

            # Copy files from origin to new directory
            shutil.copy(origin + '/' + filename, path + '/' + filename)
            print(f"{path} / {filename} copied")
