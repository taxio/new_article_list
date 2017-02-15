# -*- coding: utf-8 -*-

import urllib.request as urllib2
import sys
from bs4 import BeautifulSoup
import json
import re

class ITpro:

    def get_new_article():
        html = urllib2.urlopen("http://itpro.nikkeibp.co.jp/index-smart.html")
        soup = BeautifulSoup(html,"lxml")
        index_cs = soup.find_all('ul',class_="list_C")
        index_c = index_cs[1]
        links = index_c.find_all('a')
        article_list = [[0 for i in range(2)] for j in range(len(links))]
        for i in range(len(links)):
            article_title = links[i].find('h3')
            article_list[i][1] = "http://itpro.nikkeibp.co.jp"+links[i].get("href")
            article_list[i][0] = article_title.get_text()

        return article_list

class GIGAZINE:

    def get_content():
        html = urllib2.urlopen("http://gigazine.net/")
        soup = BeautifulSoup(html,"lxml")
        content = soup.find('div',class_="content")
        titles = content.find_all('h2')
        article_list = [[0 for i in range(2)] for j in range(len(titles))]
        for i in range(len(titles)):
            link = titles[i].find('a')
            article_list[i][0] = titles[i].get_text()
            article_list[i][1] = link.get('href')

        return article_list

class CNETJapan:

    def get_new_article():
        html = urllib2.urlopen("https://japan.cnet.com/")
        soup = BeautifulSoup(html,"lxml")
        latestnews = soup.find('div',id="latestnews")
        articles = latestnews.find_all('h3')
        article_list = [[0 for i in range(2)] for j in range(len(articles))]
        for i in range(len(articles)):
            link = articles[i].find('a')
            article_list[i][0] = articles[i].get_text()
            article_list[i][1] = "https://japan.cnet.com"+link.get("href")

        return article_list
