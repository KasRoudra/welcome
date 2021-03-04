import os
import sys
os.system("pkg install figlet")
os.system("pkg install mpv -y")
os.system("rm -rf ~/../usr/etc/motd")
print("\n\nEnter your name to displayed on home")
b=input()
print("Enter Welcome text")
c=input()
bs=open("bash.bashrc",'a')
print('''if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
	command_not_found_handle() {
		/data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
	}
fi

PS1='\$ '
mpv ~/welcome/wc.mp3 
clear
figlet''', b, "\necho", c, file=bs) 
bs.close()
os.system("rm -rf ~/../usr/etc/bash.bashrc")
os.system("mv -f bash.bashrc ~/../usr/etc")
zs=open("zshrc",'a')
print('''. /data/data/com.termux/files/usr/etc/profile
command_not_found_handler() {
	/data/data/com.termux/files/usr/libexec/termux/command-not-found $1
}
#set nomatch so *.sh would not error if no file is available
setopt +o nomatch
. /data/data/com.termux/files/usr/etc/profile
PS1='%# '
mpv ~/welcome/wc.mp3 
clear
figlet''', b, "\necho", c, file=zs) 
zs.close()
os.system("rm -rf ~/../usr/etc/zshrc")
os.system("mv -f zshrc  ~/../usr/etc")
os.system("clear")
print("Please restart Termux")
exit()
