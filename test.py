from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Locate local copy of chromedriver on win 10.
# PATH = "/home/mrana/Codes_And_Experiments/DataScienceUtilityProjects/chromedriver"
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
    posts = blog.find_elements_by_tag_name("h2")
    dates = blog.find_elements_by_css_selector("p.card-text")

    print(len(dates))
    print("0", dates[0].text)
    print("1", dates[1].text)
    print("2", dates[2].text)
    print("3", dates[3].text)

    # for date in dates:
    #     print(date.text)

    print(f"Total {len(posts)} posts found")

    for i in range(len(posts)):
        print(f"Post number {i+1}: ", posts[i].text, "by", dates[i*2].text)
finally:
    driver.quit()

# By xpath