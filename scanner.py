#!/usr/bin/python3
import ftplib
import argparse

def tryLogin(fileName):
    ipList = []    
    with open(fileName, 'r') as file:
        for line in file:
            ipList.append(line.strip())

    for ipAddress in ipList:
        try:
            ftp = ftplib.FTP(ipAddress, timeout=5)
            ftp.login('anonymous', '')
            print(f'{ipAddress} anonymous login *SUCCESS*.')
            ftp.quit()
        except Exception as e:
            print(f'{ipAddress} anonymous login FAILED.')

try:
    parser = argparse.ArgumentParser(
            prog='',
            description='Anonymous FTP scanner',
            add_help=True)

    parser.add_argument("-i", type=str, required=False, help="Single IP to scan")
    parser.add_argument("-l", type=str, required=False, help="List of IPs to scan")
    options = parser.parse_args()
    # Check against one host
    if options.i:
        ipAddr = options.i
        try:
            ftp = ftplib.FTP(ipAddr, timeout=5)
            ftp.login('anonymous', '')
            print(f'{ipAddr} anonymous login *SUCCESS*.')
            ftp.quit()
        except Exception as e:
            print(f'{ipAddr} anonymous login FAILED.')

    # If IP list file, pass file name to function
    if options.l:
        tryLogin(str(options.l))

    #If no options selected, stop
    if not any(vars(options).values()):
        parser.error("No arguments provided. Must either enter one IP or list of IPs to scan with options `-i` for single IP address or `-l` for a list of IP addresses.")

except KeyboardInterrupt:
    print("\nStopped by user")
