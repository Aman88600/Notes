import os
import time
import random
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

# Load environment variables
load_dotenv()
BOT_USERNAME = os.getenv("INSTAGRAM_USERNAME")
BOT_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

# Global variables
bot_username = BOT_USERNAME
bot_password = BOT_PASSWORD
profiles = ['gunther.super']  # Add profiles to scrape
amount = 30  # Number of followers to scrape
result = 'usernames'  # Save usernames

class Instagram():
    def __init__(self, username, password):
        self.username = username
        self.password = password

        chrome_options = Options()
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        chrome_options.add_argument("--window-size=400,900")
        # chrome_options.add_argument("--headless")  # Keep this commented to see the window

        service = Service(executable_path=r"C:\ProgramData\chocolatey\bin\chromedriver.exe")
        self.browser = webdriver.Chrome(service=service, options=chrome_options)

    def close_browser(self):
        self.browser.quit()

    def login(self):
        browser = self.browser
        try:
            browser.get('https://www.instagram.com')
            time.sleep(random.uniform(3, 5))  # Random delay between 3-5 seconds
            
            # Enter username:
            username_input = browser.find_element(By.NAME, 'username')
            username_input.clear()
            username_input.send_keys(self.username)
            time.sleep(random.uniform(2, 4))
            
            # Enter password:
            password_input = browser.find_element(By.NAME, 'password')
            password_input.clear()
            password_input.send_keys(self.password)
            time.sleep(random.uniform(1, 2))
            password_input.send_keys(Keys.ENTER)
            time.sleep(random.uniform(3, 5))

            print(f'[{self.username}] Successfully logged in!')
        except Exception as ex:
            print(f'[{self.username}] Login failed. Exiting... Error: {ex}')
            self.close_browser()

    def xpath_exists(self, xpath):
        """Check if element exists on the page using XPath."""
        try:
            self.browser.find_element(By.XPATH, xpath)
            return True
        except NoSuchElementException:
            return False

    def get_followers(self, users, amount):
        followers_list = []
        for user in users:
            self.browser.get(f'https://instagram.com/{user}')
            time.sleep(random.uniform(3, 5))

            # Wait for followers button to be available
            followers_button_xpath = '/html/body/div[1]/section/main/div/ul/li[2]/a/span'
            if not self.xpath_exists(followers_button_xpath):
                print(f'Error: Unable to find followers button for {user}. Skipping...')
                continue

            followers_button = self.browser.find_element(By.XPATH, followers_button_xpath)
            count = followers_button.get_attribute('title')

            if ',' in count:
                count = int(''.join(count.split(',')))
            else:
                count = int(count)

            if amount > count:
                print(f'You set amount = {amount}, but there are only {count} followers. Adjusting amount.')
                amount = count

            followers_button.click()

            loops_count = int(amount / 12)
            print(f'Scraping {amount} followers. Total iterations: {loops_count}')
            time.sleep(random.uniform(5, 7))

            followers_ul_xpath = "/html/body/div[6]/div/div/div[2]"
            if not self.xpath_exists(followers_ul_xpath):
                print(f'Error: Unable to find followers list for {user}. Skipping...')
                continue

            followers_ul = self.browser.find_element(By.XPATH, followers_ul_xpath)
            time.sleep(random.uniform(5, 7))

            try:
                with open('userlist.txt', 'w') as f3:  # Open file once
                    for i in range(1, loops_count + 1):
                        self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_ul)
                        time.sleep(random.uniform(8, 10))

                        all_div = followers_ul.find_elements(By.TAG_NAME, "li")
                        for us in all_div:
                            us = us.find_element(By.TAG_NAME, "a").get_attribute("href")
                            if result == 'usernames':
                                us = us.replace("https://www.instagram.com/", "").replace("/", "")
                            followers_list.append(us)

                        # Write to file after every loop
                        for list_item in followers_list:
                            f3.write(list_item + '\n')
                        print(f'Got: {len(followers_list)} usernames of {amount}. Saved to file.')

                time.sleep(random.uniform(3, 5))

            except Exception as ex:
                print(f'Error scraping followers for {user}: {ex}')
                self.close_browser()

        return followers_list


# Running the bot
bot = Instagram(bot_username, bot_password)

# Log in only once
bot.login()

# Get followers
followers = bot.get_followers(profiles, amount)

# Close browser after scraping
bot.close_browser()
