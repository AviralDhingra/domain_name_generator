import os
import sys
import webbrowser

import requests
from bs4 import BeautifulSoup


def decideName(keywords):
    print(keywords)
    keywords = ' '.join([str(elem) for elem in keywords])
    print(keywords)
    keywords = keywords.replace(' ', '+')

    print(keywords)
    productUrl = f'https://www.shopify.in/tools/business-name-generator/search?query={keywords}&button=&tool=business_name_generator#ToolContent'
    print(productUrl)

    res = requests.get(
        productUrl,
        headers={
            "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"
        })
    print(f'Connection Status: {res.status_code}')
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
            print(elem)
            print(type(elem))
            l.append(elem)
            # print('.' + elem + '.')
        row = row + 1
    for i in range(len(l)):
        elem = l[i]
        elem = str(elem)
        elem = elem.replace('[<span class="business-name-button__name">', '')
        elem = elem.replace('</span>]', '')
        l2.append(elem)
        print(elem)
    return l2


def godaddy_redirect(name_chosen, domain):
    inp = name_chosen
    inpD = domain
    if inpD[0] == '.':
        pass
    else:
        inpD = '.' + str(inpD)

    name_wanted = inp + inpD
    # print(name_wanted)

    # domain_wanted = f'http://{name_wanted}'
    # res = requests.get(
    #     domain_wanted,
    #     headers={
    #         "User-Agent":
    #         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"
    #     })

    finalGodaddyLink = f'https://in.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck={name_wanted}'
    # webbrowser.open(finalGodaddyLink)
    return finalGodaddyLink


# ToolContent > div > div.grid-container.grid-container--thirds.grid--striped > div:nth-child(2) > div:nth-child(2) > button > span

# ToolContent > div > div.grid-container.grid-container--thirds.grid--striped > div:nth-child(5) > div:nth-child(2) > button > span

# ToolContent > div > div.grid-container.grid-container--thirds.grid--striped > div:nth-child(3) > div:nth-child(3) > button > span

# ToolContent > div > div.grid-container.grid-container--thirds.grid--striped > div:nth-child(1) > div:nth-child(1) > button > span


def main(keywords):
    print(keywords)
    print(type(keywords))
    keywords = keywords
    print(keywords)
    ### Keywords is 'ImmutableMultiDict' Right now
    # keywords = keywords[0]['keywords']
    # keywords = keywords[1:]
    # print(keywords + 'original')
    name_wanted_opt = decideName(keywords)
    print(name_wanted_opt)
    for i in range(2):
        name_wanted_opt.pop(len(name_wanted_opt) -
                            1)  ## Last 2 Responses ([]. [])
    # print(name_wanted_opt)
    # print(type(name_wanted_opt))
    """
    for i in range(len(name_wanted_opt)):
        if name_wanted_opt[i] == '[]' or name_wanted_opt[i] == []:
            name_wanted_opt.pop(i)
    """
    """
    name_wanted_opt.remove('[]')
    name_wanted_opt.remove('[]')
    print(name_wanted_opt)
    for i in range(len(name_wanted_opt)):
    print(f'{i}. {name_wanted_opt[i]}')
    inp = int(input('What Name Do You Like?'))
    """
    return name_wanted_opt
    godaddy_redirect(name_wanted)


"""
try:
    main()
except KeyboardInterrupt:
    # os.system('clear')
    # print('[+] Exiting...')
    os.system('exit')
    os.system('exit')
"""

# try:
#     res.raise_for_status()
#     # print('Working...')
#     True
# except requests.exceptions.HTTPError:
#     # print("Invlaid URL...")
#     # print(False)
