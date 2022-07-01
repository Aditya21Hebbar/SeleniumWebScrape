from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

grab_url='https://food.grab.com/sg/en/restaurants'

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headers')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

def get_titles(driver):
  driver.get(grab_url)
  title_div_class ='name___2epcT' 
  title = driver.find_elements(By.CLASS_NAME,title_div_class)
  return title

if __name__ == "__main__":
  print("creating driver")
  driver = get_driver()
  print('fetching the top list restaurants')
 
  title_divs = get_titles(driver)
  print('Found titles number',len(title_divs))

  print('Parsing the first div')