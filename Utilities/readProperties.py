import configparser

config=configparser.RawConfigParser()
config.read("E-commerce_Usecase/configuration/config.ini")

class readConfig:

    @staticmethod
    def getApplicationUrl():
        url=config.get('login info','baseURL')
        return url

    @staticmethod
    def getUsername():
        user=config.get('login info','username')
        return user

    @staticmethod
    def getPassword():
        pwd=config.get('login info','password')
        return pwd