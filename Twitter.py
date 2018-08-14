import time
from pynput.keyboard import Key
from Basic import Basic

class Twitter(Basic):

    def post(self):

        try:
            self.Chrome.get("https://twitter.com/")
            self.Chrome.find_element_by_name('session[username_or_email]').send_keys(self.email)
            self.Chrome.find_element_by_name('session[password]').send_keys(self.password)
            self.Chrome.find_element_by_xpath("//input[@class='EdgeButton EdgeButton--secondary EdgeButton--medium submit js-submit']").click()
            time.sleep(1)
        except:
            self._bug_rep.append("Can't login")
        try:
            if self.post_on_my_page == "1":
                self.Chrome.find_element_by_xpath("//div[@id='tweet-box-home-timeline']/div[1]").click()
                self.type(self.text + " " + self.link)
                self.run_key(Key.enter)
                self.Chrome.find_element_by_xpath("//button[@class='tweet-action EdgeButton EdgeButton--primary js-tweet-btn']/span[@class='button-text tweeting-text' and 1]").click()
                time.sleep(5)
        except:
            self._bug_rep.append("Can't post on my page")
