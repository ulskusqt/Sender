import time
from Basic import Basic


class Plurk(Basic):

    def post(self):
        try:
            self.Chrome.get("https://www.plurk.com/login?r=")
        except:
            self._bug_rep.append("Can't navigate to " + self.url)
        try:
            self.Chrome.find_element_by_xpath("//input[@id='input_nick_name']").send_keys(self.email)
            self.Chrome.find_element_by_xpath("//input[@id='input_password']").send_keys(self.password)
            self.Chrome.find_element_by_xpath("//button[@id='login_submit']").click()
        except:
            self._bug_rep.append("Can't login")
        try:
            if self.post_on_my_page == "1":
                if self.priority == "image":
                    self.Chrome.find_element_by_xpath("//textarea[@id='input_big']").send_keys(self.text + " " + self.link + " " + self.image_link)
                else:
                    self.Chrome.find_element_by_xpath("//textarea[@id='input_big']").send_keys(
                        self.image_link + " " + self.text + " " + self.link)
                time.sleep(3)
                self.Chrome.find_element_by_xpath("//div[@class='click submit_img q_is']").click()
                time.sleep(5)
        except:
            self._bug_rep.append("Can't post on my page")