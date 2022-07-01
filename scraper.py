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

if __name__ == "__main__":
  print("creating driver")
  driver = get_driver()

  print('fetching the page')
  driver.get(grab_url)
  print('Page title',driver.title)
  
  print('get title divs')
  title_div_class ='name___2epcT' 
  title_divs = driver.find_elements(By.CLASS_NAME,title_div_class)
  print('Found  titles',len(title_divs))