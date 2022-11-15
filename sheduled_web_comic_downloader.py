#!/usr/bin/env python3
# Write a program that checks the websites of several web comics and auto-
# matically downloads the images if the comic was updated since the pro-
# gram’s last visit. Your operating system’s scheduler (Scheduled Tasks on
# Windows, launchd on macOS, and cron on Linux) can run your Python
# program once a day. The Python program itself can download the comic
# and then copy it to your desktop so that it is easy to find. This will free you
# from having to check the website yourself to see whether it has updated.
# (A list of web comics is available at https://nostarch.com/automatestuff2/.)
# https://www.lefthandedtoons.com/
# https://buttersafe.com/
# https://www.savagechickens.com/
# https://www.lunarbaboon.com/
# https://completelyseriouscomics.com/
# https://www.exocomics.com/
# https://nonadventures.com/
# https://moonbeard.com/
# https://www.happletea.com/
# a for loop that goes trough all websites
# check the date of a posted image, if it is greater than that
# of last visit then download it and place to a folder
# program should remember the date of last visit
import requests
import bs4
import os
import datetime
import shelve

comicWebsites = [
    'http://www.lefthandedtoons.com/',
    'http://buttersafe.com/',
    'http://www.savagechickens.com/',
    'http://www.lunarbaboon.com/',
    'http://www.exocomics.com/',
    'http://nonadventures.com/',
    'http://moonbeard.com/',
    'http://www.happletea.com/'
]
comicShelf = shelve.open('comicLastCheck')
comicShelf.setdefault(
    'lastTimeChecked', datetime.datetime.fromtimestamp(0))

os.makedirs('comics', exist_ok=True)
comicWebsite = comicWebsites[4]
res = requests.get(comicWebsite)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
dateElem = soup.select('.date')
dateComic = datetime.datetime.strptime(dateElem[0].getText(), "%d %b '%y")
print('Comics was posted on ', dateComic)
print('Last visit was on', comicShelf['lastTimeChecked'])
if dateComic > comicShelf['lastTimeChecked']:
    comicElem = soup.select('.image-style-main-comic')
    comicUrl = comicWebsite + comicElem[0].get('src')
    res = requests.get(comicUrl)
    res.raise_for_status()
    path = os.path.join('comics', os.path.basename(comicUrl))
    print(f'Downloading image {comicUrl}...')
    imageFile = open(path, 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    dateNow = datetime.datetime.now()
    comicShelf['lastTimeChecked'] = dateNow
else:
    print('No updates available')
comicShelf.close()
