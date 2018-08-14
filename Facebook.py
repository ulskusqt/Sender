import time
from pynput.keyboard import Key
from Basic import Basic

class Facebook(Basic):

    def post(self):
        try:
            self.Chrome.get("https://www.facebook.com/")
            self.Chrome.find_element_by_id('email').send_keys(self.email)
            self.Chrome.find_element_by_id('pass').send_keys(self.password)
            self.Chrome.find_element_by_id('u_0_2').click()
        except:
            self._bug_rep.append("Can't login")
        try:
            if self.post_on_my_page == "1":
                self.Chrome.find_element_by_css_selector('span._1vp5').click()
                time.sleep(2)
                self.Chrome.find_element_by_css_selector("span._5qtp").click()
                self.Chrome.find_element_by_css_selector('div._1mf._1mj').click()
                time.sleep(2)
                if self.priority == "image":
                    self.type(self.image_link)
                    self.run_key(Key.enter)
                    time.sleep(3)
                    for x in range(0, len(self.image_link)):
                        self.run_key(Key.backspace)
                self.type(self.text + " " + self.link)
                self.run_key(Key.enter)
                if self.post_date_time == '':
                    pass
                else:
                    pass
                if self.post_on_my_page == '1':
                    self.Chrome.find_element_by_css_selector('li._1pek._vli > div > ol._159h > li._1sex > div._1sez > div._1se- > div._1se_').click()
                else:
                    pass
                self.Chrome.find_element_by_xpath("//button[@class='_1mf7 _4r1q _4jy0 _4jy3 _4jy1 _51sy selected _42ft']").click()
                time.sleep(5)
        except:
            self._bug_rep.append("Can't post on my page")