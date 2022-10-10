import os
import sys
import webbrowser

import requests
from bs4 import BeautifulSoup

# from pprint import pprint


def decideName(keywords):
    keywords = ' '.join([str(elem) for elem in keywords])
    keywords = keywords.replace(' ', '+')

    print(keywords)
    productUrl = f'https://www.shopify.in/tools/business-name-generator/search?query={keywords}&button=&tool=business_name_generator#ToolContent'
    # print(productUrl)

    res = requests.get(productUrl, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"
    })
    # print(f'Connection Status: {res.status_code}')
    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Invlaid URL...")

    # *****************
    elem = ['Testing Attribute']
    row = 1
    columns = 3  # Fixed
    l = []  # Name Suggestions (HTML)
    l2 = []  # Name Suggestions (Str)
    while not elem == []:
        for i in range(1, columns, 1):
            name_cssTag = f'#ToolContent > div > div.grid-container.grid-container--thirds.grid--striped > div:nth-child({row}) > div:nth-child({i}) > button > span'

            soup = BeautifulSoup(res.text, 'html.parser')
            elem = soup.select(name_cssTag)
            # print(elem)
            # print(type(elem))
            l.append(elem)
            # print('.' + elem + '.')
        row = row + 1
    for i in range(len(l)):
        elem = l[i]
        elem = str(elem)
        elem = elem.replace(
            '[<span class="business-name-button__name">', '')
        elem = elem.replace(
            '</span>]', '')
        l2.append(elem)
        # print(elem)
    return l2


def godaddy_redirect(name_wanted):
    domain_wanted = f'http://{name_wanted}'
    try:
        res = requests.get(domain_wanted, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"
        })
        # res.raise_for_status()
        if res.status_code == 200:
            print(
                f"The Website '{name_wanted}' already exists... try a new one")
            main()
        # print(f'Connection Status: {res.status_code}')
        elif not res.status_code == 200:
            print('Congratulations... Your wanted name exists')
            print("[+] Directing You To 'godaddy.com'")
            webbrowser.open(
                f'https://in.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck={name_wanted}')
    except requests.exceptions.ConnectionError:
        print('COngratulations... Your wanted name exists')
        print("[+] Directing You To 'godaddy.com'")
        webbrowser.open(
            f'https://in.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck={name_wanted}')


# ToolContent > div > div.grid-container.grid-container--thirds.grid--striped > div:nth-child(2) > div:nth-child(2) > button > span

# ToolContent > div > div.grid-container.grid-container--thirds.grid--striped > div:nth-child(5) > div:nth-child(2) > button > span

# ToolContent > div > div.grid-container.grid-container--thirds.grid--striped > div:nth-child(3) > div:nth-child(3) > button > span

# ToolContent > div > div.grid-container.grid-container--thirds.grid--striped > div:nth-child(1) > div:nth-child(1) > button > span

def main():
    sys.argv = sys.argv
    name_wanted_opt = decideName(sys.argv[1:])
    # print(name_wanted_opt)
    for i in range(len(name_wanted_opt)):
        print(f'{i}. {name_wanted_opt[i]}')

    inp = int(input('What Name Do You Like?'))
    inp = name_wanted_opt[inp]

    inpD = input('What Domain Extension Would You Want?')
    if inpD[0] == '.':
        pass
    else:
        inpD = '.' + str(inpD)

    name_wanted = inp + inpD
    # print(name_wanted)
    godaddy_redirect(name_wanted)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        # os.system('clear')
        print('[+] Exiting...')
        os.system('exit')
        os.system('exit')

# try:
#     res.raise_for_status()
#     print('Working...')
#     True
# except requests.exceptions.HTTPError:
#     print("Invlaid URL...")
#     print(False)
