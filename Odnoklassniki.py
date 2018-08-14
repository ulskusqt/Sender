import time
from pynput.keyboard import Key
from Basic import Basic
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Odnoklassniki(Basic):

    def post(self):
        try:
            self.Chrome.get("https://ok.ru/")
            self.Chrome.find_element_by_xpath("//input[@id='field_email']").send_keys(self.email)
            self.Chrome.find_element_by_xpath("//input[@id='field_password']").send_keys(self.password)
            self.Chrome.find_element_by_xpath("//input[@class='button-pro __wide']").click()
        except:
            self._bug_rep.append("Can't login")
        try:
            if self.post_on_my_page == "1":
                self.Chrome.get(self.url + "/post")
                element = WebDriverWait(self.Chrome, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@class='posting_itx emoji-tx h-mod js-ok-e ok-posting-handler']")))
                self.Chrome.find_element_by_xpath("//div[@class='posting_itx emoji-tx h-mod js-ok-e ok-posting-handler']").click()
                self.Chrome.find_element_by_xpath("//div[@class='posting_itx emoji-tx h-mod js-ok-e ok-posting-handler']").send_keys(self.text + " " + self.link + " ")
                if self.priority == "image":
                    self.Chrome.find_element_by_xpath(
                        "//div[@class='posting_itx emoji-tx h-mod js-ok-e ok-posting-handler']").send_keys(self.image_link)
                    self.run_key(Key.enter)
                    time.sleep(5)
                    for x in range(0, len(self.image_link)+1):
                        self.run_key(Key.backspace)
                self.run_key(Key.space)
                self.run_key(Key.backspace)
                self.run_key(Key.enter)
                time.sleep(2)
                self.Chrome.find_element_by_css_selector('div.posting_submit.button-pro').click()
        except:
            self._bug_rep.append("Can't post this post on my page")