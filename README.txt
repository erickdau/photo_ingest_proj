# photo_ingesting_project

A program to ingest image files with specific folder structures. 

Photographers often use Adobe Lightroom importing module to ingest photos from an external memory to a hard-drive. This program intends to do the same process faster than Lightroom.

Since I'm no programmer, this small script lacks a lot of features, like ingesting every file in a SD card, despite the folder structures created by different brands of cameras. By now, you have to choose each folder you want to ingest.

The script is supposed to ingest photo and video files, according to the extensions added in the program. By default, it works with .png, .jpg, .jpeg, .tiff, .bmp', .raw, .awr and .gif photo formats; and .mov and .mp4 video formats. It's easy to add new formats - there are indications where to add the code on the script. 

There are four folder structures to chose from, created after Lightroom options. These options are coded in a separate file. 

### IMPORTANT ###

I take NO RESPONSIBILITY for script malfunction and any file loss due to its use. I myself double check that every file I need was copied to the destination folder when the script runs with no issues - let alone when it returns some kind of error. So I recommend anyone who uses it to do the same.

Known issues:
1. Copied files update their creation date for the date they were copied. Still working on resolving that.

