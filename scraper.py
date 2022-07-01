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

def get_restaurant(driver):
  driver.get(grab_url)
  restaurant_div_class ='asList___1ZNTr' 
  restaurant = driver.find_elements(By.CLASS_NAME,restaurant_div_class)
  return restaurant

if __name__ == "__main__":
  print("creating driver")
  driver = get_driver()
  print('fetching the top list restaurants')
 
  restaurants = get_restaurant(driver)
  print('Found restaurants ',len(restaurants))

  print('Parsing the first div')
  # Now in restaurants we have a list of 
  # restaurants which includes all the info but we
  # might only want title which could help us later
  restaurant_title_div_class ='name___2epcT' 
  restaurants_title = driver.find_elements(By.CLASS_NAME,restaurant_title_div_class)
  restaurant_title_tag= restaurants_title[0]
  restaurant_title = restaurant_title_tag.text
  print(restaurant_title)