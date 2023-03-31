from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class login:

    username_id="Email"
    password_id="Password"
    btnLI_xpath='/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form//button[text()="Log in"]'
                
    btnLO_linkText='//*[@id="navbarText"]/ul/li[3]/a'

    def __init__(self,driver):
        self.driver=driver

    def setUser(self,username):
        self.driver.find_element(By.ID,self.username_id).clear()
        self.driver.find_element(By.ID,self.username_id).send_keys(username)

    def setPass(self,password):
        self.driver.find_element(By.ID,self.password_id).clear()
        self.driver.find_element(By.ID,self.password_id).send_keys(password)

    def login(self):
        lin=WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,self.btnLI_xpath)))
        lin.click()

    def logout(self):
        logoff=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.btnLO_linkText)))
        logoff.click()