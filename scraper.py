#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

while True:
    link = str(input("inserisci il link (0 per uscire): "))
    if(link == "0"):
        break
    soup = BeautifulSoup(requests.get(link).content, 'html.parser')
    movie_containers = []
    n =  soup.findAll('source')
    movie_containers.append(str(n) + "\n")
    print(movie_containers)