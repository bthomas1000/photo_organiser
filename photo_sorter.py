#!/usr/bin/env python

import exifread
import os
from shutil import copy2

folder_with_files = 'PATH TO FILES TO SORT'
folder_with_folders = 'PATH TO YEAR SEPERATED FOLDERS'

def get_exif(folder_with_files):
    '''Retrieve exif data from photo and add to dict'''
    photos_exif = {}
    count = 0
    for photo in os.listdir(folder_with_files):
        count += 1
        print('Processing ' + photo)
        print(count)
        # Open image file for reading (binary mode)
        f = open(folder_with_files + '/' + photo, 'rb')
        # Return Exif tags
        tags = exifread.process_file(f)
        photos_exif[photo] = tags
    return photos_exif

def main(folder_with_files, folder_with_folders):
    """Main Function"""
    photos_exif = get_exif(folder_with_files)
    photo_date = {}
    for photo_name, exif_info in photos_exif.items():
        for exif_key, exif_value in exif_info.items():
            if exif_key == 'Image DateTime':
               photo_date[photo_name] = exif_value
    
    yr_04 = []
    yr_05 = []
    yr_06 = []
    yr_07 = []
    yr_08 = []
    yr_09 = []
    yr_10 = []
    yr_11 = []
    yr_12 = []
    yr_13 = []
    yr_14 = []
    yr_15 = []
    yr_16 = []
    yr_17 = []
    
    for photo_name, date in photo_date.items():
        print('Organsing ' + photo_name)
        date_string = str(date)
        if '2004' in date_string:
            yr_04.append(photo_name)
        if '2005' in date_string:
            yr_05.append(photo_name)
        if '2006' in date_string:
            yr_06.append(photo_name)
        if '2007' in date_string:
            yr_07.append(photo_name)
        if '2008' in date_string:
            yr_08.append(photo_name)
        if '2009' in date_string:
            yr_09.append(photo_name)
        if '2010' in date_string:
            yr_10.append(photo_name)
        if '2011' in date_string:
            yr_11.append(photo_name)
        if '2012' in date_string:
            yr_12.append(photo_name)
        if '2013' in date_string:
            yr_13.append(photo_name)
        if '2014' in date_string:
            yr_14.append(photo_name)
        if '2015' in date_string:
            yr_15.append(photo_name)
        if '2016' in date_string:
            yr_16.append(photo_name)
        if '2017' in date_string:
            yr_17.append(photo_name)

    for photo in yr_04:
        print('Copying ' + photo)
        copy2(folder_with_files + '/' + photo, folder_with_folders + '/' + '2004/2004 No Album')
    
    for photo in yr_05:
        print('Copying ' + photo)
        copy2(folder_with_files + '/' + photo, folder_with_folders + '/' + '2005/2005 No Album')

    for photo in yr_06:
        print('Copying ' + photo)
        copy2(folder_with_files + '/' + photo, folder_with_folders + '/' + '2006/2006 No Album')

    for photo in yr_07:
        print('Copying ' + photo)
        copy2(folder_with_files + '/' + photo, folder_with_folders + '/' + '2007/2007 No Album')

    for photo in yr_08:
        print('Copying ' + photo)
        copy2(folder_with_files + '/' + photo, folder_with_folders + '/' + '2008/2008 No Album')

    for photo in yr_09:
        print('Copying ' + photo)
        copy2(folder_with_files + '/' + photo, folder_with_folders + '/' + '2009/2009 No Album')

    for photo in yr_10:
        print('Copying ' + photo)
        copy2(folder_with_files + '/' + photo, folder_with_folders + '/' + '2010/2010 No Album')

    for photo in yr_11:
        print('Copying ' + photo)
        copy2(folder_with_files + '/' + photo, folder_with_folders + '/' + '2011/2011 No Album')

    for photo in yr_12:
        print('Copying ' + photo)
        copy2(folder_with_files + '/' + photo, folder_with_folders + '/' + '2012/2012 No Album')

    for photo in yr_13:
        print('Copying ' + photo)
        copy2(folder_with_files + '/' + photo, folder_with_folders + '/' + '2013/2013 No Album')

    for photo in yr_14:
        print('Copying ' + photo)
        copy2(folder_with_files + '/' + photo, folder_with_folders + '/' + '2014/2014 No Album')
    
    for photo in yr_15:
        print('Copying ' + photo)
        copy2(folder_with_files + '/' + photo, folder_with_folders + '/' + '2015/2015 No Album')

    for photo in yr_16:
        print('Copying ' + photo)
        copy2(folder_with_files + '/' + photo, folder_with_folders + '/' + '2016/2016 No Album')

    for photo in yr_17:
        print('Copying ' + photo)
        copy2(folder_with_files + '/' + photo, folder_with_folders + '/' + '2017/2017 No Album')

if __name__ == '__main__':
    main(folder_with_files, folder_with_folders)
