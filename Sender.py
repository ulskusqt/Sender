from pynput.keyboard import Key, Controller
from Facebook import Facebook
from Google import Google
from Instagram import Instagram
from LinkedIn import LinkedIn
from MySpace import MySpace
from Odnoklassniki import Odnoklassniki
from Plurk import Plurk
from Reddit import Reddit
from Skyrock import Skyrock
from Tumblr import Tumblr
from Twitter import Twitter
from Vkontakte import Vkontakte
from WeHear import WeHear



json = {
    "id": "li",
    'url': "https://www.linkedin.com/",
    "login": "uls.kusqt@gmail.com",
    'pass': 'i60405891',
    'text': 'sdfdsgdfh ghfjghj hgfdesfsd asdfaf sd f fshdfh',
    'link': 'https://www.exportportal.com/register',
    'datetime': '',
    "server": "eu",
    'title': 'title',
    'image_link': 'https://pp.userapi.com/c844520/v844520448/bd4e7/wbIdUkZLEJ8.jpg',
    'hashtags': '',
    'page_post': '1',
    "groupe_post": '1',
    "gropes_links": 'link1, link2, link3',
    'priority': "",

}


if json['id'] == "fb":
    FB = Facebook(json['login'], json['pass'], json['text'], json['link'], json['datetime'],
                  json['page_post'], json['groupe_post'], json['title'] ,json['image_link'], json['hashtags'], json['gropes_links'], json["priority"])
    FB.post()
    print(FB.get_bugrep())
if json['id'] == "tw":
    TW = Twitter(json['login'], json['pass'], json['text'], json['link'], json['datetime'],
                  json['page_post'], json['groupe_post'], json['title'] ,json['image_link'], json['hashtags'], json['gropes_links'], json['priority'])
    TW.post()
    print(TW.get_bugrep())
if json['id'] == "vk":
    VK = Vkontakte(json['login'], json['pass'], json['text'], json['link'], json['datetime'],
                  json['page_post'], json['groupe_post'], json['title'] ,json['image_link'], json['hashtags'], json['gropes_links'], json["priority"])
    VK.post()
    print(VK.get_bugrep())
if json['id'] == "ok":
    OK = Odnoklassniki(json['login'], json['pass'], json['text'], json['link'], json['datetime'],
                  json['page_post'], json['groupe_post'], json['title'] ,json['image_link'], json['hashtags'], json['gropes_links'], json["priority"])
    OK.post()
    print(OK.get_bugrep())
if json['id'] == 'gp':
    GP = Google(json['login'], json['pass'], json['text'], json['link'], json['datetime'],
                  json['page_post'], json['groupe_post'], json['title'] ,json['image_link'], json['hashtags'], json['gropes_links'], json["priority"])
    GP.post()
    print(GP.get_bugrep())
if json['id'] == 'pl':
    PL = Plurk(json['login'], json['pass'], json['text'], json['link'], json['datetime'],
                  json['page_post'], json['groupe_post'], json['title'] ,json['image_link'], json['hashtags'], json['gropes_links'], json["priority"])
    PL.post()
    print(PL.get_bugrep())
if json['id'] == 'ms':
    MS = MySpace(json['login'], json['pass'], json['text'], json['link'], json['datetime'],
                  json['page_post'], json['groupe_post'], json['title'] ,json['image_link'], json['hashtags'], json['gropes_links'], json["priority"])
    MS.post()
    print(MS.get_bugrep())
if json['id'] == 'sk':
    SK = Skyrock(json['login'], json['pass'], json['text'], json['link'], json['datetime'],
                  json['page_post'], json['groupe_post'], json['title'] ,json['image_link'], json['hashtags'], json['gropes_links'], json['priority'])
    SK.post()
    print(SK.get_bugrep())
if json['id'] == 'wh':
    WH = WeHear(json['login'], json['pass'], json['text'], json['link'], json['datetime'],
                  json['page_post'], json['groupe_post'], json['title'] ,json['image_link'], json['hashtags'], json['gropes_links'], json['priority'])
    WH.post()
    print(WH.get_bugrep())
if json['id'] == 'rd':
   RD = Reddit(json['login'], json['pass'], json['text'], json['link'], json['datetime'],
                  json['page_post'], json['groupe_post'], json['title'] ,json['image_link'], json['hashtags'], json['gropes_links'], json['priority'])
   RD.post()
   print(RD.get_bugrep())
if json['id'] == 'li':
   LI = LinkedIn(json['login'], json['pass'], json['text'], json['link'], json['datetime'],
                  json['page_post'], json['groupe_post'], json['title'] ,json['image_link'], json['hashtags'], json['gropes_links'], json["priority"])
   LI.post()
   print(LI.get_bugrep())
if json['id'] == 'tr':
    TR = Tumblr(json['login'], json['pass'], json['text'], json['link'], json['datetime'],
                  json['page_post'], json['groupe_post'], json['title'] ,json['image_link'], json['hashtags'], json['gropes_links'])
    TR.post()
    print(TR.get_bugrep())



