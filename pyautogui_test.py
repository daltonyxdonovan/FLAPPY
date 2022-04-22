import pyautogui as pg
import time

running = True
justStarted = True
speed = 4

def startFromVSCode(durations):
    pg.moveTo(1800, 20, durations)
    pg.click()
    pg.moveTo(20, 20, durations)
    pg.doubleClick()
    pg.moveTo(650, 400, durations*5)
    pg.doubleClick()
    pg.moveTo(1430, 250, durations)
    pg.click()

def refresh(durations):
    pg.moveTo(150, 150, durations)
    pg.doubleClick()

def stop(durations):
    global running
    pg.moveTo(1900, 40, durations)
    pg.click()
    pg.moveTo((1920/2)+30, (1080/2)+20, durations)
    pg.click()
    
def start(durations):
    pg.moveTo(20, 20, durations)
    pg.doubleClick()
    pg.moveTo(650, 400, durations*5)
    pg.doubleClick()
    pg.moveTo(1430, 250, durations)
    pg.click()

while running:
    stop(speed)
    time.sleep(10)
    start(speed)
    running = False
        
