import time
from Basic import Basic

class Skyrock(Basic):

    def post(self):
        try:
            self.Chrome.get("https://www.skyrock.com/?connect=1")
        except:
            self._bug_rep.append("Can't navigate to " + self.url)
        try:
            self.Chrome.find_element_by_xpath("//input[@id='login']").send_keys(self.email)
            self.Chrome.find_element_by_xpath("//input[@id='password']").send_keys(self.password)
            self.Chrome.find_element_by_xpath("//input[@class='bouton_wide primary floatright']").click()
            time.sleep(1)
        except:
            self._bug_rep.append("Can't Login (Wrong login or password")
        try:
            if self.post_on_my_page == "1":
                    print("dsf") #Не готово.
        except:
            self._bug_rep.append("Can't post on my page")