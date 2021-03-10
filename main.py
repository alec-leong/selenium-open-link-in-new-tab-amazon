from path import chromedriver_rel_path
from selenium import webdriver
from selenium.common.exceptions import MoveTargetOutOfBoundsException, ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Chromedriver.
driver = webdriver.Chrome(chromedriver_rel_path)

# Driver configuration.
driver.implicitly_wait(2)
driver.maximize_window()

# Fetch webpage.
driver.get('https://www.amazon.com/')

# Open link in new tab.
anchors = driver.find_elements_by_css_selector('div[id="nav-xshop-container"] a')
for anchor in anchors:
    try:
        anchor.send_keys(Keys.CONTROL, Keys.ENTER)
    except ElementNotInteractableException as e:
        try:
            ActionChains(driver).move_to_element(anchor).perform()
            anchor.send_keys(Keys.CONTROL, Keys.ENTER)
        except MoveTargetOutOfBoundsException as e:  # Disability Customer Support
            # Screenshot invisible element.
            driver.save_screenshot('screenshot-invisible-disability-customer-support-anchor.png')

            # Element visible.
            driver.execute_script('document.querySelector(\'a[aria-label="Click to call our Disability Customer Support'
                                  ' line, or reach us directly at 1-888-283-1678"]\').className = "nav-a"')
            # Screenshot visible element.
            driver.save_screenshot('screenshot-visible-disability-customer-support-anchor.png')

            # Open link in new tab.
            anchor.send_keys(Keys.CONTROL, Keys.ENTER)

# Switch window.
parent_handle = driver.current_window_handle
for handle in driver.window_handles:
    driver.switch_to.window(handle)
driver.switch_to.window(parent_handle)
