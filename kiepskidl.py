#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.error import HTTPError
from os.path import exists
from os import rename,remove
from sys import exit
import wget
# import sys

with open("urls.txt") as linki_f: linki = linki_f.read().splitlines()
with open("titles.txt") as nazwy_f: nazwy = nazwy_f.read().splitlines()
if (len(linki) != len(nazwy)):
	print("List ranges mismatch! Aborting...")
	exit()

do_pobrania = [int(i) if i.isnumeric() for i in sys.argv[1:]]
if not do_pobrania: do_pobrania = range(1, len(linki)-1)

for i in do_pobrania:
    # if !i.isnumeric(): continue
    try:
    	curr_epis = nazwy[i-1] + ".mp4"
    	curr_epis_temp = curr_epis + ".part"
    	# wget.download(linki[i-1], nazwy[i-1] + ".mp4")
    	if exists(curr_epis_temp):
    		print("Próbowano poprzednio pobrać " + str(i) + ", usuwam")
    		os.remove(curr_epis_temp)
    	if exists(curr_epis):
    		print("Odcinek " + str(i) + " został już pobrany, pomijam...")
    	else:
    		print("Pobieram odcinek " + str(i) + "...")
    		wget.download(linki[i-1], curr_epis_temp)
    		os.rename(curr_epis_temp, curr_epis)
    		
    except HTTPError:
        print("Nie można pobrać odcinka " + str(i))
        continue

