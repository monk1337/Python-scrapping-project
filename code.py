import requests as tt
from bs4 import BeautifulSoup
from tkinter import *
import urllib.request
import io
from PIL import Image, ImageTk


import random

import json
tkinter_main=Tk()
get_first_url=tt.get("http://www.updatepedia.com/motivational-quotes-hindi/")
soup=BeautifulSoup(get_first_url.text,'html.parser')
name_box=soup.find_all(attrs={"class":"su-note-inner su-clearfix"})

def hi(x):
    for i in x:
        yield i.text
ter=hi(name_box)

get_url=tt.get("https://in.pinterest.com/search/pins/?rs=ac&len=2&q=batman%20motivation&eq=batman%20moti&etslf=5839&term_meta[]=batman%7Cautocomplete%7Cundefined&term_meta[]=motivation%7Cautocomplete%7Cundefined")
soup=BeautifulSoup(get_url.text,"html.parser")
er=[]
select_css=soup.select("script#jsInit1")[0]


def hello(x):
    for i in x:
        return json.loads(i)

desired_variable=hello(select_css)
random_1=random.randint(1,24)
random_2=random.randint(1,15)
ut=desired_variable['tree']['data']['results'][random_1]['images']['474x']['url']

r1=urllib.request.urlopen(ut).read()
r2=Image.open(io.BytesIO(r1))
r3=ImageTk.PhotoImage(r2)
print(name_box[random_2].text)
l1=Label(tkinter_main,image=r3).pack()
l2=Label(tkinter_main,text=(name_box[random_2].text)).pack()



tkinter_main.geometry("1000x1000")


tkinter_main.mainloop()

