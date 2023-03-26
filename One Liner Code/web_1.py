

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

browser_locale = 'en'
chrome_driver_path = "E:\chromedriver_win32\chromedriver.exe"

options = Options()
options.add_argument("--lang={}".format(browser_locale))

browser = webdriver.Chrome(executable_path=chrome_driver_path,
                           chrome_options=options)
browser.get('https://google.com/')
