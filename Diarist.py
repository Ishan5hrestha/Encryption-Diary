import msvcrt as m
import os
from os import system
import glob
import hashlib
import sys
from time import sleep

phrase = "phrase.set"
icfile = "key_check.set"
setting = ".set"
extension = ".dovah"
pkey = "hahahaa"

#colors
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))


def clear(): os.system('cls')

def checkphrase(pkey,key):
	g = open(phrase,"r",encoding="utf-8")
	read = g.read()
	if encrypt(pkey,key)==read:return 1
	else: return 0
	g.close()

def header():
	intro = """
	______  _____   ___  ______  _____  _____  _____ 
	|  _  \\|_   _| / _ \\ | ___ \\|_   _|/  ___||_   _|
	| | | |  | |  / /_\\ \\| |_/ /  | |  \\ `--.   | |  
	| | | |  | |  |  _  ||    /   | |   `--. \\  | |  
	| |/ /  _| |_ | | | || |\\ \\  _| |_ /\\__/ /  | |  
	|___/   \\___/ \\_| |_/\\_| \\_| \\___/ \\____/   \\_/  
	"""
	prRed(intro)
	prYellow("-By Parewa".rjust(80,' '))

def typewriter(x,time):
	for char in x:
		sleep(time)
		sys.stdout.write(char)
		sys.stdout.flush()

def hasher(key):
	try:
		key = key.encode()
		x = hashlib.sha224(key).hexdigest()
		return(int(str(x),16))
	except:
		return -1

def encrypt(key,text,dec=1):
	if __name__ == '__main__':
		encrypted = ""
		key = hasher(key)
		dupkey = key
		for i in range(len(text)):
			new = chr(ord(text[i])+ dec*(dupkey%10))
			encrypted = encrypted + new
			if dupkey==0: dupkey = key
			dupkey = int(dupkey/10)
		return encrypted	

def make(pkey):
	clear()
	done = 0
	prRed("Are you sure?? This can cause alot of damage!!!")
	print("> Enter the checkphrase")
	ch = input("> ")
	if checkphrase(pkey,ch)==1:
		for filename in glob.glob("*.txt"):
			with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
				content = f.read()
				x = encrypt(pkey,content)
				filename = filename.replace(".txt","")
				g = open(filename+extension,"w",encoding="utf-8")
				g.write(x)
				g.close()
				try:
					f.close()
					filename = filename+".txt"
					os.remove(filename)
					done = 1
				except OSError as e:
					prRed("Error! Couldn't Shred: ",e)
					return -1
		if done==1: prGreen("Make successful!!!")
		else: prYellow("Nothing to Make")
		m.getch()

def view(pkey):
	while True:
		clear()
		print("Which one?".center(30,'-'))
		files = []
		i = 0
		print((str(i)+". Back").center(5,' '))
		for filename in glob.glob("*"+extension):
			i += 1
			print((str(i)+". "+filename).center(5,' '))
			files.append(filename)

		try:
			ch = int(input(">"))
			if ch==0: break
			f = open(files[ch-1],"r",encoding="utf-8")
			content = f.read()
			x = encrypt(pkey,content,-1)
			f.close()
		except:
			print("No jokes!!!")
			return 0 

		clear()
		print(filename)

		typewriter(x,0.005)

		m.getch()

def keychange(pkey):
	success = 0
	clear()
	header()
	prRed("Are you sure?? This causes entire change. Dont foget the key!!!")
	print("> Enter Checkphrase")
	ch = input("> ")
	if checkphrase(pkey,ch)==1:
		print("!!!!!!!!!!!!!!")
		nkey1 = input("Enter New Key: ")
		nkey2 = input("Reenter the Key: ")
		nphrase = input("Enter a Checkphrase: ")
		if nkey1!=nkey2: return 0
		try:
			for filename in glob.glob("*"+extension):
				with open(os.path.join(os.getcwd(), filename), 'r',encoding="utf-8") as f: # open in readonly mode
					content = f.read()
					f.close()
					x = encrypt(pkey,content,-1)
					x = encrypt(nkey1,x)
					g = open(filename,"w",encoding="utf-8")
					g.write(x)
					g.close()
					m.getch()
			#making new check phrase
			g = open(phrase,"w",encoding="utf-8")
			g.write(encrypt(nkey1,nphrase))
			g.close()
			#changing settings file
			for filename in glob.glob("*"+setting):
				with open(os.path.join(os.getcwd(), filename), 'r',encoding="utf-8") as f: # open in readonly mode
					content = f.read()
					f.close()
					x = encrypt(pkey,content,-1)
					print(x)
					x = encrypt(nkey1,x)
					print(x)
					g = open(filename,"w",encoding="utf-8")
					g.write(x)
					g.close()
					m.getch()
			prGreen("Key changed Successfully!!!")
			prYellow("Please Restart the app!!!")
			m.getch()
			return(nkey1)
		except:
			prRed("Something Went Wrong")
			return -1
	else:
		return -1

def choice():
	header()
	prRed('Choices'.center(30,'-'))
	prYellow("1. Check Key".ljust(30,' '))
	prYellow("2. View All".ljust(30,' '))
	prYellow("3. Make Enc".ljust(30,' '))
	prYellow("4. Key Change".ljust(30,' '))
	prYellow("5. Quit".ljust(30,' '))

	try:
		ch = int(m.getch())
		return ch
	except:
		return -1

def keychecker(key):
	f=open(icfile,"r",encoding="utf-8")
	pic = f.read()
	pic = encrypt(key,pic,-1)
	pic = pic.replace("\\","\\\\")
	f.close()
	print(pic)
	m.getch()

def main():
	clear()
	header()
	print("KEYS")
	pkey = input()
	sleep(1)
	while True:
		clear()
		ch = choice()
		if ch==1:keychecker(pkey)
		elif ch==2:view(pkey)
		elif ch==3: make(pkey)
		elif ch==4: 
			if keychange(pkey)!=-1:break
		elif ch==5:break
		else: continue

#keychecker()
main()
#print(hasher("hahahaa"))
#make()
#view()
#m.getch()