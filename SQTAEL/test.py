from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_driver_path = "D:\\projects\\chromedriver-win64\\chromedriver.exe"
service = Service(chrome_driver_path)


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.get("https://magento.softwaretestingboard.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

try:
  
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign In"))).click()

    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys("vandana123@gmail.com")
    driver.find_element(By.ID, "pass").send_keys("Vandana2001")
    driver.find_element(By.ID, "send2").click()

  
    search_box = wait.until(EC.presence_of_element_located((By.ID, "search")))
    search_box.send_keys("Jacket")
    search_box.send_keys(Keys.RETURN)


    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-item-link"))).click()

 
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'swatch-option')][@option-label='M']"))).click()

    
    color_selected = False
    color_options = driver.find_elements(By.CLASS_NAME, "swatch-option")
    for color in color_options:
        if "Purple" in color.get_attribute("aria-label"):
            color.click()
            color_selected = True
            break

    if not color_selected:
        raise Exception("Blue color option not found!")


    wait.until(EC.element_to_be_clickable((By.ID, "product-addtocart-button"))).click()
    

   
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".showcart"))).click()


    wait.until(EC.element_to_be_clickable((By.ID, "top-cart-btn-checkout"))).click()
    print(" Item added to cart successfully ")

    print(" Automation completed successfully ")

except Exception as e:
    print(f"[ERROR] {e}")

finally:
    driver.quit()