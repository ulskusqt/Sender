import time
from pynput.keyboard import Key
from Basic import Basic


class Instagram(Basic):

    def post(self):

        try:
            self.Chrome.get(self.url + 'accounts/login/')
            time.sleep(4)
            self.Chrome.find_element_by_xpath("//input[@name='username']").send_keys(self.email)
            self.Chrome.find_element_by_xpath("//input[@name='password']").send_keys(self.password)
            self.Chrome.find_element_by_xpath("//button").click()
            time.sleep(1)
        except:
            self._bug_rep.append("Can't login (Wrong login or password")
        try:
            if self.post_on_my_page == "1":
                self.Chrome.find_element_by_xpath("//div[@id='post_field']").clear()
                self.Chrome.find_element_by_xpath("//div[@id='post_field']").click()
                self.type(self.text + " " + self.link + " ")
                self.run_key(Key.space)
                self.run_key(Key.backspace)
                self.run_key(Key.enter)
                self.Chrome.find_element_by_xpath("//button[@id='send_post']").click()
        except:
            self._bug_rep.append("Can't post this post on my page")