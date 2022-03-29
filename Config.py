
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import pickle, os
from colorama import init, Fore
from time import sleep

init()

n = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [lg, r, w, cy, ye]

try:
    import requests
except ImportError:
    print(f'{lg}[i] Installing module - requests...{n}')
    os.system('pip install requests')

def banner():
    import random
    
    b = [   
   
    
    '  ',
    ' ░█▀▄▀█ █▀▀█ █── █── █▀▀█ 　 ▀▀█▀▀ █▀▀ █── █▀▀ █▀▀▀ █▀▀█ █▀▀█ █▀▄▀█ ',
    ' ░█░█░█ █▄▄█ █── █── █▄▄█ 　 ─░█── █▀▀ █── █▀▀ █─▀█ █▄▄▀ █▄▄█ █─▀─█ ',
    ' ░█──░█ ▀──▀ ▀▀▀ ▀▀▀ ▀──▀ 　 ─░█── ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀─▀▀ ▀──▀ ▀───▀ ',
    '                                      〸🝗㇄🝗Ꮆ尺闩爪 ',

    ' ========================================================',
    ]
    for char in b:
        print(f'{random.choice(colors)}{char}{n}')
        
    
    print(f'   📌  Silahkan Pilih Menu DiBawah Ini {n}\n')

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    clr()
    banner()
    print(lg+'[1] ☎️ Tambahkan Nomor Telegram'+n)
    print(lg+'[2] 👣 Cek Akun Banned'+n)
    print(lg+'[3] ✂️ Hapus Akun'+n)
    print(lg+'[4] ❌ Keluar'+n)
    a = int(input('\n✍️Masukkan Pilihan: '))
    if a == 1:
        new_accs = []
        with open('OTP.txt', 'ab') as g:
            number_to_add = int(input(f'\n{lg}  [📌] Masukkan Jumlah Akun Yang Akan Di Gunakan : {r}'))
            for i in range(number_to_add):
                phone_number = str(input(f'\n{lg}[📌] Masukkan Nomor Telegrammu: {r}'))
                parsed_number = ''.join(phone_number.split())
                pickle.dump([parsed_number], g)
                new_accs.append(parsed_number)
            print(f'\n{lg} [📌] Data Akun Tersimpan Di OTP.txt')
            clr()
            print(f'\n{lg} [📌] Cek Akun, Silahkan Tunggu ...\n')
            for number in new_accs:
                c = TelegramClient(f'sessions/{number}', 19286603 , '3f459e22ac139db64f0ddcd2c70ab1ba')
                c.start(number)
                print(f'{lg}[📌] Suskse')
                c.disconnect()
            input(f'\n 🔐 Kembali Kemenu Sebelumnya (press Enter)')

        g.close()
    elif a == 2:
        accounts = []
        banned_accs = []
        h = open('OTP.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(h))
            except EOFError:
                break
        h.close()
        if len(accounts) == 0:
            print(r+'[📌] Tidak ada akun! Silakan tambahkan beberapa akun dan coba lagi')
            sleep(3)
        else:
            for account in accounts:
                phone = str(account[0])
                client = TelegramClient(f'sessions/{phone}',19286603  , '3f459e22ac139db64f0ddcd2c70ab1ba')
                client.connect()
                if not client.is_user_authorized():
                    try:
                        client.send_code_request(phone)
                        #client.sign_in(phone, input('[+] Enter the code: '))
                        print(f'{lg}[+] {phone} ❌ is Aman banned{n}')
                    except PhoneNumberBannedError:
                        print(r+str(phone) + ' ⛔️ is banned!'+n)
                        banned_accs.append(account)
            if len(banned_accs) == 0:
                print(lg+'⭕️ Tidak ada akun yang diblokir.')
                input('\n🔐 Kembali ke menu sebelumnya (press Enter)')
            else:
                for m in banned_accs:
                    accounts.remove(m)
                with open('OTP.txt', 'wb') as k:
                    for a in accounts:
                        Phone = a[0]
                        pickle.dump([Phone], k)
                k.close()
                print(lg+'[📌] Semua akun yang dibanned dihapus'+n)
                input('\n🔐 Kembali ke menu sebelumnya (press Enter)')

    elif a == 3:
        accs = []
        f = open('OTP.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()
        i = 0
        print(f'{lg}[📌] Pilih akun yang akan dihapus \n')
        for acc in accs:
            print(f'{lg}[{i}] {acc[0]}{n}')
            i += 1
        index = int(input(f'\n{lg}[📌] Masukkan Pilihan: {n}'))
        phone = str(accs[index][0])
        session_file = phone + '.session'
        if os.name == 'nt':
            os.system(f'del sessions\\{session_file}')
        else:
            os.system(f'rm sessions/{session_file}')
        del accs[index]
        f = open('OTP.txt', 'wb')
        for account in accs:
            pickle.dump(account, f)
        print(f'\n{lg}[📌] Akun Di Hapus {n}')
        input(f'\n🔐 Kembali ke menu sebelumnya (press Enter)')
        f.close()
    elif a == 4:
         
       
 
        clr()
        banner()
        exit()
