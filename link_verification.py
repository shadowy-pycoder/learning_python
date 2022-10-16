#!/usr/bin/env python3
# Write a program that, given the URL of a web page, will attempt to down-
# load every linked page on the page. The program should flag any pages
# that have a 404 “Not Found” status code and print them out as broken links.


import requests
import sys
import bs4


if len(sys.argv) < 2:
    print('Usage: app.py <URL>')
    sys.exit(1)

res = requests.get(sys.argv[1])
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
broken_links = []
for link in soup.find_all('a', href=True):
    try:
        res = requests.get(link['href'], stream=True, timeout=5)
    except:
        pass
    else:
        print(f"Checking {link['href']}")
        if res.status_code == 404:
            print(f"\n404 Page Not Found: {link['href']}\n")
            broken_links.append(link['href'])
print('\nDone checking')
print('The following pages give 404 error:')
print(*broken_links, sep='\n')
