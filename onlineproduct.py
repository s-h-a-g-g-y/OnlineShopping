import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

product = input("Enter the product you need to search!!")
product = product.title()

browser = webdriver.Firefox()
browser.get('https://www.flipkart.com/')
linkElem = browser.find_element_by_css_selector('input[class=LM6RPg]')
linkElem.send_keys(product)
linkElem.submit()
time.sleep(10)
try:
    prod_title = browser.find_elements_by_class_name("_2cLu-l")
    prod_price = browser.find_elements_by_class_name("_1vC4OE")
    if not prod_title:
        prod_title = browser.find_elements_by_class_name("_3wU53n")
except:
    print("Sorry! Product can't be found on Flipkart!!")

cnt=0
print("These products are available on Flipkart!!!")
print()
for title , price in zip(prod_title,prod_price):
    cnt+=1
    print(title.text)
    print(price.text)
    if(cnt>10):
        break

print()
browser.get('https://www.snapdeal.com/')
linkElem = browser.find_element_by_xpath('//input[@id="inputValEnter"]')
linkElem.send_keys(product,Keys.ENTER)
time.sleep(10)
try:
    prod_title = browser.find_elements_by_class_name('product-title')
    prod_price = browser.find_elements_by_class_name('product-price')
except:
    print("Sorry! Product can't be found on Snapdeal!!")
cnt=0
print("These products are available on Snapdeal!!!")
print()
for title , price in zip(prod_title,prod_price):
    cnt+=1
    print(title.text)
    print(price.text)
    if(cnt>10):
        break

print()


browser.get("https://www.myntra.com/")
linkElem = browser.find_element_by_xpath('//input[@class="desktop-searchBar"]')
linkElem.send_keys(product,Keys.ENTER)
time.sleep(10)
try:
    prod_brand = browser.find_elements_by_class_name('product-brand')
    prod_title = browser.find_elements_by_class_name('product-product')
    prod_price = browser.find_elements_by_class_name('product-discountedPrice')
except:
    print("Sorry! Product can't be found on Myntra!!")

cnt=0
print("These products are available on Myntra!!!")
print()
for brand, title , price in zip(prod_brand,prod_title,prod_price):
    cnt+=1
    print(brand.text," ",title.text)
    print(price.text)
    if(cnt>10):
        break
