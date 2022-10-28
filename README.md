# Bypass403

Bypass URL that http status code is 403 with URL bypass payload and Header bypass payload

### Usage
```sh
python Bypass403.py -h
```

```

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

😍 Made with <3 By ITPAT
-------------------------------------------------------------------------------
 Twitter ❯ https://twitter.com/IttipatJitrada
-------------------------------------------------------------------------------

usage: Bypass403.py [-h] -u URL [-l LIST] [-p PROXY]

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     URL status 403 that you want to bypass
  -l LIST, --list LIST  List of URL status 403 that you want to bypass
  -p PROXY, --proxy PROXY
                        Burp proxy or any other proxy to send the request -p http://127.0.0.1:9090
```
__Running Bypass 403__

Bypass Single URL
```sh
python Bypass403.py -u https://example.com
```
Bypass URLs
```sh
python Bypass403.py -l urls.txt
```
Example of `urls.txt`:

```yaml
http://example.com
http://app.example.com
http://test.example.com
http://uat.example.com
```
