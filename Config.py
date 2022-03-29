
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
 
' 7777777777~:                               7PPP?      !!!!!!!~~~^.                      ?55P!  ^5555',
' PPPPPPPPGGPPJ:                             ?PPP?     .5PPPGGGGGPP5J^                    JPPG7  ^PPPP',
' 5PPP7::^~JPPPP^                            ?PPP?     .5PPP?~~~!YPPPP:                   JPPP!  ^PPPP',
' 5PPG!     5PPGJ                            ?PPP?     .5PPP~    :PPPG!                   JPPP!  ^PPPP',
' PPPG! ::^?PPPP~   :!?YYYYJ!:       ^7?JJ?!:JPPP?     .5PPP~ ~!7YPPP?    ^~~~.    :~~~^  JPPP!  ^PPPP',
' PPPG~.PPPPP5J^  :JPGPJ77YPPPJ.   ~YPPGP55PPPPPP?     .5PPP~ PGGGPP57:  .PPPG^    7GPGY  JPPP!  ^PPPP',
' PPPG~:PPP5^.   .5PPP?^::^JPPGJ  !PPPP?:..:7PPPP?     .5PPP~ ~~!7JPPPP7 .5PPP^    !PPPJ  JPPP!  ^PPPP',
' PPPG~ JPPPJ:   ~GPPP555555555Y. JPPP5      JPPP?     .5PPP~      7PPPG^ 5PPP^    7PPPJ  JPPP!  ^PPPP',
' PPPG!  7PPPP!  .5PPP7....^~^..  !GPPP7.  .~5PPP?     .5PPP! ....:YPPPP: 5PPP!    JPPPJ  JPPP!  ^PPPP',
' PPPG!   ^5PPGJ: :YPPPYJ?JPGPY:   7PPPG5YY5GPPPG?     .5PPPP55555PGPP5~  ?PPPPJ7?YPPPP~  YPPG7  ^PPPP',
' JJJJ^    .JYYYJ:  ^?Y5555YJ!:     :!J555YJ~?YYY7     .JYYYYYYYYYYJ7~.    ^?YPPGGP5Y?:   ?555!  :5555',
'                      ...              ..                                    .:^^:.       ...    ....',
'                                                 .....                                               ',
'                                            .:~~!!!!!!~~:.                                           ',
'                        :.              ...^!77!!!!!!!!77!^...              .:                       ',
'                       .?JJ~        :~7J555J7!!!!!!!!!!!!7J555J7~:        ~JJ?.                      ',
'                        :??:  ..:7JYPPPPP5PPPY7!!!!!!!!7YPPP5PPPPPYJ7:..  :??:                       ',
'                       J?.:~J55PPPPPPPPPPPPPPP?!!!!!!?PPPPPPPPPPPPPPP55J~:.?J                       ',
'                        .~!7PPPPPPPPPPPPP5PPP555!!!!!!555PPP5PPPPPPPPPPPPP7!~.                       ',
'                          .~5PP5JJJYYJ5PYJJ5PPPPJ7!!7JPPPP5JJYP5JYYJJJ5PP5~.                         ',
'                      .~7?55YJJ7:  ^JJY55J755YYYYJ!!JYYYY557J55YJJ^  :?JJY55?7~.                     ',
'                      ^7J7^:        :!!~:..^!!!!77!!77!!!!^..:~!!:        :^7J7^                     ',
'                                             :^~!!!!!!~^.                                            ',
    
 
    ' ========================================================',
    ' 👽 Telegram Member Pro 💪',
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
