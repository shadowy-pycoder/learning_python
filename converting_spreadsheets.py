#!/usr/bin/env python3
# You can use Google Sheets to convert a spreadsheet file into other formats.
# Write a script that passes a submitted file to upload(). Once the spread-
# sheet has uploaded to Google Sheets, download it using downloadAsExcel(),
# downloadAsODS(), and other such functions to create a copy of the spreadsheet
# in these other formats.
import ezsheets
import sys
import os


def ss_converter():
    print('Usage: app.py <path/to/existing/spreadsheet>')
    sys.exit(1)


if len(sys.argv) < 2:
    ss_converter()


filename = sys.argv[1]
if not filename.endswith('xlsx'):
    ss_converter()
elif not os.path.exists(filename):
    ss_converter()

print('Uploading', filename)
ss = ezsheets.upload(filename)
methods = [ss.downloadAsExcel, ss.downloadAsODS, ss.downloadAsCSV,
           ss.downloadAsTSV, ss.downloadAsPDF, ss.downloadAsHTML]
for method in methods:
    print('Downloading', filename, method.__name__[10:], 'version')
    method()
