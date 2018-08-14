import time
from pynput.keyboard import Key
from Basic import Basic

class Vkontakte(Basic):

    def post(self):
        try:
            self.Chrome.get("https://vk.com/")
        except:
            self._bug_rep.append("Can't navigate to " + self.url)
        try:
            self.Chrome.find_element_by_xpath("//input[@id='index_email']").send_keys(self.email)
            self.Chrome.find_element_by_xpath("//input[@id='index_pass']").send_keys(self.password)
            self.Chrome.find_element_by_xpath("//button[@id='index_login_button']").click()
            time.sleep(1)
        except:
            self._bug_rep.append("Can't login (Wrong login or password")
        try:
            if self.post_on_my_page == "1":
                self.Chrome.find_element_by_xpath("//div[@id='post_field']").clear()
                self.Chrome.find_element_by_xpath("//div[@id='post_field']").click()
                if self.image_link != "":
                    self.type(self.image_link + " ")
                    time.sleep(1)
                    self.Chrome.find_element_by_xpath("//*[@id='post_field']").clear()
                    self.Chrome.find_element_by_xpath("//*[@id='post_field']").send_keys(self.text + " " + self.link + " ")
                self.run_key(Key.space)
                self.run_key(Key.backspace)
                self.run_key(Key.enter)
                self.Chrome.find_element_by_xpath("//button[@id='send_post']").click()
                time.sleep(5)
        except:
            self._bug_rep.append("Can't post on my page")
