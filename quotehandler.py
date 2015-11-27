# coding=utf-8
import random

class Quote(object):

    def __init__(self,filename):
        self.filename=filename
        self.quotes=dict()
        self.count=0
        with open(filename) as f:
            for line in f:
                linearr=line.strip().split(' ',1)
                self.quotes[int(linearr[0])]=linearr[1]
                self.count+=1
    
    def get_db_size(self):
        return self.count

    def get_random_quote(self):
        index=random.randint(0,self.count-1)
        quote=self.quotes[index]
        return str(index)+" - "+quote

    def get_quote_at(self,index):
        if index in self.quotes:
            quote=self.quotes[index]
            return str(index)+" - "+quote
        else:
            return "Pas d'article à cet index"

    def save_quote(self,quote):
        try:
            index=self.count
            with open(self.filename,"a") as f:
                string=str(index)+" "+quote.replace("\n"," ").strip()+"\n"
                print string
                f.write(string.encode('utf-8'))
        except Exception as e:
            print e
            return "Impossible de sauvegarder la quote" 
        return "Quote enregistrée sous l'index "+str(index)
    
    def search_quote(self,pattern):
        rv="\n Quotes matching "+pattern
        for key,value in self.quotes.items():
            if pattern.lower() in value:
                rv+="\n"+str(key)+" - "+value
        return rv
