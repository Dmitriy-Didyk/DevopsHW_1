#preconditions:
#pip install requests
#pip install google
#pip install psutil
#python3


import webbrowser
from urllib.parse import urlparse
from googlesearch import search  
import requests
from random import randrange
import os
import sys
import time
import psutil



#get 50 urls based on google search for random word, save unique
def google_urls (counter):

    #request for array of words
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"  
    response = requests.get(word_site)
    query = response.content.splitlines()
    countdown=0 #counter before restart browsers
    #get random number to choose random word from mit array
    i=randrange(10000)  
    links = []  
    prev_url=""
    if counter == 0:
        stop_counter=None

    #search for random word and save "unique" results to file
    for j in search(query[i], tld="co.in", num=100, stop=stop_counter, pause=2):    
        parse_result = urlparse(j)
        new_url = parse_result.scheme + "://" + parse_result.netloc
        if new_url!=prev_url:
            prev_url = new_url
            open_link(new_url)

            #restart browsers after x sites
            if countdown==10:    
                kill_browsers()
                countdown = 0
            else:
                countdown = countdown + 1
        


def kill_browsers():
    time.sleep(10)
    os.system("taskkill /im chrome.exe /F")
    os.system("taskkill /im msedge.exe /F")
    os.system("taskkill /im firefox.exe /F")
    time.sleep(10)

            
# open url at random browser and log links to file
def open_link(url):
    x=randrange(3)
    if x==0:
        ch = open ("ch.txt", "a") 
        browser = "chrome"
        webbrowser.get(browser).open(url, new=2)
        ch.write(url)  
        ch.write("\n")
        ch.close()
        time.sleep(5)
    elif x==1:
        ff = open ("ff.txt", "a")
        browser = "firefox"
        webbrowser.get(browser).open(url, new=2)
        ff.write(url) 
        ff.write("\n")
        ff.close()
        time.sleep(5)
    elif x==2:
        ed = open ("ed.txt", "a")
        browser= "edge"
        webbrowser.get(browser).open(url, new=2)
        ed.write(url) 
        ed.write("\n")
        ed.close()
        time.sleep(5)







# define browsers
br_chrome = 'chrome'
chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
br_ff = 'firefox'
ff_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(ff_path))
br_edge = 'edge'
edge_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge', None,webbrowser.BackgroundBrowser(edge_path))



#if no parameter
if (len(sys.argv)==1):   
    counter = 0 
else:
    counter = int(sys.argv[1])
    
#define number of sites to search, 0 for endless
google_urls(counter)  

