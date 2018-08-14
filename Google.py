import time
from pynput.keyboard import Key
from Basic import Basic
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Google(Basic):

    def post(self):
        try:
            self.Chrome.get("https://www.google.com/")
            self.Chrome.find_element_by_xpath("//a[@id='gb_70']").click()
            self.Chrome.find_element_by_xpath("//input[@id='identifierId']").send_keys(self.email)
            self.Chrome.find_element_by_xpath("//div[@id='identifierNext']/content[@class='CwaK9' and 1]").click()
            time.sleep(1)
            self.Chrome.find_element_by_xpath("//div/input[@class='whsOnd zHQkBf' and 1]").send_keys(self.password)
            self.Chrome.find_element_by_xpath("//content[@class='CwaK9']/span[@class='RveJvd snByac' and 1]").click()
            time.sleep(2)
        except:
            self._bug_rep.append("Can't login (Wrong login or password)")
        try:
            if self.post_on_my_page == "1":
                time.sleep(1)
                self.Chrome.get("https://plus.google.com/")
                self.Chrome.find_element_by_xpath("//c-wiz[@class='SSPGKf Jvazdb nWGHWc G6GRIc k7iNHb cLa0Ib']/c-wiz[@class='pf7Psf kQxXGc KFV7Ie']/content[@class='x2sGwe aRDqpc']/div[@class='T4LgNb O1bNWe ']/div[@class='DAbEod']/content/c-wiz/div[@class='M7vp2c']/div[@class='jx5iDb pd4VHb Ocx56c']/div[@class='H68wj jxKp7']/div[@class='aJZAlb pYN4db uenjKc']/c-wiz/div[@class='Ihwked UB0dDd cDhoub XkfHGe ScDfle vCjazd']/div[@class='yYUaOb']/div[@class='OnYLS']").click()
                time.sleep(2)
                if self.priority == "image":
                    self.type(self.image_link)
                    self.run_key(Key.enter)
                    time.sleep(5)
                    for x in range(0, len(self.image_link)):
                        self.run_key(Key.backspace)
                    self.type(self.text + " "  + self.link)
                    time.sleep(3)
                else:
                    self.type(self.text)
                    self.Chrome.find_element_by_xpath("//div[2]/div[@class='U26fgb mUbCce fKz7Od' and 1]/content[@class='xjKiLb' and 1]/span[1]").click()
                    self.Chrome.find_element_by_xpath("//input[@class='whsOnd zHQkBf']").send_keys(self.link)
                    self.Chrome.find_element_by_xpath("//*[@id='yDmH0d']/div[5]/div/div[2]/div[2]/div[2]/content/span").click()
                element = WebDriverWait(self.Chrome, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[@class='U26fgb O0WRkf zZhnYe e3Duub C0oVfc']/content[@class='CwaK9']/span[@class='RveJvd snByac']")))
                self.Chrome.find_element_by_xpath("//*[@id='yDmH0d']/div[4]/div[2]/div[2]/c-wiz/c-wiz/content/div[2]/div[3]/content/span").click()
                time.sleep(4)
        except:
            self._bug_rep.append("Can't post on my page")