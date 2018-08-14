import time
from pynput.keyboard import Key
from Basic import Basic


class Reddit(Basic):

    def post(self):
        try:
            self.Chrome.get("https://www.reddit.com/login")
            time.sleep(1)
            self.Chrome.find_element_by_xpath("//input[@id='loginUsername']").send_keys(self.email)
            time.sleep(1)
            self.Chrome.find_element_by_xpath("//input[@id='loginPassword']").send_keys(self.password)
            time.sleep(1)
            self.Chrome.find_element_by_xpath("//button").click()
            time.sleep(3)
        except:
            self._bug_rep.append("Can't login")
        try:
            if self.post_on_my_page == "1":
                self.Chrome.get("https://www.reddit.com/submit")
                self.Chrome.find_element_by_xpath("//input[@class='s1u2j4lv-0 cCJJXE']").click()
                self.run_key(Key.down)
                self.run_key(Key.enter)
                time.sleep(1)
                self.Chrome.find_element_by_xpath("//div[@id='SHORTCUT_FOCUSABLE_DIV']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/button[3]").click()
                self.Chrome.find_element_by_xpath("//textarea[@class='dv38e5-1 kMUpkq nsxnvf-0 gJghlv']").send_keys(self.title)
                self.Chrome.find_element_by_xpath("//textarea[@class='s3szogb-1 nBUJr nsxnvf-0 gJghlv']").send_keys(self.link)
                self.Chrome.find_element_by_xpath("//button[@class='s1ewxf2z-0 coAaMI']").click()
                time.sleep(4)
        except:
            self._bug_rep.append("Can't post on my page")
