#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.error import HTTPError
from os.path import exists
from os import rename,remove,listdir
from sys import exit,argv
from wget import download
# import sys

with open("urls.txt") as links_f: linki = links_f.read().splitlines()
with open("titles.txt") as titles_f: nazwy = titles_f.read().splitlines()
if (len(linki) != len(nazwy)):
	print("Niezgodność długości list! Wycofuję się...")
	exit()

do_pobrania = [int(i) for i in argv[1:] if i.isnumeric()]
if not do_pobrania: do_pobrania = range(1, len(linki)-1)

for file in listdir():
    if file[-4:] == ".tmp":
    	print("Usuwam odpad: " + file)
    	remove(file)

for i in do_pobrania:
    try:
    	curr_epis = nazwy[i-1] + ".mp4"
    	if exists(curr_epis):
    		print("Odcinek " + str(i) + " został już pobrany, pomijam...")
    	else:
    		print("Pobieram odcinek " + str(i) + "...")
    		download(linki[i-1], curr_epis)
    		
    except HTTPError:
        print("Nie można pobrać odcinka " + str(i))
        continue

