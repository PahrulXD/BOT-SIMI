from rich.console import Console
from rich.panel import Panel
from time import sleep as s
import requests, sys, os, time, random

logo = ('''\033[0;97m
  ____        _      _____ _           _ 
 |  _ \      | |    / ____(_)         (_)
 | |_) | ___ | |_  | (___  _ _ __ ___  _ 
 |  _ < / _ \| __|  \___ \| | '_ ` _ \| |
 | |_) | (_) | |_   ____) | | | | | | | |
 |____/ \___/ \__| |_____/|_|_| |_| |_|_|   

ketik ( stop ) untuk menghentikan program''')

def proccess():
    for i in list("\|/-"):
        print(f"\r\033[0;97m[\033[0;92m{i}\033[0;97m] sedang mengetik...",end="")
        time.sleep(0.5)

def bot():
        os.system('clear')
        print(logo)
        while True:
                print(f"\n")
                pesan = input(f'     \033[1;90mKetik pesan\r \033[1;91m>\033[1;92m ')
                print('\033[4A');Console().print(Panel('[white]'+pesan, style='green'), justify='right')
                if pesan in ["stop","Stop"]:exit()
                print(f"\n");proccess()
                simi = requests.get(f'https://api.simsimi.net/v2/?text={pesan}&lc=id&cf=false')
                balasan_simi = simi.json().get('success')
                print('\033[3A');Console().print(Panel('[white]'+balasan_simi, style='purple'), justify='left')
                
bot()