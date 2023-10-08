from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from urllib.parse import urljoin
import Constantes as keys

options = Options()
options.add_experimental_option ("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

def getIpAddress():
    driver.get(keys.ROUTER_URL)
    driver.find_element(By.ID,"txt_Username").send_keys(keys.ROUTER_USERNAME)
    driver.find_element(By.ID,"txt_Password").send_keys(keys.ROUTER_PASSWORD)
    driver.find_element(By.ID,"button").click()
    driver.find_element(By.NAME,"subdiv_waninfo").click()
    time.sleep(5)
    src = driver.find_element(By.ID,"frameContent").get_attribute("src")
    url = urljoin(keys.ROUTER_URL, src)
    print('url',url)
    driver.get(url)
    ip = driver.find_element(By.XPATH,"/html/body/div[2]/table[2]/tbody/tr[2]/td[3]").text
    return "http://"+ip+"/"

def mockGetIpAddress():
    return keys.MOCKED_URL

def main():
    adrsIp = getIpAddress()
    #publishAdressJira(adrsIp)
    print(adrsIp)
    driver.close()


#if __name__ == "__main__":
    #main()