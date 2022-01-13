from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pyautogui as pg

path = "C:/Users/Adam/PycharmProjects/S48_Selenium/chromedriver_win32/chromedriver_old.exe"

class Dino:

    def __init__(self, path):
        self.s = Service(path)
        self.driver = webdriver.Chrome(service=self.s)
        self.driver.maximize_window()
        self.driver.get('https://elgoog.im/t-rex/')

    def jump(self, pyautogui=None):
        print("Dinooo")

        # # get CANVAS
        # canvas = self.driver.find_element(by=By.CSS_SELECTOR, value=".runner-canvas")
        # # print(type(canvas))
        # # get the canvas as a PNG base64 string
        # canvas_base64 = self.driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)
        # # decode
        # canvas_png = base64.b64decode(canvas_base64)
        # # save to a file
        # with open(r"canvas.png", 'wb') as f:
        #     f.write(canvas_png)

        pg.moveTo(778, 435, duration=1)
        time.sleep(2)
        pg.press('space')
        x = True
        while x:
            # pg.position()
            # print(pg.position())
            # jumper = pg.pixelMatchesColor(778, 435, (83, 83, 83))
            #felugro ablak es eltolas miatt
            jumper = pg.pixelMatchesColor(790, 385, (83, 83, 83))
            if jumper:
                pg.press('space')


bot = Dino(path)
bot.jump()
