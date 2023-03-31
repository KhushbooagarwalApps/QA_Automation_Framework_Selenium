from selenium import webdriver
from pageObjects.loginPage import login
import pytest
from Utilities.readProperties import readConfig
from Utilities.customLogger import LogGen

class Test_001_login:
    baseURL=readConfig.getApplicationUrl()
    username=readConfig.getUsername()
    password=readConfig.getPassword()

    logger=LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression

    def test_loginpgTitle(self,setup):

        self.logger.info("******* TC001_Login_Title *******")

        self.driver=setup
        self.driver.get(self.baseURL)
        res_title=self.driver.title
        if res_title=="dcbbcbnzxn":
            assert True
            self.driver.close()
            self.logger.info("******* TC001_Login_Title_Passed *******")
        else:
            self.driver.save_screenshot("E-commerce_Usecase/Screenshots/"+"TC001_loginpageTitle.png")
            self.driver.close()
            self.logger.info("******* TC001_Login_Title_Fail *******")
            assert False
            
    
    @pytest.mark.regression

    def test_login(self,setup):

        self.logger.info("******* TC001_Login_check *******")

        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=login(self.driver)
        self.lp.setUser(self.username)
        self.lp.setPass(self.password)
        self.lp.login()
        rev_title=self.driver.title
        
        if rev_title=="Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("******* TC001_Login_check_pass *******")
            assert True
        else:
            self.driver.save_screenshot("E-commerce_Usecase/Screenshots/"+"TC001_test_login.png")
            self.driver.close()
            self.logger.info("******* TC001_Login_check_failed *******")
            assert False
            
        
