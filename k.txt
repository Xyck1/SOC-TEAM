import os, threading, time, requests, socket, sys, mechanize
from bs4 import BeautifulSoup

import OskharGans

#---------------------------------------------------------------------------------------------------------------------------

os.system("clear")                                             

print("\033[96m")
print("            .::::.                           ")
print("          `+:    :/`                         ")
print("         +:.      .-+                        ")
print("         o-........-o`-`                     ")
print("          `.........:+-+:                    ")
print("                   o+...+o                   ")
print("                  o-     -o                  ")
print("                 -o `.-.` o-                 ")
print("                 s. s   s .s           ``    ")
print("                 y  o   o  y         `:..:`  ")
print("      `..`       s.  ...  .s        .:.``.:. ")
print("    /+/::++-     -o       o-         ``````  ")
print(" `-s/     `y/-  `+y:`...`:y+`                ")
print(".y-.       `./s yo++/+-+/+/oy                ")
print(".y-.\033[91mBy.Xyck\033[96m../y`/`  -N+m-  `/`               ")
print(" `-::::::::::.`      +M+                     ")
print("                      :                      ")
print("                                             ")
print("                                             ")
print("                                             ")

time.sleep(0.2)
os.system("clear")
                                            
print("                                             ")
print("            .::::.   /+/                     ")
print("          `+:    :/.s- -s.                   ")
print("         +:.      .:s....s.                  ")
print("         o-........-o    `y`                 ")
print("          `......o/`-///- :+                 ")
print("                 y  h` `h `y                 ")
print("                 y  -///- `y                 ")
print("                 +:       :+                 ")
print("                 .y       h.           ``    ")
print("                -ooo-:::-ooo:        `:..:`  ")
print("      `..`     `h/-.:y`y:.-/h`      .:.``.:. ")
print("    /+/::++-    `   `ddd`   `        ``````  ")
print(" `-s/     `y/-       .h.                     ")
print(".y-.       `./s       :                      ")
print(".y-.\033[91mBy.Xyck\033[96m../y       :                      ")
print(" `-::::::::::.`                              ")
print("                      :                      ")
print("                                             ")
print("                                             ")
print("                                             ")

time.sleep(0.2)
os.system("clear")


print("                  +:     :+                  ")
print("            .:::::s  ```  s.                 ")
print("          `+:    :+`o/-/o .o                 ")
print("         +:.      .-h-`-s  y                 ")
print("         o-........-o-:-  `s                 ")
print("          `....../o`      +:                 ")
print("                 :h.`````.h:                 ")
print("                oo+o/+:+/o+os                ")
print("               `+.  -m:m-  .+`               ")
print("                     sMs               ``    ")
print("                      :              `:..:`  ")
print("      `..`            :             .:.``.:. ")
print("    /+/::++-                         ``````  ")
print(" `-s/     `y/-        :                      ")
print(".y-.       `./s                              ")
print(".y-.\033[91mBy.Xyck\033[96m../y       :                      ")
print(" `-::::::::::.`                              ")
print("                      :                      ")
print("                                             ")
print("                                             ")
print("                                             ")

time.sleep(0.2)
os.system("clear")

print("                 y  :+/+:  y                 ")
print("            .::::y-       -o                 ")
print("          `+:    :s`      y.                 ")
print("         +:.      .-+-:--+oo.                ")
print("         o-........-ys`s/-:+d                ")
print("          `........``mym.   .`               ")
print("                     -m-                     ")
print("                      :                      ")
print("                                             ")
print("                      :                ``    ")
print("                                     `:..:`  ")
print("      `..`            :             .:.``.:. ")
print("    /+/::++-                         ``````  ")
print(" `-s/     `y/-        :                      ")
print(".y-.       `./s                              ")
print(".y-.\033[91mBy.Xyck\033[96m../y       :                      ")
print(" `-::::::::::.`                              ")
print("                      :                      ")
print("                                             ")
print("                                             ")
print("                                             ")

time.sleep(0.2)
os.system("clear")



print("                +o+s/////y+o+                ")
print("            .:::d/  :m.m:  -s`               ")
print("          `+:    :/` yMy                     ")
print("         +:.      .-+`o`                     ")
print("         o-........-o                        ")
print("          `........`  :                      ")
print("                                             ")
print("                      :                      ")
print("                                             ")
print("                      :                ``    ")
print("                                     `:..:`  ")
print("      `..`            :             .:.``.:. ")
print("    /+/::++-                         ``````  ")
print(" `-s/     `y/-        :                      ")
print(".y-.       `./s                              ")
print(".y-.\033[91mBy.Xyck\033[96m../y       :                      ")
print(" `-::::::::::.`                              ")
print("                      :                      ")
print("                                             ")
print("                                             ")
print("                                             ")

time.sleep(0.2)
os.system("clear")

print("                      :                      ")
print("            .::::.    :                      ")
print("          `+:    :/`                         ")
print("         +:.      .-+ :                      ")
print("         o-........-o                        ")
print("          `........`  :                      ")
print("                                             ")
print("                      :                      ")
print("                                             ")
print("                      :                ``    ")
print("                                     `:..:`  ")
print("      `..`            :             .:.``.:. ")
print("    /+/::++-                         ``````  ")
print(" `-s/     `y/-        :                      ")
print(".y-.       `./s                              ")
print(".y-.\033[91mBy.Xyck\033[96m../y       :                      ")
print(" `-::::::::::.`                              ")
print("                      :                      ")
print("                                             ")
print("                                             ")
print("                                             ")

time.sleep(1)
os.system("clear")


#---------------------------------------------------------------------------------------------------------------------------

def steg():
	print("\033[91m(\033[92m1\033[91m)\033[96m Menyembunyikan pesan\n\033[91m(\033[92m2\033[91m)\033[96m Melihat pesan tersembunyi")
	jawb=str(input("\033[91m>>> \033[93m"))
	if jawb == "1":
		print("\033[96mMasukan pesan anda")
		psn=str(input("\033[91m>>> \033[93m"))
		rr=open("input_pesan.txt","w")
		rr.write("")
		rr=open("input_pesan.txt","a")
		rr.write(psn)
		print("\033[96mFotonya")
		fto=str(input("\033[91m>>> \033[93m"))
		os.system("steghide embed -cf "+str(fto)+" -ef input_pesan.txt")
	elif jawb == "2":
		print("\033[96mFoto yang berisi pesan tersembunyi")
		fto=str(input("\033[91m>>> \033[93m"))
		os.system("steghide extract -sf "+str(fto))
	else:
		print("\033[91mJawab yang bener tolol")
		steg()

#---------------------------------------------------------------------------------------------------------------------------


def Copy():
	os.system("clear")
	print("\033[96mMasukan URL Website")
	url=str(input("\033[91m>>> \033[93m"))
	print("\033[96mNama file yang ingin di isi html")
	file=str(input("\033[91m>>> \033[93m"))
	file="%s.html"%(file)
	req=requests.get(url)
	html=bs(req.text,"html.parser")
	ct3=open(file,"w")
	ct3.write("")
	ct4=open(file,"a")
	ct4.write(str(html))
	print("\033[96mSuccess, code website target berhasil di copy\033[92m")


#---------------------------------------------------------------------------------------------------------------------------

mation = "wait"
def anim():
	while True:
		sys.stdout.write("\r [+] [|] [+] Wait   ")
		time.sleep(0.2)
		sys.stdout.write("\r [-] [\\] [-] wAit.  ")
		time.sleep(0.2)
		sys.stdout.write("\r [+] [-] [+] waIt.. ")
		time.sleep(0.2)
		sys.stdout.write("\r [-] [/] [-] waiT...")
		time.sleep(0.2)
		if mation == "success":
			sys.exit()

tanim=threading.Thread(target=anim)


#---------------------------------------------------------------------------------------------------------------------------


print("\033[91m(\033[92m1\033[91m)\033[96m DDoS Attack[√]\n\033[91m(\033[92m2\033[91m)\033[96m Get info from number phone[√]\n\033[91m(\033[92m3\033[91m)\033[96m Copy Html Website[√]\n\033[91m(\033[92m4\033[91m)\033[96m Scan IP and Port Website[√]\n\033[91m(\033[92m5\033[91m)\033[96m WP Bruteforce[√]\n\033[91m(\033[92m6\033[91m)\033[96m Bruteforce WiFi Cracking[X]\n\033[91m(\033[92m7\033[91m)\033[96m Hack WiFi wihtout Crack[X]\n\033[91m(\033[92m8\033[91m)\033[96m Scan Website[X]\n\033[91m(\033[92m9\033[91m)\033[96m Stegnography[√]\n\033[91m(\033[92m10\033[91m)\033[96m Phising[X]\n\033[91m(\033[92m11\033[91m)\033[96m Virtex[X]\n\033[91m(\033[92m12\033[91m)\033[96m Phising dengan html buatan sendiri[X]\n\033[91m(\033[92m13\033[91m)\033[96m Membagi file[√]\n\033[91m(\033[92m14\033[91m)\033[96m cPanel Bruteforce[X] \n\033[91m(\033[92m15\033[91m)\033[96m Bot auto absen sekolah [khusus linux][√] \n\033[91m(\033[92m16\033[91m)\033[96m Browsing Darkweb via terminal/termux[X] \n")
jawaban=str(input("\033[91m>>> \033[93m"))


#---------------------------------------------------------------------------------------------------------------------------


if jawaban == "1":
	os.system("clear")
	print ("\033[96mMasukan IP target:")
	target = input("\033[91m>>> \033[93m")
	print ("\033[96mMasukan PORT target:")
	port= int(input("\033[91m>>> \033[93m"))
	def if1():
		print ("\033[96mMasukan jumblah thread [1-100] :")
		th= int(input("\033[91m>>> \033[93m"))
		return th
	OskharGans.DDoS(port,target)
	th=if1()


	def t1():
		while True:
			os1()
	def t2():
		while True:
			os2()
	def t3():
		while True:
			os3()
	def t4():
		while True:
			os4()
	def t5():
		while True:
			os5()
	def t6():
		while True:
			os6()
	def t7():
		while True:
			os7()
	def t8():
		while True:
			os8()
	def t9():
		while True:
			os9()
	def t10():
		while True:
			os10()
	tth1=threading.Thread(target=t1)
	tth2=threading.Thread(target=t2)
	tth3=threading.Thread(target=t3)
	tth4=threading.Thread(target=t4)
	tth5=threading.Thread(target=t5)
	tth1=threading.Thread(target=t6)
	tth2=threading.Thread(target=t7)
	tth3=threading.Thread(target=t8)
	tth4=threading.Thread(target=t9)
	tth5=threading.Thread(target=t10)

	def if2(th):
		if th == 1:
			OskharGans.Dos1()
		elif th == 2:
			OskharGans.Dos2()
		elif th == 3:
			OskharGans.Dos3()
		elif th == 4:
			OskharGans.Dos4()
		elif th == 5:
			OskharGans.Dos5()
		elif th == 6:
			OskharGans.Dos6()
		elif th == 7:
			OskharGans.Dos7()
		elif th == 8:
			OskharGans.Dos8()
		elif th == 9:
			OskharGans.Dos9()
		elif th == 10:
			OskharGans.Dos10()
		elif th == 11:
			OskharGans.Dos11()
		elif th == 12:
			OskharGans.Dos12()
		elif th == 13:
			OskharGans.Dos13()
		elif th == 14:
			OskharGans.Dos14()
		elif th == 15:
			OskharGans.Dos15()
		elif th == 16:
			OskharGans.Dos16()
		elif th == 17:
			OskharGans.Dos17()
		elif th == 18:
			OskharGans.Dos18()
		elif th == 19:
			OskharGans.Dos19()
		elif th == 20:
			OskharGans.Dos20()
		elif th == 21:
			OskharGans.Dos21()
		elif th == 22:
			OskharGans.Dos22()
		elif th == 23:
			OskharGans.Dos23()
		elif th == 24:
			OskharGans.Dos24()
		elif th == 25:
			OskharGans.Dos25()
		elif th == 26:
			OskharGans.Dos26()
		elif th == 27:
			OskharGans.Dos27()
		elif th == 28:
			OskharGans.Dos28()
		elif th == 29:
			OskharGans.Dos29()
		elif th == 30:
			OskharGans.Dos30()
		elif th == 31:
			OskharGans.Dos31()
		elif th == 32:
			OskharGans.Dos32()
		elif th == 33:
			OskharGans.Dos33()
		elif th == 34:
			OskharGans.Dos34()
		elif th == 35:
			OskharGans.Dos35()
		elif th == 36:
			OskharGans.Dos36()
		elif th == 37:
			OskharGans.Dos37()
		elif th == 38:
			OskharGans.Dos38()
		elif th == 39:
			OskharGans.Dos39()
		elif th == 40:
			OskharGans.Dos40()
		elif th == 41:
			OskharGans.Dos41()
		elif th == 42:
			OskharGans.Dos42()
		elif th == 43:
			OskharGans.Dos43()
		elif th == 44:
			OskharGans.Dos44()
		elif th == 45:
			OskharGans.Dos45()
		elif th == 46:
			OskharGans.Dos46()
		elif th == 47:
			OskharGans.Dos47()
		elif th == 48:
			OskharGans.Dos48()
		elif th == 49:
			OskharGans.Dos49()
		elif th == 50:
			OskharGans.Dos50()
		elif th == 51:
			OskharGans.Dos51()
		elif th == 52:
			OskharGans.Dos52()
		elif th == 53:
			OskharGans.Dos53()
		elif th == 54:
			OskharGans.Dos54()
		elif th == 55:
			OskharGans.Dos55()
		elif th == 56:
			OskharGans.Dos56()
		elif th == 57:
			OskharGans.Dos57()
		elif th == 58:
			OskharGans.Dos58()
		elif th == 59:
			OskharGans.Dos59()
		elif th == 60:
			OskharGans.Dos60()
		elif th == 61:
			OskharGans.Dos61()
		elif th == 62:
			OskharGans.Dos62()
		elif th == 63:
			OskharGans.Dos63()
		elif th == 64:
			OskharGans.Dos64()
		elif th == 65:
			OskharGans.Dos65()
		elif th == 66:
			OskharGans.Dos66()
		elif th == 67:
			OskharGans.Dos67()
		elif th == 68:
			OskharGans.Dos68()
		elif th == 69:
			OskharGans.Dos69()
		elif th == 70:
			OskharGans.Dos70()
		elif th == 71:
			OskharGans.Dos71()
		elif th == 72:
			OskharGans.Dos72()
		elif th == 73:
			OskharGans.Dos73()
		elif th == 74:
			OskharGans.Dos74()
		elif th == 75:
			OskharGans.Dos75()
		elif th == 76:
			OskharGans.Dos76()
		elif th == 77:
			OskharGans.Dos77()
		elif th == 78:
			OskharGans.Dos78()
		elif th == 79:
			OskharGans.Dos79()
		elif th == 80:
			OskharGans.Dos80()
		elif th == 81:
			OskharGans.Dos81()
		elif th == 82:
			OskharGans.Dos82()
		elif th == 83:
			OskharGans.Dos83()
		elif th == 84:
			OskharGans.Dos84()
		elif th == 85:
			OskharGans.Dos85()
		elif th == 86:
			OskharGans.Dos86()
		elif th == 87:
			OskharGans.Dos87()
		elif th == 88:
			OskharGans.Dos88()
		elif th == 89:
			OskharGans.Dos89()
		elif th == 90:
			OskharGans.Dos90()
		elif th == 91:
			OskharGans.Dos91()
		elif th == 92:
			OskharGans.Dos92()
		elif th == 93:
			OskharGans.Dos93()
		elif th == 94:
			OskharGans.Dos94()
		elif th == 95:
			OskharGans.Dos95()
		elif th == 96:
			OskharGans.Dos96()
		elif th == 97:
			OskharGans.Dos97()
		elif th == 98:
			OskharGans.Dos98()
		elif th == 99:
			OskharGans.Dos99()
		elif th == 100:
			OskharGans.Dos100()

		else:
			print ("\033[91mJawab yang bener tolol\033[92m")
			th=if1()
			f2(th)
	if2(th)


#---------------------------------------------------------------------------------------------------------------------------


elif jawaban == "2":
	os.system("clear")
	print("\033[96mContoh (+62) 82718728182")
	z1=str(input("Masukan Nomor yang ingin di lacak <=> (+62) "))

	u1="https://id.tellows.net/num/0"+z1
	s1= requests.get(u1)
	x1=BeautifulSoup(s1.text,'html.parser')
	d1=x1.find('td', style="width:80%;")
	print("\n")
	print("\033[92mType nomor:"+d1.text+"\033[91m")
	s2= requests.get(u1)
	x2=BeautifulSoup(s2.text,'html.parser')
	d2=x2.find('table', style="table-layout: fixed;line-height: 22px;margin-top:-15px;")
	print(d2.text)


	print("\n\n\033[92mInfo akun dari nomor Hp\033[96m\n")

	f2=("62","0")
	f1=('inurl:facebook intext:"','inurl:instagram intext:"','inurl:twitter intext:"','inurl:github intext:"')
	f6=("info akun facebook:\n", "info akun instagram:\n", "info akun twitter:\n", "info akun github:\n")



	for q in range(2):
		for q2 in range(4):
			print("\n\033[91m",f6[q2],"\033[96m")
			br1 = mechanize.Browser()
			url1 = "https://www.google.com/"
			br1.set_handle_robots(False)
			br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
			br1.open(url1)
			br1.select_form(nr=0)
			br1.form["q"] = f1[q2]+f2[q]+z1+'"'
			sub1= br1.submit()
			print ("\033[92m",sub1.geturl(),"\033[96m\n")

			s2= requests.get(sub1.geturl())
			x2=BeautifulSoup(s2.text,'html.parser')
			llk=x2.select("a")
			lk = min(5, len(llk))
			for i in range(lk):
				print("https://google.com"+llk[i].get("href"))


#---------------------------------------------------------------------------------------------------------------------------


elif jawaban == "3":
	Copy()


#---------------------------------------------------------------------------------------------------------------------------


elif jawaban == "4":
	os.system("clear")
	print("\033[96mMasukan Url target [tidak menggunakan https] ")
	url=str(input("\033[91m>>> \033[93m"))
	os.system("clear")
	print ("ketik ctrl + c jika sudah selesai")
	def t1():
		os.system("perl nikto/program/nikto.pl -h "+str(url)+" | grep IP:")
	def t2():
		os.system("perl nikto/program/nikto.pl -h "+str(url)+" | grep Port:")
	th1=threading.Thread(target=t1)
	th2=threading.Thread(target=t2)
	th1.start()
	th2.start()
	time.sleep(3)
	print("\033[91m")


#---------------------------------------------------------------------------------------------------------------------------


elif jawaban == "5":
	os.system("clear")
	print("\033[96mMasukan URL wp-login nya:")
	inurl=str(input("\033[91m>>> \033[93m"))
	print("\033[96mMasukan username:")
	z=str(input("\033[91m>>> \033[93m"))
	print("\033[96mMasukan Wordlist:")
	fl=str(input("\033[91m>>> \033[93m"))
	print("\033[96mThreading 10 or 100:")
	tr=str(input("\033[91m>>> \033[93m"))
	if tr != "10" or "100":
		tr="10"
		print("\033[92m")
		tanim.start()
		os.system("grep -c -E '^.{1,500}$' "+str(fl)+" > namafl.txt")
		nm="0."
		a=open("namafl.txt", "r")
		brs=a.readline().strip()
	else:
		print("\033[92m")
		tanim.start()
		os.system("grep -c -E '^.{1,500}$' "+str(fl)+" > namafl.txt")
		nm="0."
		a=open("namafl.txt", "r")
		brs=a.readline().strip()

	if int(brs) <= 500000:
		brs = 500000

	OskharGans.reead()

	OskharGans.input_data(inurl,z)

	m=int(int(brs)/100);os.system("sed -n 1,%sp %s > %s1.txt"%(m,fl,nm));a=m*2;os.system("sed -n %s,%sp %s > %s2.txt"%(m,a,fl,nm));a=m*2;
	b=m*3;os.system("sed -n %s,%sp %s > %s3.txt"%(a,b,fl,nm));a=m*3;b=m*4;os.system("sed -n %s,%sp %s > %s4.txt"%(a,b,fl,nm));a=m*4;b=m*5;
	os.system("sed -n %s,%sp %s > %s5.txt"%(a,b,fl,nm));a=m*5;b=m*6;os.system("sed -n %s,%sp %s > %s6.txt"%(a,b,fl,nm));a=m*6;b=m*7;
	os.system("sed -n %s,%sp %s > %s7.txt"%(a,b,fl,nm));a=m*7;b=m*8;os.system("sed -n %s,%sp %s > %s8.txt"%(a,b,fl,nm));a=m*8;b=m*9;
	os.system("sed -n %s,%sp %s > %s9.txt"%(a,b,fl,nm));a=m*9;b=m*10;os.system("sed -n %s,%sp %s > %s10.txt"%(a,b,fl,nm));a=m*10;b=m*11;
	os.system("sed -n %s,%sp %s > %s11.txt"%(a,b,fl,nm));a=m*11;b=m*12;os.system("sed -n %s,%sp %s > %s12.txt"%(a,b,fl,nm));a=m*12;b=m*13;
	os.system("sed -n %s,%sp %s > %s13.txt"%(a,b,fl,nm));a=m*13;b=m*14;os.system("sed -n %s,%sp %s > %s14.txt"%(a,b,fl,nm));a=m*14;b=m*15;
	os.system("sed -n %s,%sp %s > %s15.txt"%(a,b,fl,nm));a=m*15;b=m*16;os.system("sed -n %s,%sp %s > %s16.txt"%(a,b,fl,nm));a=m*16;b=m*17;
	os.system("sed -n %s,%sp %s > %s17.txt"%(a,b,fl,nm));a=m*17;b=m*18;os.system("sed -n %s,%sp %s > %s18.txt"%(a,b,fl,nm));a=m*18;b=m*19;
	os.system("sed -n %s,%sp %s > %s19.txt"%(a,b,fl,nm));a=m*19;b=m*20;os.system("sed -n %s,%sp %s > %s20.txt"%(a,b,fl,nm));a=m*20;b=m*21;
	os.system("sed -n %s,%sp %s > %s21.txt"%(a,b,fl,nm));a=m*21;b=m*22;os.system("sed -n %s,%sp %s > %s22.txt"%(a,b,fl,nm));a=m*22;b=m*23;
	os.system("sed -n %s,%sp %s > %s23.txt"%(a,b,fl,nm));a=m*23;b=m*24;os.system("sed -n %s,%sp %s > %s24.txt"%(a,b,fl,nm));a=m*24;b=m*25;
	os.system("sed -n %s,%sp %s > %s25.txt"%(a,b,fl,nm));a=m*25;b=m*26;os.system("sed -n %s,%sp %s > %s26.txt"%(a,b,fl,nm));a=m*26;b=m*27;
	os.system("sed -n %s,%sp %s > %s27.txt"%(a,b,fl,nm));a=m*27;b=m*28;os.system("sed -n %s,%sp %s > %s28.txt"%(a,b,fl,nm));a=m*28;b=m*29;
	os.system("sed -n %s,%sp %s > %s29.txt"%(a,b,fl,nm));a=m*29;b=m*30;os.system("sed -n %s,%sp %s > %s30.txt"%(a,b,fl,nm));a=m*30;b=m*31;
	os.system("sed -n %s,%sp %s > %s31.txt"%(a,b,fl,nm));a=m*31;b=m*32;os.system("sed -n %s,%sp %s > %s32.txt"%(a,b,fl,nm));a=m*32;b=m*33;
	os.system("sed -n %s,%sp %s > %s33.txt"%(a,b,fl,nm));a=m*33;b=m*34;os.system("sed -n %s,%sp %s > %s34.txt"%(a,b,fl,nm));a=m*34;b=m*35;
	os.system("sed -n %s,%sp %s > %s35.txt"%(a,b,fl,nm));a=m*35;b=m*36;os.system("sed -n %s,%sp %s > %s36.txt"%(a,b,fl,nm));a=m*36;b=m*37;
	os.system("sed -n %s,%sp %s > %s37.txt"%(a,b,fl,nm));a=m*37;b=m*38;os.system("sed -n %s,%sp %s > %s38.txt"%(a,b,fl,nm));a=m*38;b=m*39;
	os.system("sed -n %s,%sp %s > %s39.txt"%(a,b,fl,nm));a=m*39;b=m*40;os.system("sed -n %s,%sp %s > %s40.txt"%(a,b,fl,nm));a=m*40;b=m*41;
	os.system("sed -n %s,%sp %s > %s41.txt"%(a,b,fl,nm));a=m*41;b=m*42;os.system("sed -n %s,%sp %s > %s42.txt"%(a,b,fl,nm));a=m*42;b=m*43;
	os.system("sed -n %s,%sp %s > %s43.txt"%(a,b,fl,nm));a=m*43;b=m*44;os.system("sed -n %s,%sp %s > %s44.txt"%(a,b,fl,nm));a=m*44;b=m*45;
	os.system("sed -n %s,%sp %s > %s45.txt"%(a,b,fl,nm));a=m*45;b=m*46;os.system("sed -n %s,%sp %s > %s46.txt"%(a,b,fl,nm));a=m*46;b=m*47;
	os.system("sed -n %s,%sp %s > %s47.txt"%(a,b,fl,nm));a=m*47;b=m*48;os.system("sed -n %s,%sp %s > %s48.txt"%(a,b,fl,nm));a=m*48;b=m*49;
	os.system("sed -n %s,%sp %s > %s49.txt"%(a,b,fl,nm));a=m*49;b=m*50;os.system("sed -n %s,%sp %s > %s50.txt"%(a,b,fl,nm));a=m*50;b=m*51;
	os.system("sed -n %s,%sp %s > %s51.txt"%(a,b,fl,nm));a=m*51;b=m*52;os.system("sed -n %s,%sp %s > %s52.txt"%(a,b,fl,nm));a=m*52;b=m*53;
	os.system("sed -n %s,%sp %s > %s53.txt"%(a,b,fl,nm));a=m*53;b=m*54;os.system("sed -n %s,%sp %s > %s54.txt"%(a,b,fl,nm));a=m*54;b=m*55;
	os.system("sed -n %s,%sp %s > %s55.txt"%(a,b,fl,nm));a=m*55;b=m*56;os.system("sed -n %s,%sp %s > %s56.txt"%(a,b,fl,nm));a=m*56;b=m*57;
	os.system("sed -n %s,%sp %s > %s57.txt"%(a,b,fl,nm));a=m*57;b=m*58;os.system("sed -n %s,%sp %s > %s58.txt"%(a,b,fl,nm));a=m*58;b=m*59;
	os.system("sed -n %s,%sp %s > %s59.txt"%(a,b,fl,nm));a=m*59;b=m*60;os.system("sed -n %s,%sp %s > %s60.txt"%(a,b,fl,nm));a=m*60;b=m*61;
	os.system("sed -n %s,%sp %s > %s61.txt"%(a,b,fl,nm));a=m*61;b=m*62;os.system("sed -n %s,%sp %s > %s62.txt"%(a,b,fl,nm));a=m*62;b=m*63;
	os.system("sed -n %s,%sp %s > %s63.txt"%(a,b,fl,nm));a=m*63;b=m*64;os.system("sed -n %s,%sp %s > %s64.txt"%(a,b,fl,nm));a=m*64;b=m*65;
	os.system("sed -n %s,%sp %s > %s65.txt"%(a,b,fl,nm));a=m*65;b=m*66;os.system("sed -n %s,%sp %s > %s66.txt"%(a,b,fl,nm));a=m*66;b=m*67;
	os.system("sed -n %s,%sp %s > %s67.txt"%(a,b,fl,nm));a=m*67;b=m*68;os.system("sed -n %s,%sp %s > %s68.txt"%(a,b,fl,nm));a=m*68;b=m*69;
	os.system("sed -n %s,%sp %s > %s69.txt"%(a,b,fl,nm));a=m*69;b=m*70;os.system("sed -n %s,%sp %s > %s70.txt"%(a,b,fl,nm));a=m*70;b=m*71;
	os.system("sed -n %s,%sp %s > %s71.txt"%(a,b,fl,nm));a=m*71;b=m*72;os.system("sed -n %s,%sp %s > %s72.txt"%(a,b,fl,nm));a=m*72;b=m*73;
	os.system("sed -n %s,%sp %s > %s73.txt"%(a,b,fl,nm));a=m*73;b=m*74;os.system("sed -n %s,%sp %s > %s74.txt"%(a,b,fl,nm));a=m*74;b=m*75;
	os.system("sed -n %s,%sp %s > %s75.txt"%(a,b,fl,nm));a=m*75;b=m*76;os.system("sed -n %s,%sp %s > %s76.txt"%(a,b,fl,nm));a=m*76;b=m*77;
	os.system("sed -n %s,%sp %s > %s77.txt"%(a,b,fl,nm));a=m*77;b=m*78;os.system("sed -n %s,%sp %s > %s78.txt"%(a,b,fl,nm));a=m*78;b=m*79;
	os.system("sed -n %s,%sp %s > %s79.txt"%(a,b,fl,nm));a=m*79;b=m*80;os.system("sed -n %s,%sp %s > %s80.txt"%(a,b,fl,nm));a=m*80;b=m*81;
	os.system("sed -n %s,%sp %s > %s81.txt"%(a,b,fl,nm));a=m*81;b=m*82;os.system("sed -n %s,%sp %s > %s82.txt"%(a,b,fl,nm));a=m*82;b=m*83;
	os.system("sed -n %s,%sp %s > %s83.txt"%(a,b,fl,nm));a=m*83;b=m*84;os.system("sed -n %s,%sp %s > %s84.txt"%(a,b,fl,nm));a=m*84;b=m*85;
	os.system("sed -n %s,%sp %s > %s85.txt"%(a,b,fl,nm));a=m*85;b=m*86;os.system("sed -n %s,%sp %s > %s86.txt"%(a,b,fl,nm));a=m*86;b=m*87;
	os.system("sed -n %s,%sp %s > %s87.txt"%(a,b,fl,nm));a=m*87;b=m*88;os.system("sed -n %s,%sp %s > %s88.txt"%(a,b,fl,nm));a=m*88;b=m*89;
	os.system("sed -n %s,%sp %s > %s89.txt"%(a,b,fl,nm));a=m*89;b=m*90;os.system("sed -n %s,%sp %s > %s90.txt"%(a,b,fl,nm));a=m*90;b=m*91;
	os.system("sed -n %s,%sp %s > %s91.txt"%(a,b,fl,nm));a=m*91;b=m*92;os.system("sed -n %s,%sp %s > %s92.txt"%(a,b,fl,nm));a=m*92;b=m*93;
	os.system("sed -n %s,%sp %s > %s93.txt"%(a,b,fl,nm));a=m*93;b=m*94;os.system("sed -n %s,%sp %s > %s94.txt"%(a,b,fl,nm));a=m*94;b=m*95;
	os.system("sed -n %s,%sp %s > %s95.txt"%(a,b,fl,nm));a=m*95;b=m*96;os.system("sed -n %s,%sp %s > %s96.txt"%(a,b,fl,nm));a=m*96;b=m*97;
	os.system("sed -n %s,%sp %s > %s97.txt"%(a,b,fl,nm));a=m*97;b=m*98;os.system("sed -n %s,%sp %s > %s98.txt"%(a,b,fl,nm));a=m*98;b=m*99;
	os.system("sed -n %s,%sp %s > %s99.txt"%(a,b,fl,nm));a=m*99;b=m*100;os.system("sed -n %s,%sp %s > %s100.txt"%(a,b,fl,nm));
	mation = "success";time.sleep(0.5);
	print("")

	if tr == "10":
		OskharGans.start1()
	elif tr == "100":
		OskharGans.start2()

#---------------------------------------------------------------------------------------------------------------------------

elif jawaban == "6":
	print ("\033[91mBelom ada tolol\033[92m")

#---------------------------------------------------------------------------------------------------------------------------

elif jawaban == "7":
	print ("\033[91mBelom ada tolol\033[92m")

#---------------------------------------------------------------------------------------------------------------------------

elif jawaban == "8":
	print ("\033[91mBelom ada tolol\033[92m")

#---------------------------------------------------------------------------------------------------------------------------

elif jawaban == "9":
	steg()

#---------------------------------------------------------------------------------------------------------------------------


elif jawaban == "10":
	print ("\033[91mBelom ada tolol\033[92m")

#---------------------------------------------------------------------------------------------------------------------------

elif jawaban == "11":
	print ("\033[91mBelom ada tolol\033[92m")

#---------------------------------------------------------------------------------------------------------------------------

elif jawaban == "12":
	print ("\033[91mBelom ada tolol\033[92m")

#---------------------------------------------------------------------------------------------------------------------------

elif jawaban == "13":
    os.system("clear")
    brs=int(input("Jumblah baris <=>"))
    jml=str(input("Jumblah file <=>"))
    fl=str(input("File yang ingin di bagi <=>"))
    nm=str(input("Nama file <=>"))

    if jml == '2':
        m=int(brs/2)
        os.system("sed -n 1,%sp %s > %s1.txt"%(m,fl,nm))
        a=m*2
        os.system("sed -n %s,%sp %s > %s2.txt"%(m,a,fl,nm))

    elif jml == '3':
        m=int(brs/3)
        os.system("sed -n 1,%sp %s > %s1.txt"%(m,fl,nm))
        a=m*2
        os.system("sed -n %s,%sp %s > %s2.txt"%(m,a,fl,nm))
        b=m*3
        os.system("sed -n %s,%sp %s > %s3.txt"%(a,b,fl,nm))

    elif jml == '4':
        m=int(brs/4)
        os.system("sed -n 1,%sp %s > %s1.txt"%(m,fl,nm))
        a=m*2
        os.system("sed -n %s,%sp %s > %s2.txt"%(m,a,fl,nm))
        b=m*3
        os.system("sed -n %s,%sp %s > %s3.txt"%(a,b,fl,nm))
        c=m*4
        os.system("sed -n %s,%sp %s > %s4.txt"%(b,c,fl,nm))

    elif jml == '5':
        m=int(brs/5)
        os.system("sed -n 1,%sp %s > %s1.txt"%(m,fl,nm))
        a=m*2
        os.system("sed -n %s,%sp %s > %s2.txt"%(m,a,fl,nm))
        b=m*3
        os.system("sed -n %s,%sp %s > %s3.txt"%(a,b,fl,nm))
        c=m*4
        os.system("sed -n %s,%sp %s > %s4.txt"%(b,c,fl,nm))
        d=m*5
        os.system("sed -n %s,%sp %s > %s5.txt"%(c,d,fl,nm))
                    
    elif jml == '6':
        m=int(brs/6)
        os.system("sed -n 1,%sp %s > %s1.txt"%(m,fl,nm))
        a=m*2
        os.system("sed -n %s,%sp %s > %s2.txt"%(m,a,fl,nm))
        b=m*3
        os.system("sed -n %s,%sp %s > %s3.txt"%(a,b,fl,nm))
        c=m*4
        os.system("sed -n %s,%sp %s > %s4.txt"%(b,c,fl,nm))
        d=m*5
        os.system("sed -n %s,%sp %s > %s5.txt"%(c,d,fl,nm))
        e=m*6
        os.system("sed -n %s,%sp %s > %s6.txt"%(d,e,fl,nm))
            
    elif jml == '7':
        m=int(brs/7)
        os.system("sed -n 1,%sp %s > %s1.txt"%(m,fl,nm))
        a=m*2
        os.system("sed -n %s,%sp %s > %s2.txt"%(m,a,fl,nm))
        b=m*3
        os.system("sed -n %s,%sp %s > %s3.txt"%(a,b,fl,nm))
        c=m*4
        os.system("sed -n %s,%sp %s > %s4.txt"%(b,c,fl,nm))
        d=m*5
        os.system("sed -n %s,%sp %s > %s5.txt"%(c,d,fl,nm))
        e=m*6
        os.system("sed -n %s,%sp %s > %s6.txt"%(d,e,fl,nm))
        f=m*7
        os.system("sed -n %s,%sp %s > %s7.txt"%(e,f,fl,nm))
        
    elif jml == '8':
        m=int(brs/8)
        os.system("sed -n 1,%sp %s > %s1.txt"%(m,fl,nm))
        a=m*2
        os.system("sed -n %s,%sp %s > %s2.txt"%(m,a,fl,nm))
        b=m*3
        os.system("sed -n %s,%sp %s > %s3.txt"%(a,b,fl,nm))
        c=m*4
        os.system("sed -n %s,%sp %s > %s4.txt"%(b,c,fl,nm))
        d=m*5
        os.system("sed -n %s,%sp %s > %s5.txt"%(c,d,fl,nm))
        e=m*6
        os.system("sed -n %s,%sp %s > %s6.txt"%(d,e,fl,nm))
        f=m*7
        os.system("sed -n %s,%sp %s > %s7.txt"%(e,f,fl,nm))
        g=m*8
        os.system("sed -n %s,%sp %s > %s8.txt"%(f,g,fl,nm))
        
    elif jml == '9':
        m=int(brs/9)
        os.system("sed -n 1,%sp %s > %s1.txt"%(m,fl,nm))
        a=m*2
        os.system("sed -n %s,%sp %s > %s2.txt"%(m,a,fl,nm))
        b=m*3
        os.system("sed -n %s,%sp %s > %s3.txt"%(a,b,fl,nm))
        c=m*4
        os.system("sed -n %s,%sp %s > %s4.txt"%(b,c,fl,nm))
        d=m*5
        os.system("sed -n %s,%sp %s > %s5.txt"%(c,d,fl,nm))
        e=m*6
        os.system("sed -n %s,%sp %s > %s6.txt"%(d,e,fl,nm))
        f=m*7
        os.system("sed -n %s,%sp %s > %s7.txt"%(e,f,fl,nm))
        g=m*8
        os.system("sed -n %s,%sp %s > %s8.txt"%(f,g,fl,nm))
        h=m*9
        os.system("sed -n %s,%sp %s > %s9.txt"%(g,h,fl,nm))
        
    elif jml == '10':
        m=int(brs/10)
        os.system("sed -n 1,%sp %s > %s1.txt"%(m,fl,nm))
        a=m*2
        os.system("sed -n %s,%sp %s > %s2.txt"%(m,a,fl,nm))
        a=m*2
        b=m*3
        os.system("sed -n %s,%sp %s > %s3.txt"%(a,b,fl,nm))
        c=m*4
        os.system("sed -n %s,%sp %s > %s4.txt"%(b,c,fl,nm))
        d=m*5
        os.system("sed -n %s,%sp %s > %s5.txt"%(c,d,fl,nm))
        e=m*6
        os.system("sed -n %s,%sp %s > %s6.txt"%(d,e,fl,nm))
        f=m*7
        os.system("sed -n %s,%sp %s > %s7.txt"%(e,f,fl,nm))
        g=m*8
        os.system("sed -n %s,%sp %s > %s8.txt"%(f,g,fl,nm))
        h=m*9
        os.system("sed -n %s,%sp %s > %s9.txt"%(g,h,fl,nm))
        i=m*10
        os.system("sed -n %s,%sp %s > %s10.txt"%(h,i,fl,nm))
        

    print("success")

#---------------------------------------------------------------------------------------------------------------------------


elif jawaban == "14":
	print ("\033[91mBelom ada tolol\033[92m")

#---------------------------------------------------------------------------------------------------------------------------


elif jawaban == "15":
	print("\033[96m 1.jam\n 2.nama\n 3.mata pelajaran")
	print("\033[96m a.1-2-3\nb.2-3-1\nc.3-1-2\nd.1-3-2\ne.3-2-1\nf.2-1-3")
	print("\033[96mPilih urutan dengan benar")
	plh=str(input("\033[91m>>> \033[93m"))

	print("\033[96mMasukan nama")
	nam=str(input("\033[91m>>> \033[93m"))
	print("\033[96mMasukan mata pelajaran harian")
	sn=str(input("\033[91m[senin]>>> \033[93m"))
	sl=str(input("\033[91m[selasa]>>> \033[93m"))
	rb=str(input("\033[91m[rabu]>>> \033[93m"))
	kms=str(input("\033[91m[Kamis]>>> \033[93m"))
	jmt=str(input("\033[91m[Jumat]>>> \033[93m"))

	kl=open("bot.py","w")
	kl.write("")
	kl=open("bot.py","a")
	kkl=open("awok.txt","r")

	kl.write('from selenium import webdriver as wb\nimport tkinter, threading, time, os, sys\n\na=0\nos.system("clear")\ndef thread():\n	animation = ["bot preparation","Bot preparation","bOt preparation","boT preparation","bot Preparation","bot pReparation","bot prEparation","bot preParation","bot prepAration","bot prepaRation","bot preparAtion","bot preparaTion","bot preparatIon","bot preparatiOn","bot preparatioN","bot preparation~","Bot preparation ","bOt preparation","boT preparation","bot Preparation","bot pReparation","bot prEparation","bot preParation","bot prepAration","bot prepaRation","bot preparAtion","bot preparaTion","bot preparatIon","bot preparatiOn","bot preparatioN","bot preparation~","Bot preparation ","bOt preparation","boT preparation","bot Preparation","bot pReparation","bot prEparation","bot preParation","bot prepAration","bot prepaRation","bot preparAtion","bot preparaTion","bot preparatIon","bot preparatiOn","bot preparatioN","bot preparation"]\n	for i in range(len(animation)):\n	    time.sleep(0.2)\n	    sys.stdout.write("\r\033[91m[\033[93m+\033[91m]\033[96m " + animation[i % len(animation)] )\n	    sys.stdout.flush()\n	    if a==1:\n	    	print("\033[92m")\n	    	sys.exit()\n	print("\033[92m")\nhari=("Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu")\nsekaran=time.time()\ninfowaktu= time.localtime()\nhari_ini=hari[infowaktu[6]]\nt=threading.Thread(target=thread)\nprint("absen hari ",hari_ini)\nt.start()\ntgl=infowaktu[2]\nbl=infowaktu[1]\nth=infowaktu[0]\n')
	kl.write('nama='+str(nam)+'\n')
	# mata_pelajaran=("SEJARAH INDO, Ekonomi, SEJARAH LM","SOSIO, AGAMA, B.ING","Seni Budaya, PENJAS, PKN","Geografi, KWU, LM Fisika, BK","Matematika, B.INDO")
	kl.write('mata_pelajaran=("'+str(sn)+'","'+str(sl)+'","'+str(rb)+'","'+str(kms)+'","'+str(jmt)+'")\n')
	kl.write(kkl.read())
	kl.write('d=wb.Firefox()\n')
	kl.write('d.get("https://docs.google.com/forms/d/e/1FAIpQLScfcO4DEAdN_3qIKzqosf9GnYstzHi84PF_yBH8MpFMbabExQ/viewform")\n')
	kl.write('a=1\n')
	def pp1(urut):
		kl.write('d.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div['+str(urut)+']/div/div/div[2]/div/div/div['+str(1)+']/div/div[2]/div[1]/div/div[1]/input").send_keys(tgl)\n')
		kl.write('d.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div['+str(urut)+']/div/div/div[2]/div/div/div['+str(3)+']/div/div[2]/div[1]/div/div[1]/input").send_keys(bl)\n')
		kl.write('d.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div['+str(urut)+']/div/div/div[2]/div/div/div['+str(5)+']/div/div[2]/div[1]/div/div[1]/input").send_keys(th)\n')
	def pp2(urut):
		kl.write('d.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div['+str(urut)+']/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(nama)\n')
	def pp3(urut):
		kl.write('d.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div['+str(urut)+']/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(mata_pelajaran)\n')

	if plh=="1":
		pp1(1)
		pp2(2)
		pp3(3)
	elif plh=="2":
		pp1(2)
		pp2(3)
		pp3(1)
	elif plh=="3":
		pp1(3)
		pp2(1)
		pp3(2)
	elif plh=="4":
		pp1(1)
		pp2(3)
		pp3(2)
	elif plh=="5":
		pp1(3)
		pp2(2)
		pp3(1)
	elif plh=="6":
		pp1(2)
		pp2(1)
		pp3(3)
	else:
		print("\033[91mJawab yang bener tolol!")

#---------------------------------------------------------------------------------------------------------------------------


elif jawaban == "16":
	print ("\033[91mBelom ada tolol\033[92m")

#---------------------------------------------------------------------------------------------------------------------------


else:
	print ("\033[91mJawab yang bener tolol\033[92m")



