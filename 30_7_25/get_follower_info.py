from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\hp\AppData\Local\Google\Chrome\User Data')

options.add_argument("--remote-debugging-port=9222")
driver = webdriver.Chrome(options=options)


driver.maximize_window()

print("works_till_here")
driver.get("https://instagram.com")
print("works_till_here_1")