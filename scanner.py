import ftplib


def getHosts():
    ipList = []
    inputOption = input('Would you like to:\n(1) Scan a single host\n(2) Scan a list from a file: ')
    if inputOption == '1':
        ipList = [input('Enter the IP/hostname to scan: ').strip()]
    elif inputOption == '2':
        fileName = input("Enter the file name: ")
        with open(fileName, 'r') as file:
            for line in file:
                ipList.append(line.strip())
    else:
        print('\ninvalid option. try again\n')
        getHosts()
    return ipList


def tryLogin(ipList):
    for ipAddress in ipList:
        try:
            ftp = ftplib.FTP(ipAddress)
            ftp.login('anonymous', '')
            print(f'{ipAddress} anonymous login *SUCCESS*.')
            ftp.quit()
        except Exception as e:
            print(f'{ipAddress} anonymous login FAILED.')


ipList = getHosts()
tryLogin(ipList)
