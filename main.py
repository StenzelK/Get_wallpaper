import keyboard
import datetime
import time
import pyscreenshot

def main():

    _ROOT=open('root.txt','r').read()
    print(_ROOT)

    while True:

        if keyboard.is_pressed('shift+scroll lock'):
            time.sleep(0.5)
            name = str(datetime.datetime.now())[:-7].replace(" ", "_").replace(":", "-") + ".png"
            im = pyscreenshot.grab()
            im.save(_ROOT + name)


if __name__ == '__main__':

    main()