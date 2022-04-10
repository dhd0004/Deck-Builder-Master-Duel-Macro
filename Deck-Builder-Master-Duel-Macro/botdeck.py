from keyboard import is_pressed
from get_cards import deck
import pyautogui
from pyautogui import click, write, pixel, press, rightClick, size, alert,moveTo
from time import sleep as sleep
from get_cards import init
from pynput.keyboard import Key, Controller


def macro_deck(LANG="en"):

    """'Macro_deck' calls 'deck()' function
    after that control your mouse and keybord
    to put the cards from 'deck()' in your DeckBuilder"""

    init()
    tamanho = size()
    #Search location
    alert("Click in search bar and wait 2 seconds")
    sleep(2)
    searchbox = pyautogui.position()
    alert("Click in first card and wait 2 seconds")
    sleep(2)
    firstcard = pyautogui.position()

    print("""
\33[31mBefore proceeding.
Make sure the game configuration  is correct.\33[m
\33[33m
Requirements:

1 - In the Deck Builder, show up all card must be active.
2 - Go to Deck Builder
\33[m
\33[31mTo stop the macro just HOLD the "Esc" on your keybord.\33[m

After you placing the link you have 5 seconds to return to the game before the macro starts.
    """)
    cartas = deck(False,LANG)

    if len(cartas) != 0 and cartas != "3":
        for x in range(2):
            print("You must return to the DeckBuild Screen Please.. SECONDS:", x+1)
            sleep(1)

        for nome, quantidade in cartas.items():

            if is_pressed("esc"):
                break

           
            click(searchbox[0],searchbox[1])
            keyboard = Controller()
            keyboard.type(nome)
            press('enter')
            sleep(2)

            for x in range(int(quantidade)):
                pyautogui.moveTo(firstcard[0], firstcard[1])
                rightClick(firstcard[0], firstcard[1])

            sleep(1)

