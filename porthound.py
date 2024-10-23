import socket
from termcolor import colored
import os

# Clear the screen on startup
def clear_screen():
    os.system('clear')

# Updated Banner for the tool
def banner():
    print(colored('''
                                         
 _____         _   _____               _ 
|  _  |___ ___| |_|  |  |___ _ _ ___ _| |
|   __| . |  _|  _|     | . | | |   | . |
|__|  |___|_| |_| |__|__|___|___|_|_|___|

             PortHound - Network Port Scanner
             Developed by WizSafe Organization
    ''', 'green', attrs=['bold']))

# Function to scan ports on a target host
def scan_ports(target, start_port, end_port):
    print(colored(f"\n[+] Scanning Target: {target}", "blue"))
    print(colored(f"[+] Scanning Ports from {start_port} to {end_port}\n", "blue"))
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # Timeout for each connection attempt
        
        result = sock.connect_ex((target, port))  # Connect to the target and port
        if result == 0:
            print(colored(f"[+] Port {port} is OPEN", "green"))
        else:
            print(colored(f"[-] Port {port} is CLOSED", "red"))
        sock.close()

# Main function
def main():
    clear_screen()
    banner()

    target = input(colored("\nEnter the Target IP/Hostname: ", "yellow"))
    start_port = int(input(colored("Enter the Start Port: ", "yellow")))
    end_port = int(input(colored("Enter the End Port: ", "yellow")))

    print(colored("\n[+] Starting Scan...\n", "cyan", attrs=['bold']))
    scan_ports(target, start_port, end_port)
    print(colored("\n[+] Scan Completed.\n", "cyan", attrs=['bold']))

if __name__ == "__main__":
    main()
