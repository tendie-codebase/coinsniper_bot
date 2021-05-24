# Step 1. pip install selenium + pip install free-proxy
# Step 2 run this file
import time

ERROR_MSG = "ReCaptcha error. Please wait a few seconds and try again."
total_votes = 0
votes_passed = 0
votes_failed = 0

for i in range(10000):
    from selenium import webdriver
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

    PROXY = '62.210.205.97:19018'  # SET PROXY HERE

    #print(PROXY)
    webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
        "httpProxy": PROXY,
        "proxyType": "MANUAL",
    }
    from selenium.webdriver.firefox.options import Options
    options = Options()
    options.add_argument("--headless")
    from fake_useragent import UserAgent
    ua = UserAgent()
    a = ua.random
    user_agent = ua.random
    #print(user_agent)
    options.add_argument(f'user-agent={user_agent}')
    try:
        driver = webdriver.Firefox(firefox_profile=firefox_profile, options=options)
    except:
        time.sleep(1)
        driver = webdriver.Firefox(firefox_profile=firefox_profile, options=options)
    action = webdriver.ActionChains(driver)
    # Open URL
    driver.get("https://coinsniper.net/coin/171")
    #time.sleep(1)
    btn = driver.find_element_by_xpath('/html/body/section[2]/div/div[2]/div/div[1]/div[6]/form/button')
    time.sleep(2)
    driver.execute_script("arguments[0].scrollIntoView();", btn)
    time.sleep(0.5)
    action.move_to_element(btn)
    action.perform()
    time.sleep(1.3)
    btn.click()
    time.sleep(1)
    try:
        response = driver.find_element_by_xpath('//div[contains(concat(" ",normalize-space(@class)," ")," message ")]').text

        if response == ERROR_MSG:
            votes_failed += 1
            print("Vote failed.")
        else:
            votes_passed += 1
            print("Vote passed.")
            
    except Exception as e:
        pass
    finally:
        total_votes += 1
    

    driver.close()
    driver.quit()
    time.sleep(1)


print("************************************")
print("* Total votes: ", total_votes)
print("* Votes passed: ", votes_passed)
print("* Votes failed: ", votes_failed)

        
