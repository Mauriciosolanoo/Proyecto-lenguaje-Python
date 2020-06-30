from selenium import webdriver

class WebdriverFactory:

    def getWebdriver(browserName):
        if (browserName == 'firefox'):
            return webdriver.Firefox()
        elif (browserName == 'chrome'):
            return webdriver.Chrome("insumos/chromedriver.exe")
        elif (browserName == 'ie'):
            return webdriver.Ie()