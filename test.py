from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Locate local copy of chromedriver on win 10.
PATH = "C:\Program Files (x86)\chromedriver\chromedriver.exe"

driver = webdriver.Chrome(PATH)  # Wont work without this locally
# driver.get("https://tomislam.com")
# print("This is the title", driver.title)

# This function waits for the element to capture without disrupting the process or closing browser too quickly.
"""try:
    page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "page"))
    )
    print(page.text)
finally:
    driver.quit()"""

# Lets try something different this time.
driver.get("https://www.tomislam.com/blog/")  # Pointing at the blog section.


try:
    blog = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.col-lg-8"))  # Easy to find by ID and then manipulate inside it.
    )
    posts = blog.find_elements_by_xpath('//*[@id="about"]/div[3]/div/div/div[2]/div[1]/div[1]/div/h2')
    dates = blog.find_elements_by_css_selector("p.card-text")

    for i in range(len(dates)):
        print(dates[i].text)

    print(f"Total {len(posts)} posts found")

    for i in range(len(posts)):
        print(f"Post number {i+1}: ", posts[i].text, "by", dates[i].text)
        print("*******", dates[1].text)
finally:
    driver.quit()

# The output is, it can show how many articles are there in BLOG page along with name of blogger and date.