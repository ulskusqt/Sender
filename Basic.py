from pynput.keyboard import Controller
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Basic(object):
    def __init__(self, eml, pw, txt, link, pdt, pop, pog, title, image_link, hashtags, gr_links, priority):
        self.email = eml  # user email
        self.password = pw  # user password
        self.text = txt  # text to post
        self.link = link  # link to attach
        self.post_date_time = pdt  # date and time then to post the post / if empty then post now
        self.post_on_my_page = pop  # 0 - don't post on my page / 1 - post on my page
        self.post_on_groups = pog
        self.title = title
        self.image_link = image_link
        self.hashtags = hashtags
        self.gr_links = gr_links
        self.priority = priority
        self._keyboard = Controller()

        self._bug_rep = []
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-notifications")
            self.Chrome = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
            self.Chrome.maximize_window()
        except Exception as e:
            self._bug_rep.append(e)

    def get_bugrep(self):
        return self._bug_rep

    def run_key(self, key):
        self._keyboard.press(key)
        self._keyboard.release(key)

    def type(self, text):
        self._keyboard.type(text)