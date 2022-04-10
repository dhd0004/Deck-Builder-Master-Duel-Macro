import botdeck
from pyautogui import alert,prompt
import os
import pyglet


def set_language():
    lang=prompt("""
    Language:
    en (Default)
    es
    fr
    de
    it
    pt
    
    Your Choice:""")
    dir = pyglet.resource.get_settings_path('YGO')
    filename = os.path.join(dir, 'config.ini')
    f = open(filename, "w")
    f.write(lang)
    f.close()
    return lang


def init_language():
    dir = pyglet.resource.get_settings_path('YGO')
    if not os.path.exists(dir):
        os.makedirs(dir)
    filename = os.path.join(dir, 'config.ini')
    if not os.path.exists(filename):
        f = open(filename, "w")
        f.write("en")
        f.close()
    f =  open(filename, "r")
    lines = f.readlines()
    lang = lines[0]
    return lang


def main_menus():
    LANG=init_language()
    botdeck.init()

    while True:
        try:
            resposta = prompt("""
    Welcome to MACRO YU GI OH MASTER DUEL!!!
    Version 0.2v
    
    What do you want to do?
    1 - Get the list of cards and amount of a deck
    2 - Automatically build a deck using the Macro
    3 - Set language
    4 - Quit
    
    Your Choice:""",title='Languge:{}'.format(LANG))
            
            if not resposta:
                break
            resposta = int(resposta)
            if resposta > 3:
                alert("Just numbers in between 1 and 3. Please")

            if resposta == 1:
                botdeck.deck(True,LANG)

            elif resposta == 2:
                botdeck.macro_deck(LANG)
                botdeck.sleep(3)
            elif resposta == 3:
                LANG=set_language()
                

            elif resposta == 4:
                break
            else:
                break

        except Exception as e:

            print(e)
            print("\n\n\n\n\33[31mInvalid data!\nPlease, just numbers in between 1 and 3..\33[m")
