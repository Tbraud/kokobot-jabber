# coding=utf-8
import requests
from bs4 import BeautifulSoup
import random

class Link(object):

    header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
    
    def __init__(self,filename):
        self.filename=filename
        self.links=dict()
        self.count=0
        with open(filename) as f:
            for line in f:
                linearr=line.strip().split(' ',2)
                self.links[int(linearr[0])]=(linearr[1],linearr[2])
                self.count+=1
    
    def get_db_size(self):
        return self.count

    def get_random_link(self):
        index=random.randint(0,self.count-1)
        url=self.links[index][0]
        title=self.links[index][1]
        return str(index)+" - "+title+" "+url

    def get_link_at(self,index):
        if index in self.links:
            url=self.links[index][0]
            title=self.links[index][1]
            return str(index)+" - "+title+" "+url
        else:
            return "Pas d'article à cet index"

    def process_link(self,url):
        title = self.get_title(url)
        if(title==-1):
            return "Erreur: impossible d'accéder à la page"
        index=self.save_link(url,title)
        if(index==-1):
            return "Erreur: impossible d'enregistrer le lien"
        else:
            self.links[index]=(url,title)
            self.count+=1
            return "Article enregistré sous l'index "+str(index)
    
    def get_title(self,url):
        try:
            r = requests.get(url,headers=self.header)
            soup = BeautifulSoup(r.text, 'html.parser')
            titles = soup.findAll('title')
            title=titles[0].text
        except:
            return -1
        return title

    def save_link(self,url,title):
        try:
            index=self.count
            with open(self.filename,"a") as f:
                string=str(index)+" "+url+" "+title.replace("\n"," ").strip()+"\n"
                print string
                f.write(string.encode('utf-8'))
        except Exception as e:
            print e
            return -1
        return index
    
    def search_link(self,pattern):
        rv="\n Links matching "+pattern
        for key,value in self.links.items():
            if pattern.lower() in value[0].lower() or pattern in value[1].lower():
                rv+="\n"+str(key)+" - "+value[1]+" "+value[0]
        return rv
