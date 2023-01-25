from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

def test_amazon():

    driver = webdriver.Chrome()
    #driver = webdriver.Chrome(executable_path=r"/Users/marenrindfleisch/Downloads/chromedriver_mac64/")

    driver.get("https://www.amazon.de/")
    assert "Amazon" in driver.title

    #driver.implicity_wait(0.5)

    input = driver.find_element("id","twotabsearchtextbox")

    input.send_keys("adidas schuhe")
    input.send_keys(Keys.ENTER)
    


    firstItem = driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div/div[1]/div/span')
    firstItem.click
    print(firstItem)

    
    driver.close()





