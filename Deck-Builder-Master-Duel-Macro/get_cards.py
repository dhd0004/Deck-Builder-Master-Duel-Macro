from re import findall, UNICODE
from requests import get
from bs4 import BeautifulSoup
from colorama import init
from lxml import html
import pyautogui


def deck(show=False,LANG="en"):

    """This function gets the HTML of the link and looks  for card names"""

    init()
    cards = dict()

    while True:
        try:
            link=pyautogui.prompt("Insert a valid link from \nhttps://www.masterduelmeta.com/\n"
                  "Examples of valid links: \nhttps://www.masterduelmeta.com/top-decks\n"
                  ,"link")
            if not link:
                return 3
            if link == "3":
                return link

            else:
                conec = get(link)
            html_orig = BeautifulSoup(conec.text, "html.parser").decode()
            card = findall(r'\bname\\":\\"(.+?)\\"},\\"amount\b', str(html_orig), UNICODE)
            amount = findall(r'\bamount\\":(\d)\b', str(html_orig), UNICODE)
            break

        except Exception as e:
            print(e)
            print("\n\n\33[31mPlease, get a valid link!\33[m")

    for x in range(len(card)):
        
        if """\\\"""" in card[x]:
            name_card = card[x].replace(r"""\\\"""", '')
        else:
            name_card = card[x]
        # Translate card name
        if "en" not in LANG:
            page = get('https://yugioh.fandom.com/wiki/{}'.format(name_card.replace(" ","_")))
            
            tree = html.fromstring(page.content)
            name_card = tree.xpath('//span[@lang="{}"]/text()'.format(LANG))[0]
        
        cards[name_card] = amount[x]

    if show:
        result="List Of Cards:\n"
        for x, y in cards.items():
            result+="{}: {}\n".format(x, y)
        pyautogui.alert(result)
    return cards
