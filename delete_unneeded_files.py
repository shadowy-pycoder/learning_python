#!/usr/bin/env python3
# Write a program that walks through a folder tree and searches for excep-
# tionally large files or folders—say, ones that have a file size of more than
# 100MB. (Remember that to get a file’s size, you can use os.path.getsize() from
# the os module.) Print these files with their absolute path to the screen.
import os
import sys


def delete_unneeded_usage():
    print('Usage app.py <path/to/existing/directory> <size in MB>')


if len(sys.argv) < 3:
    delete_unneeded_usage()
    sys.exit(1)

try:
    size_limit = int(sys.argv[2])
except ValueError:
    delete_unneeded_usage()
    sys.exit(1)

path_to_dir = os.path.abspath(sys.argv[1])
if os.path.isdir(path_to_dir):
    for foldername, subfolders, filenames in os.walk(path_to_dir):
        totalSize = 0
        for filename in filenames:
            path_file = os.path.join(foldername, filename)
            try:
                size_in_mb = os.path.getsize(path_file) // (1024*1024)
            except FileNotFoundError:
                continue
            else:
                if size_in_mb > size_limit:
                    print(f'File: {path_file}, {size_in_mb} MB')
                totalSize += size_in_mb
        if totalSize > size_limit:
            print(f'Folder: {foldername}, {totalSize} MB')
else:
    delete_unneeded_usage()
    sys.exit(1)
