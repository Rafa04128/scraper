from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try:
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)

    # Navigate to the bet365 website
    url = 'https://www.bet365.com/#/AC/B18/C20888701/D1/E90187283/F2/'
    driver.get(url)

    # Click the cookie consent popup
    cookies = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ccm-CookieConsentPopup_Accept")))
    wait.until_not(EC.presence_of_element_located((By.CLASS_NAME, "bl-Preloader_SpinnerContainer")))
    cookies.click()

    # Wait for the page to stabilize
    wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    # Click the login button
    login_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "hm-MainHeaderRHSLoggedOutWide_Login")))
    login_button.click()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser window
    driver.quit()