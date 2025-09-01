from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8000")

service = Service(executable_path="C:\\ProgramData\\chocolatey\\bin\\chromedriver.exe")
# Create a new Chrome browser instance using Service
driver = webdriver.Chrome(service=service, options=opt)

# opening the ID
link = "https://in.linkedin.com/in/sahin-ahmed-469354170"
driver.get(link)

try:
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    html_content = driver.page_source
    with open("page_source.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("✅ Page source saved successfully!")
except Exception as e:
    print(f"❌ Error saving page source: {e}")
finally:
    driver.quit()