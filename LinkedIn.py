import time
from pynput.keyboard import Key
from Basic import Basic


class LinkedIn(Basic):

    def post(self):
        try:
            self.Chrome.get("https://www.linkedin.com/")
            self.Chrome.find_element_by_xpath("//input[@id='login-email']").send_keys(self.email)
            self.Chrome.find_element_by_xpath("//input[@id='login-password']").send_keys(self.password)
            self.Chrome.find_element_by_id("login-submit").click()
            time.sleep(3)
        except:
            self._bug_rep.append("Can't login")
        try:
            if self.post_on_my_page == "1":
                self.Chrome.find_element_by_xpath("//button[@class='Sans-17px-black-70%']").click()
                if self.priority == "image":
                    self.type(self.text + " " + self.link)
                    time.sleep(3)
                    self.type(" " + self.image_link)
                    time.sleep(3)
                    for x in range(0, len(self.image_link)):
                        self.run_key(Key.backspace)
                else:
                    self.type(self.text + " " + self.link)
                    time.sleep(3)
                    self.Chrome.find_element_by_xpath("//button[@class='button-primary-medium sharing-subaction-bar__post-button sharing-share-box__post-button post ember-view']").click()
                time.sleep(4)
        except:
            self._bug_rep.append("Can't post on my page")