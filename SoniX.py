import os
import subprocess
import time

merah = '\033[31m'
hijau = '\033[32m'
kuning = '\033[33m'
biru = '\033[34m'
magenta = '\033[35m'
cyan = '\033[36m'
putih = '\033[37m'
reset = '\033[0m'

def clear_screen():
    os.system("clear")

def print_sonix_logo():
    logo = f"""{magenta}
 ____              ___  __
/ ___|  ___  _ __ (_) \/ /
\___ \ / _ \| '_ \| |\  /
 ___) | (_) | | | | |/  \\
|____/ \___/|_| |_|_/_/\_\\
CREATED BY : C10F-UNKNOWN404
{reset}
    """
    print(logo)

def menu(nama):
    print(f"{hijau}HALO {nama}, SELAMAT DATANG DI TOOLS SONIX BY C10F{reset}")
    print(f"{kuning}===================================================>{reset}")
    print(f"{magenta}[1]> BELAJAR TENTANG RAT{reset}")
    print(f"{kuning}==================================================>{reset}")
    print(f"{magenta}[2]> APA ITU CYBER SECURITY{reset}")
    print(f"{kuning}==================================================>{reset}")
    print(f"{magenta}[3]> CARA JADI HACKER{reset}")
    print(f"{kuning}===================================================>{reset}")
    print(f"{magenta}[4]> CARA RESET HP JARAK JAUH MELALUI EMAIL{reset}")
    print(f"{kuning}===================================================>{reset}")
    print(f"{magenta}[5]> EXIT{reset}")
    print(f"{kuning}===================================================>{reset}")
    
def BELAJAR_TENTANG_RAT():
    os.system(f"figlet -f slant RAT")
    print(f"{merah}RAT adalah singkatan dari Remote Access Trojan. Ini adalah jenis perangkat lunak berbahaya yang memungkinkan penyerang untuk mengendalikan komputer target dari jarak jauh tanpa pengetahuan atau izin pemiliknya.{reset}")

def APA_ITU_CYBER_SECURITY():
    os.system(f"figlet -f slant Cyber Security")
    print(f"{biru}Keamanan cyber, atau sering disebut 'cybersecurity', adalah praktik dan teknologi yang dirancang untuk melindungi sistem komputer, jaringan, perangkat, dan data dari ancaman dan serangan cyber. Ini mencakup berbagai strategi seperti enkripsi data, pemantauan keamanan jaringan, pembaruan perangkat lunak, pendidikan pengguna, dan implementasi kebijakan keamanan. Tujuannya adalah untuk mencegah akses yang tidak sah, pencurian data, gangguan layanan, dan kerusakan lainnya yang dapat disebabkan oleh pihak yang tidak berwenang atau malware.{reset}")

def CARA_JADI_HACKER():
    os.system(f"figlet -f slant Hacker")
    print(f"{hijau}Saya tidak dapat memberikan panduan atau bimbingan tentang cara menjadi hacker. Menjadi hacker yang etis dan profesional melibatkan pemahaman yang luas tentang teknologi informasi, keamanan komputer, dan etika. Lebih baik fokus pada karier dalam keamanan cyber yang positif, seperti menjadi ahli keamanan yang membantu melindungi sistem dari serangan cyber, daripada mencari cara untuk mengeksploitasi atau merusak sistem.{reset}")

def CARA_RESET_HP_JARAK_JAUH_MELALUI_EMAIL():
    os.system(f"figlet -f slant Reset HP")
    print(f"{cyan}Cara mereset HP jarak jauh melalui email adalah dengan menggunakan aplikasi [Cari Perangkat Saya].{reset}")
    print("Downloadnya di mana?")
    print(f"{merah}Downloadnya di Play Store.{reset}")

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

# Run the functions
clear_screen()

os.system("figlet Verifikasi")
nama = input(f"{merah}MASUKAN USERNAME ANDA: {reset}")
print(f"{magenta}MEMASUKI TOOLS SONIX...{reset}")
print(f"{hijau}LOADING...{reset}")
time.sleep(3)

clear_screen()
print_sonix_logo()

while True:
    menu(nama)
    choice = input(f"{merah}Please select: {reset}")
    if choice == "1":
        BELAJAR_TENTANG_RAT()
    elif choice == "2":
        APA_ITU_CYBER_SECURITY()
    elif choice == "3":
        CARA_JADI_HACKER()
    elif choice == "4":
        CARA_RESET_HP_JARAK_JAUH_MELALUI_EMAIL()
    elif choice == "5":
        break
    else:
        print(f"{merah}Pilihan tidak valid{reset}")
    time.sleep(5)
    clear_screen()
    print_sonix_logo()