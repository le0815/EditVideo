import asyncio
import datetime
import os
import pickle
import random
import time
import numpy as np
import pyperclip
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

_email_pwd = '13579thanG$'


class Func:
    def __init__(self, driver, name='main'):
        self.driver = driver
        self.name = name

    def MakeAlert(self):
        duration = 1  # seconds
        freq = 440  # Hz
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))

    def GetCookie(self, email, usr_name, cookie_path):
        pickle.dump(self.driver.get_cookies(), open(f"{cookie_path}{email[:email.find('.')]}_{usr_name}.pkl", "wb"))
        print('Get cookies success')

    async def Login(self, video_name, email):

        # set full screen
        self.driver.maximize_window()

        # direct to login page
        self.driver.get("https://online-video-cutter.com/remove-logo")
        await asyncio.sleep(1)

        # click login button
        print(f"click login button - ({self.name})")
        elm = self.driver.find_element(By.CSS_SELECTOR, "button.sign-in.sm")
        elm.click()
        await asyncio.sleep(1)

        # click sign-in with google
        print(f"click sign-in with google - ({self.name})")
        self.driver.execute_script(
            'document.querySelector("div.modal.show#modal-signup").childNodes[1].childNodes[1].childNodes[5].childNodes[1].childNodes[1].childNodes[1].click();')

        while 1:
            try:
                print(f"switching to login form - ({self.name})")
                self.driver.switch_to.window(self.driver.window_handles[1])
                break
            except:
                print(f"switching to login form - ({self.name})")
        # input email
        # switch to login window

        await asyncio.sleep(1)
        email_inp = ActionChains(self.driver)
        email = email
        print(f"entering email - ({self.name})")
        email_inp.send_keys(email).perform()
        await asyncio.sleep(1)
        email_inp.send_keys(Keys.ENTER).perform()
        await asyncio.sleep(4)
        print(f"entering pwd - ({self.name})")
        email_inp.send_keys(_email_pwd).perform()
        time.sleep(1)
        email_inp.send_keys(Keys.ENTER).perform()
        # WriteEmailLogged(email)
        await asyncio.sleep(5)
        try:
            # click accept btn
            print(f"clicking accept btn - ({self.name})")
            elem = self.driver.find_element(By.CSS_SELECTOR, "div.XjS9D.TrZEUc.BbN10e.tyoyWc")
            elem.click()
        except Exception as err:
            print(f"no accept btn - ({self.name}): {err}")

        # switch back to main window
        print(f"switching to main window - ({self.name})")
        self.driver.switch_to.window(self.driver.window_handles[0])
        await asyncio.sleep(5)

        # 'Continue with a free account'

        while 1:
            try:
                print(f"click Continue with a free account - ({self.name})")
                elm = self.driver.find_element(By.XPATH, "//a[contains(text(),'Continue with a free account')]")
                elm.click()
                break
            except:
                print(f"try click Continue with a free account - ({self.name})")

        # wait for login success
        while 1:
            print(f'wait for login success - ({self.name})')
            try:

                # # switch to main tab
                # print(f'switch to main tab - ({self.name})')
                # self.driver.switch_to.window(self.driver.window_handles[0])

                # find create file button
                elm = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          'input.picker-dropdown__input')))

                elm.send_keys(f"/home/ha/PycharmProjects/Ai_content/Download/Video/Watermark/{video_name}")

                print(f"Page is ready!  - ({self.name})")
                break
            except TimeoutException:
                print(f"Loading took too much time! - ({self.name})")

    async def MakeProject(self, video_name):

        await asyncio.sleep(2)

        action_chain = ActionChains(driver=self.driver)

        # select watermark by mouse
        x1, y1 = 1018, 100
        x2, y2 = 1077, 117

        print(f"select watermark by mouse  - ({self.name})")
        action_chain.move_by_offset(x1, y1).click_and_hold().perform()
        action_chain.move_by_offset(x2 - x1, y2 - y1).click().perform()

        await asyncio.sleep(2)

        # click apply to remove watermark
        print(f"click apply to remove watermark  - ({self.name})")
        elm = self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-bright.apply.icon")
        elm.click()

        await asyncio.sleep(2)

        # click save button
        print(f"click save button - ({self.name})")
        elm = self.driver.find_element(By.CSS_SELECTOR, "div.export.component_side-menu-item")
        elm.click()

        await asyncio.sleep(2)

        # click export button
        print(f"click export button - ({self.name})")
        elm = self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-bright")
        elm.click()

        await asyncio.sleep(2)

        # wait for downloadable
        while 1:
            try:

                print(f"wait for downloadable - ({self.name})")
                elm = self.driver.find_element(By.CSS_SELECTOR, "a.btn.btn-bright.icon.btn-save")
                elm.click()
                await asyncio.sleep(2)
                break
            except:
                print(f"wait for downloadable - ({self.name})")
                await asyncio.sleep(2)

        # wait till download finish
        video_name = video_name + " (online-video-cutter.com)"
        while 1:
            print(f"wait till download finish - ({self.name})")
            if os.path.exists(
                    f'/home/ha/PycharmProjects/Ai_content/Download/Video/Removed_watermark_123/{video_name}.mp4'):
                print(f"download finished: {video_name} - ({self.name})")
                break
            time.sleep(1)
