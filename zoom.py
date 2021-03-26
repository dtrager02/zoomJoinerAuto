import time
from datetime import datetime
from pynput.keyboard import Controller, Key
import webbrowser
import csv 
keyboard = Controller()
print("#for best results:")
print("#enable global shortcuts in zoom app" )
print("#make default browser auto-open zoom links (checkbox)")
def main():
    isStarted = False
    links = dict()
    with open('zoom.csv', newline='') as csvfile:
         reader = csv.reader(csvfile, delimiter=',')
         for row in reader:
             print(row)
             if str(row).find("example") != -1:
                 print("reached end")
                 break 
             if(len(row)):
                links[row[0]] = row[1:3]

    print(links)
    print(len(links.keys()))
    for i, j in links.items():
        while True:
            if isStarted == False:
                #print(int(j[0].split(':')[0]))
                #print(datetime.now().hour)
                if datetime.now().hour > int(j[0].split(':')[0]) or (datetime.now().hour == int(j[0].split(':')[0]) and datetime.now().minute > int(j[0].split(':')[1])):
                    print("skipped")
                    break
                if datetime.now().hour == int(j[0].split(':')[0]) and datetime.now().minute == int(j[0].split(':')[1]):
                    print("joined")
                    webbrowser.open(i)
                    isStarted = True
            #elif isStarted == True:
            if datetime.now().hour == int(j[1].split(':')[0]) and datetime.now().minute == int(j[1].split(':')[1]):
                time.sleep(9)
                keyboard.press(Key.alt_l)
                time.sleep(.5)
                keyboard.press('q')
                keyboard.release(Key.alt_l)
                keyboard.release('q')
                isStarted = False
                print("left")
                time.sleep(10)
                break

if __name__ == "__main__":
    main()