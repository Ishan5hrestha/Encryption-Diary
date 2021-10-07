# Hash based Encryption Diary
## Installation
- Run Installer.py first inside Install folder
- Copy All the files it produces to base folder
- Run Diarist.py and use the key you created in installation
- View the files


By default:  
- KEY: hahahaa  
- CheckPhrase: ofcourse  

## Working
The main KEY made during installation is turned into hash of numeric digits. These digits are added to each letter in a looping manner.  
For example:  
If hashed value = 1023  
Our text = apple  
Our hashed text would be : (a+1)(p+0)(p+2)(l+3)(e+1) = bprof  
Uses two passwords:  
- KEY for hashing
- CheckPhrase for confirmation


Add any .txt file on the root directory and run the code.  
Enter main key then select make to encrypt.  
Select View to decrypt  

This deletes the main txt file and makes new .dovah file  

.set files are for its settings.  
Watch video [here](https://www.youtube.com/watch?v=7FrJ9ksalcA)
