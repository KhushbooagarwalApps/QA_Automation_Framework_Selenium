from selenium import webdriver
from pageObjects.loginPage import login
import pytest
from Utilities.readProperties import readConfig
from Utilities.customLogger import LogGen
from Utilities import ExcelUtils
import time

class Test_002_login_via_data:
    baseURL=readConfig.getApplicationUrl()
    path="/Users/khushbooagarwal/Downloads/login_test_data.xlsx"

    logger=LogGen.loggen()

   
    @pytest.mark.regression
    def test_login_data(self,setup):

        self.logger.info("******* TC002_login_via_data *******")

        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=login(self.driver)

        self.rn=ExcelUtils.getRowCount(self.path,'Sheet1')
        tst_status=[]

        for r in range(2,self.rn+1):
            self.usr=ExcelUtils.readData(self.path,'Sheet1',r,1)
            self.pasd=ExcelUtils.readData(self.path,'Sheet1',r,2)
            self.expres=ExcelUtils.readData(self.path,'Sheet1',r,3)
            self.lp.setUser(self.usr)
            self.lp.setPass(self.pasd)
            self.lp.login()
            rev_title=self.driver.title
        
            if rev_title=="Dashboard / nopCommerce administration":
                if self.expres=="P":
                    self.lp.logout()
                    self.logger.info("******* TC002_Login_check_pass *******")
                    tst_status.append("Pass")
                    
                elif self.expres=="F":
                    self.lp.logout()
                    self.logger.info("******* TC002_Login_check_fail *******")
                    tst_status.append("Fail")

            elif rev_title != "Dashboard / nopCommerce administration":
                if self.expres=="P":
                    self.logger.info("******* TC002_Login_check_fail *******")
                    tst_status.append("Fail")
                    
                elif self.expres=="F":
                    self.logger.info("******* TC002_Login_check_pass *******")
                    tst_status.append("Pass")
        
        if "Fail" not in tst_status:
            self.logger.info("******* TC002_Login_check_pass completed*******")
            self.driver.quit()
            assert True
        else: 
            self.logger.info("******* TC002_Login_check_fail completed*******")
            self.driver.quit()
            assert False

        print(tst_status)
        
        
            
        
