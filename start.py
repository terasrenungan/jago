
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChannel
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, PhoneNumberBannedError, ChatAdminRequiredError
from telethon.errors.rpcerrorlist import ChatWriteForbiddenError, UserBannedInChannelError, UserAlreadyParticipantError, FloodWaitError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
from telethon.tl.functions.messages import ImportChatInviteRequest, AddChatUserRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import UserStatusRecently
import time
import random
from colorama import init, Fore
import os
import pickle


init()


r = Fore.RED
lg = Fore.GREEN
rs = Fore.RESET
w = Fore.WHITE
grey = '\033[97m'
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [r, lg, w, ye, cy]
info = lg + '[' + w + 'i' + lg + ']' + rs
error = lg + '[' + r + '!' + lg + ']' + rs
success = w + '[' + lg + '*' + w + ']' + rs
INPUT = lg + '[' + cy + '~' + lg + ']' + rs
plus = w + '[' + lg + '+' + w + ']' + rs
minus = w + '[' + lg + '-' + w + ']' + rs

def banner():
     
    b = [    
    '   ███████╗██╗  ██╗██╗   ██╗     ██╗  ██╗██╗  ██╗██╗  ██╗ ██████╗ ██████╗  ',         
    '   ██╔════╝██║ ██╔╝╚██╗ ██╔╝     ██║  ██║██║  ██║╚██╗██╔╝██╔═══██╗██╔══██╗ ' ,      
    '   ███████╗█████╔╝  ╚████╔╝      ███████║███████║ ╚███╔╝ ██║   ██║██████╔╝ '  ,       
    '   ╚════██║██╔═██╗   ╚██╔╝       ██╔══██║╚════██║ ██╔██╗ ██║   ██║██╔══██╗   ' ,      
    '   ███████║██║  ██╗   ██║███████╗██║  ██║     ██║██╔╝ ██╗╚██████╔╝██║  ██║██╗  ',     
    '   ╚══════╝╚═╝  ╚═╝   ╚═╝╚══════╝╚═╝  ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝    ', 
    '                                           /=\        |        |         ' ,
    '                                            \  /=| /= =/ /=\ /=| /=\ /== ' ,
    '                                           \=/ \=| |  |\ \=/ \=| \=  ==/  ' ,  
    ' ========================================================',
    ' 👽 Telegram Member Pro V2 💪',
    ' ========================================================',
    ]
    for char in b:
        print(f'{random.choice(colors)}{char}{rs}')

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

accounts = []
f = open('OTP.txt', 'rb')
while True:
    try:
        accounts.append(pickle.load(f))
    except EOFError:
        break

# TODO:  
print('\n' + info + lg + '🔍 Cek akun yang dibanned...' + rs)
for a in accounts:
    phn = a[0]
    print(f'{plus}{grey} Checking {lg}{phn}')
    clnt = TelegramClient(f'sessions/{phn}',  19286603, '3f459e22ac139db64f0ddcd2c70ab1ba')
    clnt.connect()
    banned = []
    if not clnt.is_user_authorized():
        try:
            clnt.send_code_request(phn)
            print('OK')
        except PhoneNumberBannedError:
            print(f'{error} {w}{phn} {r}⛔️ is banned!{rs}')
            banned.append(a)
    for z in banned:
        accounts.remove(z)
        print(info+lg+'❌ Kembali Ke Setting.bat Untuk Menghapus Akun Yang DiBanned'+rs)
    time.sleep(0.5)
    clnt.disconnect()


print(info+' Sessions created!')
clr()
banner()
 
def log_status(scraped, index):
    with open('status.dat', 'wb') as f:
        pickle.dump([scraped, int(index)], f)
        f.close()
    print(f'{info}{lg} Session stored in {w}status.dat{lg}')
    

def exit_window():
    input(f'\n{cy} 📍 Tekan ENTER Untuk Keluar...')
    clr()
    banner()
    sys.exit()

 
try:
    
    with open('status.dat', 'rb') as f:
        status = pickle.load(f)
        f.close()
        lol = input(f'{INPUT}{cy} ✍️ Resume scraping members from {w}{status[0]}{lg}? [y/n]: {r}')
        if 'y' in lol:
            scraped_grp = status[0] ; index = int(status[1])
        else:
            if os.name == 'nt': 
                os.system('del status.dat')
            else: 
                os.system('rm status.dat')
            scraped_grp = input(f'{INPUT}{cy} ⚙️ Masukkan Link Group Target Dengan Format [https://t.me/NamaGroup] Atau [https://t.me/joinchat/xxxxxxxxx]  : {r}')
            index = 0
except:
    scraped_grp = input(f'{INPUT}{cy} ⚙️ Masukkan Link Group Target Dengan Format [https://t.me/NamaGroup] Atau [https://t.me/joinchat/xxxxxxxxx] : {r}')
    index = 0
 
accounts = []
f = open('OTP.txt', 'rb')
while True:
    try:
        accounts.append(pickle.load(f))
    except EOFError:
        break

print(f'{info}{lg} ✂️ Total Akun: {w}{len(accounts)}')
number_of_accs = int(input(f'{INPUT}{cy} ✍️ Masukkan Jumlah Akun Yang DI Gunakan : {r}'))
print(f'{info}{cy} 📍 Pilih {lg}')
print(f'{cy}[0]{lg}📍 Tambah Ke Group Public')
print(f'{cy}[1]{lg}📍 Tambah Ke Group Private')
choice = int(input(f'{INPUT}{cy} 📍 Masukkan Pilihan: {r}'))
if choice == 0:
    target = str(input(f'{INPUT}{cy} 📍 Masukkan link grup public : {r}'))
else:
    target = str(input(f'{INPUT}{cy} 📍 Masukkan link grup private : {r}'))
print(f'{grey}_'*50)
 
to_use = [x for x in accounts[:number_of_accs]]
for l in to_use: accounts.remove(l)
with open('OTP.txt', 'wb') as f:
    for a in accounts:
        pickle.dump(a, f)
    for ab in to_use:
        pickle.dump(ab, f)
    f.close()
sleep_time = int(input(f'{INPUT}{cy} Masukkan Waktu Delay {w}[{lg}0 for None{w}]: {r}'))
 
print(f'{success}{lg} 📌 Tambah Member Dari {w}{len(to_use)}{lg} Akun(s) --')
adding_status = 0
approx_members_count = 0
for acc in to_use:
    stop = index + 60
    c = TelegramClient(f'sessions/{acc[0]}', 19286603 , '3f459e22ac139db64f0ddcd2c70ab1ba')
    print(f'{plus}{grey} User: {cy}{acc[0]}{lg} -- {cy}Starting session... ')
    c.start(acc[0])
    acc_name = c.get_me().first_name
    try:
        if '/joinchat/' in scraped_grp:
            g_hash = scraped_grp.split('/joinchat/')[1]
            try:
                c(ImportChatInviteRequest(g_hash))
                print(f'{plus}{grey} User: {cy}{acc_name}{lg} 📌 Bergabung dengan grup untuk Scrape')
            except UserAlreadyParticipantError:
                pass 
        else:
            c(JoinChannelRequest(scraped_grp))
            print(f'{plus}{grey} User: {cy}{acc_name}{lg} 📌 Bergabung dengan grup untuk Scrape')
        scraped_grp_entity = c.get_entity(scraped_grp)
        if choice == 0:
            c(JoinChannelRequest(target))
            print(f'{plus}{grey} User: {cy}{acc_name}{lg} 📌 Bergabung dengan grup untuk ADD')
            target_entity = c.get_entity(target)
            target_details = InputPeerChannel(target_entity.id, target_entity.access_hash)
        else:
            try:
                grp_hash = target.split('/joinchat/')[1]
                c(ImportChatInviteRequest(grp_hash))
                print(f'{plus}{grey} User: {cy}{acc_name}{lg} 📌 Bergabung dengan grup untuk ADD')
            except UserAlreadyParticipantError:
                pass
            target_entity = c.get_entity(target)
            target_details = target_entity
    except Exception as e:
        print(f'{error}{r} User: {cy}{acc_name}{lg}📌 Gagal bergabung dengan grup')
        print(f'{error} {r}{e}')
        continue
    print(f'{plus}{grey} User: {cy}{acc_name}{lg} 📌 {cy}Retrieving entities...')
   
    try:
        members = []
        members = c.get_participants(scraped_grp_entity, aggressive=False)
    except Exception as e:
        print(f'{error}{r} Tidak Dapat Scrape Member')
        print(f'{error}{r} {e}')
        continue
    approx_members_count = len(members)
    assert approx_members_count != 0
    if index >= approx_members_count:
        print(f'{error}{lg}Tidak Ada Members Untuk Di ADD!')
        continue
    print(f'{info}{lg} Start: {w}{index}')
   
    peer_flood_status = 0
    for user in members[index:stop]:
        index += 1
        if peer_flood_status == 10:
            print(f'{error}{r} 📌 Ada begitu banyak kesalahan! Sesi terakhir ...')
            break
        try:
            if choice == 0:
                c(InviteToChannelRequest(target_details, [user]))
            else:
                c(AddChatUserRequest(target_details.id, user, 42))
            user_id = user.first_name
            target_title = target_entity.title
            print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- {cy}{user_id} {lg}--> {cy}{target_title}')
           
            adding_status += 1
            print(f'{info}{grey} ❌ User: {cy}{acc_name}{lg} -- Sleep {w}{sleep_time} {lg}second(s)')
            time.sleep(sleep_time)
        except UserPrivacyRestrictedError:
            print(f'{minus}{grey} ❌ User: {cy}{acc_name}{lg} -- {r}📌 Member Memakai Privacy ')
            continue
        except PeerFloodError:
            print(f'{error}{grey} ❌ User: {cy}{acc_name}{lg} -- {r}📌 Terdeteksi Flood.')
            peer_flood_status += 1
            continue
        except ChatWriteForbiddenError:
            print(f'{error}{r} ❌ Tidak dapat menambahkan ke grup. Hubungi admin grup untuk mengaktifkan ADD Member')
            if index < approx_members_count:
                log_status(scraped_grp, index)
            exit_window()
        except UserBannedInChannelError:
            print(f'{error}{grey} User: {cy}{acc_name}{lg} -- {r}DiBanned Nulis Chat DI Group')
            break
        except ChatAdminRequiredError:
            print(f'{error}{grey} User: {cy}{acc_name}{lg} -- {r}Chat Admin Untuk ADD Member')
            break
        except UserAlreadyParticipantError:
            print(f'{minus}{grey} User: {cy}{acc_name}{lg} -- {r}Member Sudah ADA ')
            continue
        except FloodWaitError as e:
            print(f'{error}{r} {e}')
            break
        except ValueError:
            print(f'{error}{r} ❌ Kesalahan dalam Entitas')
            continue
        except KeyboardInterrupt:
            print(f'{error}{r} ---- Proses Di Hentikan ----')
            if index < len(members):
                log_status(scraped_grp, index)
            exit_window()
        except Exception as e:
            print(f'{error} {e}')
            continue
 
if adding_status != 0:
    print(f"\n{info}{lg} ❤️ Proses Selesai")
try:
    if index < approx_members_count:
        log_status(scraped_grp, index)
        exit_window()
except:
    exit_window()
