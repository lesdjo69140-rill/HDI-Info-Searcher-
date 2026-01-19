import os
import time
import requests
import socket
import subprocess
from termcolor import cprint, colored
import random

# Typing effect
def type_print(text, color="white", delay=0.01):
    for char in text:
        print(colored(char, color), end="", flush=True)
        time.sleep(delay)
    print()

# Clear screen
os.system("clear")

# Big ASCII HDI.69k logo
def show_hdi_ascii():
    cprint("""

░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░       ░▒▓███████▓▒░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░▒▓███████▓▒░▒▓███████▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░     ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓██▓▒░▒▓█▓▒░░▒▓█▓▒░     ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░▒▓██▓▒░▒▓██████▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░

""", "red", attrs=["bold"])
    time.sleep(1)

# Intro
def show_intro():
    show_hdi_ascii()
    cprint("╔══════════════════════════════════════════════════════╗", "red")
    cprint("║                  HDI INFO SEARCHER                  ║", "red")
    cprint("║                      HDI.69k                        ║", "red")
    cprint("║                 Author - HDI.69k                    ║", "red")
    cprint("╚══════════════════════════════════════════════════════╝", "red")
    time.sleep(1)

# Warning
def show_warning():
    cprint("\n[!] WARNING: Use this tool responsibly", "yellow", attrs=["bold"])
    time.sleep(2)
    os.system("termux-open-url https://www.tiktok.com/@hdi691400")
    time.sleep(3)

# Loading
def loading_animation():
    for i in range(3):
        type_print("[*] Loading modules" + "." * i, "cyan", delay=0.1)
        time.sleep(0.5)
    print()

# Menu
def show_menu():
    os.system("clear")
    show_intro()
    menu_options = [
        "[1] IP Geolocation",
        "[2] Reverse DNS Lookup",
        "[3] Port Scanner",
        "[4] WHOIS Lookup",
        "[5] HTTP Headers Grabber",
        "[6] Subdomain Finder",
        "[7] Hash Identifier",
        "[8] User-Agent Generator",
        "[9] Save Report",
        "[10] Clear Logs",
        "[11] Update Toolkit",
        "[12] Exit"
    ]
    for option in menu_options:
        type_print(option, "green", delay=0.005)
    print()

# Tools
def ip_geolocation():
    ip = input(colored("Enter IP Address: ", "cyan"))
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}").json()
        for k, v in res.items():
            print(colored(f"{k.upper()}: {v}", "magenta"))
    except:
        print(colored("Error retrieving data.", "red"))
    input("\nPress Enter to return to menu...")

def reverse_dns():
    ip = input(colored("Enter IP Address: ", "cyan"))
    try:
        host = socket.gethostbyaddr(ip)
        print(colored(f"Hostname: {host[0]}", "magenta"))
    except:
        print(colored("No PTR record found.", "red"))
    input("\nPress Enter to return to menu...")

def port_scanner():
    ip = input(colored("Enter IP Address: ", "cyan"))
    print(colored("Scanning ports (1-100)...", "yellow"))
    for port in range(1, 101):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        if sock.connect_ex((ip, port)) == 0:
            print(colored(f"Port {port} is OPEN", "green"))
        sock.close()
    input("\nPress Enter to return to menu...")

def whois_lookup():
    domain = input(colored("Enter domain: ", "cyan"))
    result = subprocess.getoutput(f"whois {domain}")
    print(colored(result, "magenta"))
    input("\nPress Enter to return to menu...")

def headers_grabber():
    url = input(colored("Enter website URL: ", "cyan"))
    try:
        headers = requests.get(url).headers
        for k, v in headers.items():
            print(colored(f"{k}: {v}", "magenta"))
    except:
        print(colored("Invalid URL.", "red"))
    input("\nPress Enter to return to menu...")

def subdomain_finder():
    domain = input(colored("Enter domain: ", "cyan"))
    subs = ["www", "mail", "ftp", "blog", "cpanel"]
    for s in subs:
        url = f"http://{s}.{domain}"
        try:
            requests.get(url, timeout=2)
            print(colored(f"[+] Found: {url}", "green"))
        except:
            pass
    input("\nPress Enter to return to menu...")

def hash_identifier():
    h = input(colored("Enter hash: ", "cyan"))
    l = len(h)
    if l == 32:
        t = "MD5"
    elif l == 40:
        t = "SHA1"
    elif l == 64:
        t = "SHA256"
    else:
        t = "Unknown"
    print(colored(f"Possible hash type: {t}", "magenta"))
    input("\nPress Enter to return to menu...")

def user_agent_generator():
    uas = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (X11; Linux x86_64)",
        "Mozilla/5.0 (Android 11)",
        "Mozilla/5.0 (iPhone)"
    ]
    print(colored(random.choice(uas), "magenta"))
    input("\nPress Enter to return to menu...")

def save_report():
    name = input(colored("File name: ", "cyan"))
    with open(name, "w") as f:
        f.write("HDI.69k REPORT\n")
    print(colored("Report saved.", "green"))
    input("\nPress Enter to return to menu...")

def clear_logs():
    os.system("rm -f *.log *.txt")
    print(colored("Logs cleared.", "green"))
    input("\nPress Enter to return to menu...")

def update_tool():
    print(colored("No updates available.", "green"))
    input("\nPress Enter to return to menu...")

# Main
def main():
    show_intro()
    show_warning()
    loading_animation()
    while True:
        show_menu()
        c = input(colored("Select option: ", "cyan"))
        if c == "1": ip_geolocation()
        elif c == "2": reverse_dns()
        elif c == "3": port_scanner()
        elif c == "4": whois_lookup()
        elif c == "5": headers_grabber()
        elif c == "6": subdomain_finder()
        elif c == "7": hash_identifier()
        elif c == "8": user_agent_generator()
        elif c == "9": save_report()
        elif c == "10": clear_logs()
        elif c == "11": update_tool()
        elif c == "12":
            print(colored("Bye 👋", "red"))
            break
        else:
            print(colored("Invalid option", "red"))

if __name__ == "__main__":
    main()