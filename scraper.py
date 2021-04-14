#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

while True:
    choice = int(input('vuoi inserire il tuo risultato in un file? (1 per sì) (2 per il no)'))
    link = str(input('inserisci il link (0 per uscire): '))
    if(link == "0"):
        break
    soup = BeautifulSoup(requests.get(link).content, 'html.parser')
    movie_containers = []
    n =  soup.findAll('source')
    movie_containers.append(str(n) + "\n")
    if(n != '[]'):
        if(choice == 1):
            file = open("link.txt", "w")
            file.write(movie_containers)
            file.close()
        print(movie_containers)
    else:
        print("not working link")