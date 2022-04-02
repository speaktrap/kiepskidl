#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.error import HTTPError
from sys import exit
import wget
import sys

with open("urls.txt") as linki_f: linki = linki_f.read().splitlines()
with open("titles.txt") as nazwy_f: nazwy = nazwy_f.read().splitlines()
if (len(linki) != len(nazwy)):
	print("List ranges mismatch! Aborting...")
	exit()

do_pobrania = [int(i) for i in sys.argv[1:]]
if not do_pobrania: do_pobrania = range(1, len(linki)-1)

for i in do_pobrania:
    try:
    	print("Pobieram odcinek " + str(i) + "...")
    	wget.download(linki[i-1], nazwy[i-1] + ".mp4")
    except HTTPError:
        print("Nie można pobrać odcinka " + str(i))
        continue

