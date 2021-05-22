#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

while True:
    choice = int(input('vuoi inserire il tuo risultato in un file? (1 per sì) (2 per il no) (0 per uscire): '))
    if choice == 0:
        quit()
    link = str(input('inserisci il link: '))
    soup = BeautifulSoup(requests.get(link).content, 'html.parser')
    video_container = soup.findAll('source') # searchs all "videos", change this to make the script work for img or maybe text
    if(video_container == '[]'): # verifying if using the "source" tag found the link or not
        video_container = soup.findAll('video')
        if (video_container == '[]'):
            print('not working link')
        else:
            print(str(video_container[0]['src']))
            if(choice == 1):
                file = open('link.txt', 'a')
                file.write(str(video_container[1]['src']) + "\n")
                file.close()