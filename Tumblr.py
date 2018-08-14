import time
from Basic import Basic

class Tumblr(Basic):

    def post(self):
        try:
            self.Chrome.get(self.url)
            self.Chrome.find_element_by_xpath("//input[@id='signup_determine_email']").send_keys(self.email)
            self.Chrome.find_element_by_xpath("//span[@class='signup_determine_btn active']").click()
            time.sleep(1)
            self.Chrome.find_element_by_xpath("//div[@id='signup_magiclink']/div[@class='magiclink_password_container chrome' and 2]").click()
            self.Chrome.find_element_by_xpath("//input[@id='signup_password']").send_keys(self.password)
            self.Chrome.find_element_by_xpath("//span[@class='signup_login_btn active']").click()
            time.sleep(5)
        except:
            self._bug_rep.append("Can't login")
