import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.headless = True  # Run in headless mode
driver = webdriver.Firefox(options=options)


# Politico
url = 'https://www.politico.com/'
driver.get(url)
url = driver.current_url  # Update url after navigation

headline = 'none'
link = 'none'

try:
    # Get page content
    article = driver.find_element(By.CSS_SELECTOR, 'div.page-content')

    # Get headline
    headline_element = article.find_element(By.CSS_SELECTOR, 'h3.headline')
    headline = headline_element.text

    # Get link
    link = headline_element.find_element(
        By.TAG_NAME, 'a').get_attribute('href')

except NoSuchElementException:
    print('Element not found')

# Write to CSV
data = {
    'site': url,
    'headline': headline,
    'link': link,
}

print({
    'site': url,
    'headline': headline,
    'link': link,
})

with open('articles.csv', 'a', newline='') as csvfile:
    fieldnames = ['site', 'headline', 'link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow(data)

# NPR
url = 'https://www.npr.org/'
driver.get(url)
url = driver.current_url  # Update url after navigation

driver.get(url)

try:
    # Get page content
    article = driver.find_element(By.CSS_SELECTOR, 'section#main-section')

    # Get headline
    headline_element = article.find_element(By.CSS_SELECTOR, 'h3.title')
    headline = headline_element.text

    # Get link
    link = headline_element.find_element(
        By.TAG_NAME, 'a').get_attribute('href')

except NoSuchElementException:
    print('Element not found')

# Update data with NPR data
data = {
    'site': url,
    'headline': headline,
    'link': link,
}

print({
    'site': url,
    'headline': headline,
    'link': link,
})

with open('articles.csv', 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow(data)


driver.quit()