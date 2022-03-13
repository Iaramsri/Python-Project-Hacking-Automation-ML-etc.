from bs4 import BeautifulSoup
import requests
import requests.exceptions
import urllib.parse
from collections import deque
import re

print(
    '''
       ____             _  __  ____                                 ___         __   __               ____
      / __/__ _  ___ _ (_)/ / / __/____ ___ _ ____ ___  ___  ____  / _ \ __ __ / /_ / /  ___   ___   |_  /
     / _/ /  ' \/ _ `// // / _\ \ / __// _ `// __// _ \/ -_)/ __/ / ___// // // __// _ \/ _ \ / _ \ _/_ < 
    /___//_/_/_/\_,_//_//_/ /___/ \__/ \_,_//_/  / .__/\__//_/   /_/    \_, / \__//_//_/\___//_//_//____/ 
                                                /_/                    /___/                              
       ____ __   __   __    _     __        _   ___                                _                      
      /  _// /_ / /_ / /   (_)___/ /___    (_) / _ |  ____ ___ _ __ _   ___  ____ (_)                     
     _/ / / __// __// _ \ / // _  // -_)  / / / __ | / __// _ `//  ' \ (_-< / __// /                      
    /___/ \__/ \__//_//_//_/ \_,_/ \__/__/ / /_/ |_|/_/   \_,_//_/_/_//___//_/  /_/                       
                                      |___/                                                               
    '''
)

while True:
    choice = input("1 - HTTP\n2 - HTTPS\n\n[+] Enter Yours Choice Here: ")
    try:
        choice_num = int(choice)
        if choice_num == 1:
            user_url0 = str(input('[+] Enter Target URL To Scan: http://'))
            user_url = "http://" + user_url0
            urls = deque([user_url])
            break
        elif choice_num == 2:
            user_url0 = str(input('[+] Enter Target URL To Scan: https://'))
            user_url = "https://" + user_url0
            urls = deque([user_url])
            break
        else:
            print("You entered an incorrect option, please try again.")
    except:
        print("You entered an invalid option, please try again.")

scraped_urls = set()
emails = set()

count = 0
count2 = int(input('[+] Enter Count Number: '))
try:
    while len(urls):
        count += 1
        if count == count2+1:
            break
        url = urls.popleft()
        scraped_urls.add(url)

        parts = urllib.parse.urlsplit(url)
        base_url = '{0.scheme}://{0.netloc}'.format(parts)

        path = url[:url.rfind('/')+1] if '/' in parts.path else url

        print('[%d] Processing %s' % (count, url))
        try:
            response = requests.get(url)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            continue

        new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
        emails.update(new_emails)

        soup = BeautifulSoup(response.text, features="lxml")

        for anchor in soup.find_all("a"):
            link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
            if link.startswith('/'):
                link = base_url + link
            elif not link.startswith('http'):
                link = path + link
            if not link in urls and not link in scraped_urls:
                urls.append(link)
except KeyboardInterrupt:
    print('[-] Closing!')

for mail in emails:
    print(mail)
