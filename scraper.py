#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

while True:
    choice = int(input('vuoi inserire il tuo risultato in un file? (1 per sì) (2 per il no): '))
    link = str(input('inserisci il link (0 per uscire): '))
    if  link == '0':
        break
    soup = BeautifulSoup(requests.get(link).content, 'html.parser')
    video_container = str(soup.findAll('source')) # searchs all "videos", change this to make the script work for img or maybe text
    if(video_container == '[]'): # verifying if using the "source" tag found the link or not
        video_container = str(soup.findAll('video')) 
    if(video_container != '[]'):
        newList = []
        for i in video_container:
            newList.append(video_container.split('"')[1])
        if(choice == 1):
            file = open('link.txt', 'a')
            file.write(newList[1] + "\n")
            file.close()
        print(newList[1])
    else:
        print('not working link')