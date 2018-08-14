import time
from Basic import Basic


class WeHear(Basic):

    def post(self):
        try:
            self.Chrome.get("https://weheartit.com/login")
            self.Chrome.find_element_by_xpath("//input[@id='user_email_or_username']").send_keys(self.email)
            self.Chrome.find_element_by_xpath("//input[@id='user_password_login']").send_keys(self.password)
            self.Chrome.find_element_by_xpath("//input[@class='btn btn-block btn-large bg-primary sign_up_button']").click()
            time.sleep(2)
        except:
            self._bug_rep.append("Can't login")
        try:
            if self.post_on_my_page == "1":
                self.Chrome.get("https://weheartit.com/articles/new")
                self.Chrome.find_element_by_xpath("//input[@class='input-block text-big text-strong js-article-input-title js-text-preview-input js-required-field']").send_keys(self.title)
                self.Chrome.find_element_by_xpath("//textarea[@class='input-block flex-1 js-article-input-body js-required-field']").send_keys(self.text + " " + self.link)
                self.Chrome.find_element_by_xpath("//input[@class='input-block no-margin js-file-preview-input js-required-max-file-size js-required-field']").send_keys("C:\\Users\\user\Downloads\dcL60Zp2Kxk.jpg")
                self.Chrome.find_element_by_xpath("//*[@class='input-block input-icon-right icon-dropdown']").click()
                self.run_key("A")
                self.Chrome.find_element_by_xpath("//input[@class='input-block']").send_keys(self.hashtags)
                self.Chrome.find_element_by_xpath("//input[@class='btn bg-primary js-required-submit']").click()
                time.sleep(5)
        except:
            self._bug_rep.append("Can't post on my page")