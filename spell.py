import requests
from time import sleep
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from datetime import datetime
import pytz

console = Console()
tz = pytz.timezone('Asia/Jakarta')

banner = """[blue]
███████╗██████╗ ███████╗██╗     ██╗     
██╔════╝██╔══██╗██╔════╝██║     ██║     
███████╗██████╔╝█████╗  ██║     ██║     
╚════██║██╔═══╝ ██╔══╝  ██║     ██║     
███████║██║     ███████╗███████╗███████╗
╚══════╝╚═╝     ╚══════╝╚══════╝╚══════╝
                            @kambingnoob 
1. [green]Complete all task [/green]
2. [red]Upgrade Boost (soon)[/red]
3. [red]Upgrade Storage (soon)[/red]
4. [green]Auto Claim[/green]
"""

console.print(Panel(banner, title="[bold blue]Spell Bot Menu[/bold blue]"))

pilihan = Prompt.ask("Masukan pilihan")

def completetask(token, akunke, total_akun):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'authorization': token,
        'origin': 'https://wallet.spell.club',
        'referer': 'https://wallet.spell.club/',
    }
    params = {
        'batch_mode': 'true',
    }
    
    tasklist = []
    r = requests.get('https://wapi.spell.club/quest/1', headers=headers)
    for task in r.json()['steps']:
        tasklist.append(task['id'])
    for task in tasklist:
        response = requests.post('https://wapi.spell.club/quest/step/' + str(task) + '/complete', headers=headers)
        if response.status_code == 200:
            console.print(f"[bold royal_blue1][{datetime.now(tz).strftime('%H:%M:%S')}] [bold green]Akun [{akunke}/{total_akun}] [bold blue]=>[bold spring_green2] Task {task} Success [reset]")
        elif response.status_code == 400:
            console.print(f"[bold royal_blue1][{datetime.now(tz).strftime('%H:%M:%S')}] [bold green]Akun [{akunke}/{total_akun}] [bold blue]=>[bold yellow2] Task {task} Already Completed [reset]")
    try:
        response = requests.post('https://wapi.spell.club/quest/1/claim', params=params, headers=headers)
        while response.status_code == 500:
            response = requests.post('https://wapi.spell.club/quest/1/claim', params=params, headers=headers)
        claimid = response.json()['id']
        console.print(f"[bold royal_blue1][{datetime.now(tz).strftime('%H:%M:%S')}] [bold green]Akun [{akunke}/{total_akun}] [bold blue]=>[bold spring_green2] Success Claim {claimid} [reset]")
    except:
        console.print(f"[bold royal_blue1][{datetime.now(tz).strftime('%H:%M:%S')}] [bold green]Akun [{akunke}/{total_akun}] [bold red]=>[bold deep_pink2] {response.status_code} {response.json()['message']} [reset]")
def upgradelab(token, akunke, total_akun):
    pass
def autoclaim(token, akunke, total_akun):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'authorization': token,
        'origin': 'https://wallet.spell.club',
        'referer': 'https://wallet.spell.club/',
    }
    params = {
        'batch_mode': 'true',
    }
    try:
        response = requests.post('https://wapi.spell.club/claim', params=params, headers=headers)
        while response.status_code == 500:
            response = requests.post('https://wapi.spell.club/claim', params=params, headers=headers)
        claimid = response.json()['id']
        r = requests.get('https://wapi.spell.club/user', headers=headers).json()
        balance = r['balance']
        console.print(f"[bold royal_blue1][{datetime.now(tz).strftime('%H:%M:%S')}] [bold green]Akun [{akunke}/{total_akun}] [bold blue]=>[bold spring_green2] Success Claim {claimid} | Balance: {balance / 1000000} MANA[reset]")
    except:
        console.print(f"[bold royal_blue1][{datetime.now(tz).strftime('%H:%M:%S')}] [bold green]Akun [{akunke}/{total_akun}] [bold red]=>[bold deep_pink2] {response.status_code} {response.json()['message']} [reset]")
        
with open("data.txt", "r") as file:
    token_list = file.readlines()

if pilihan == "1":
    total_akun = len(token_list)
    for i, token in enumerate(token_list, start=1):
        completetask(token.strip(), i, total_akun)  
        
elif pilihan == "2":
    console.print(f"[bold royal_blue1][{datetime.now(tz).strftime('%H:%M:%S')}] [bold red]Soon bang kalo g males[reset]")  
        
elif pilihan == "3":
    console.print(f"[bold royal_blue1][{datetime.now(tz).strftime('%H:%M:%S')}] [bold red]Soon bang kalo g males[reset]")    
        
elif pilihan == "4":
    total_akun = len(token_list)
    while True:
        for i, token in enumerate(token_list, start=1):
            autoclaim(token.strip(), i, total_akun)
        detik = 3600

        menit = detik // 60
        sisadetik = detik % 60
        console.print(f"[bold royal_blue1][{datetime.now(tz).strftime('%H:%M:%S')}] [bold blue]Menunggu {menit} menit {sisadetik} detik untuk claim lagi[reset]")
        sleep(detik)
else:
    exit()
