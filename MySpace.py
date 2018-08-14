import time
from pynput.keyboard import Key
from Basic import Basic


class MySpace(Basic):

    def post(self):
        try:
            self.Chrome.get("https://myspace.com/login")
        except:
            self._bug_rep.append("Can't navigate to " + self.url)
        try:
            self.Chrome.find_element_by_xpath("//input[@id='login.email']").send_keys(self.email)
            self.Chrome.find_element_by_xpath("//input[@id='login.password']").send_keys(self.password)
            self.Chrome.find_element_by_xpath("//form[@id='signInForm']/footer[@class='formFooter' and 1]/button[@class='primary' and 1]").click()
            time.sleep(1)
        except:
            self._bug_rep.append("Can't login (Wrong login or password")
        try:
            self.Chrome.get("https://myspace.com/home")
            if self.priority == "image":
                self.Chrome.find_element_by_xpath("//div[@class='postControl mentions']/div[@class='textarea' and 1]").send_keys(self.image_link)
                self.run_key(Key.enter)
                time.sleep(3)
                self.Chrome.find_element_by_xpath("//div[@class='postControl mentions']/div[@class='textarea' and 1]").clear()
                self.Chrome.find_element_by_xpath("//div[@class='postControl mentions']/div[@class='textarea' and 1]").send_keys(self.text + " " + self.link + " ")
                time.sleep(1)
            else:
                self.Chrome.find_element_by_xpath(
                    "//div[@class='postControl mentions']/div[@class='textarea' and 1]").clear()
                self.Chrome.find_element_by_xpath(
                    "//div[@class='postControl mentions']/div[@class='textarea' and 1]").send_keys(
                    self.text + " " + self.link + " ")
            time.sleep(3)
            self.Chrome.find_element_by_xpath("//div[@class='superpost inline isMinimized activating location   webcamSupported attaching link']/footer[1]/button[@class='primary' and 1]").click()
            time.sleep(5)
        except:
            self._bug_rep.append("Can't post on my page")