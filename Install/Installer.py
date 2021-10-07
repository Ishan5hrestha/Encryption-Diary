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
ckey = "ofcourse"

def clear(): os.system('cls')




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


def main():
	clear()
	key = input("KEY> ")
	checker = input("CHECKER> ")
	f=open("ikchk.set","r",encoding="utf-8")
	g=open(icfile,"w",encoding="utf-8")
	pic = f.read()
	pic = encrypt(key, pic)
	g.write(pic)
	f.close()
	g.close()

	f=open("ipc.set","r",encoding="utf-8")
	g=open(phrase,"w",encoding="utf-8")
	pic = f.read()
	pic = encrypt(key, ckey)
	g.write(pic)
	f.close()
	g.close()

	f=open("example.txt","r",encoding="utf-8")
	g=open("example.dovah","w",encoding="utf-8")
	pic = f.read()
	pic = encrypt(key, pic)
	g.write(pic)
	f.close()
	g.close()

#keychecker()
main()
#print(hasher("hahahaa"))
#make()
#view()
#m.getch()