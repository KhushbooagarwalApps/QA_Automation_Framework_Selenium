import logging

class LogGen :

    @staticmethod
    def loggen():
        logging.basicConfig(filename="E-commerce_Usecase/logs/"+"automation.log",mode='a',
                        format='%(asctime)s: %(levelname)s: %(message)s', datefrt='%m/%d/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger