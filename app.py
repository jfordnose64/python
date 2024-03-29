from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# import username from './stuff.py'
# import password from './stuff.py'


class TwitterBot:
    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query')
        time.sleep(3)
        for i in range(1, 10):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets = [i.get_attribute('href')
                      for i in bot.find_elements_by_xpath("//a[@dir='auto']")]
            filteredLinks = list(filter(lambda x: 'status' in x, tweets))
            # print(filteredLinks)

            for link in filteredLinks:
                bot.get(link)
                time.sleep(5)
                try:
                    bot.find_element_by_xpath(
                        "//div[@data-testid='like']").click()
                    time.sleep(30)
                except Exception as ex:
                    time.sleep(60)
            # links = [elem.get_attribute('data-permalink-path')
            #          for elem in tweets]
            # print(links)
            # for link in links:
            #     bot.get('https://twitter.com' + link)
            #     try:
            #         bot.find_element_by_class_name('Heart-animation').click()
            #         time.sleep(10)
            #     except Exception as ex:
            #         time.sleep(60)


ed = TwitterBot('xxxx', 'xxxxxx')
ed.login()
ed.like_tweet('javascript')
