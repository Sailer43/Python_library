import socket
import sys
import os

def ret_banner(IP : str, port : int):
    try:
        s = socket.socket()
        s.connect((IP, port))
        banner = s.recv(1024)
        return banner
    except Exception as e:
        print("[-] Error while connecting " + IP + ": " + str(e))
        return

def check_vulns(banner, file_name):
    with open(file_name) as f:
        for line in f.readlines():
            if line.strip('\n') in str(banner):
                print("\t[+] Server is vulnerable: " + str(banner).strip('\n'))

def get_a_readable_vuln_list():
    if len(sys.argv) < 2:
        while True:
            filename = input("[*] Please enter a readable vulnerability list:\n")
            if not os.path.isfile(filename):
                print('[-] ' + filename +' does not exist.')
            elif not os.access(filename, os.R_OK):
                print('[-] ' + filename +' access denied.')
            else:
                return filename
    else:
        if not os.path.isfile(sys.argv[1]):
            print('[-] ' + sys.argv[1] +' does not exist.')
        elif not os.access(sys.argv[1], os.R_OK):
            print('[-] ' + sys.argv[1] +' access denied.')
        else:
            return sys.argv[1]
            
def main():
    filename = get_a_readable_vuln_list()
    port_list = [21, 22, 25, 80, 110, 443]
    socket.setdefaulttimeout(2)
    for i in range(113, 255):
        IP = '164.107.' + str(i) + ".26"
        for port in port_list:
            banner = ret_banner(IP, port)
            if banner:
                print('[+] ' + IP + ': ' + str(banner))
                check_vulns(banner, filename)

if __name__ == "__main__":
    main()
