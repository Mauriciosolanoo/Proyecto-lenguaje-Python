import unittest
from datetime import time


class Page(unittest.TestCase):

    def __init__(self, selenium_driver, base_url='www,lineru.com/'):
        self.base_url = base_url
        self.driver = selenium_driver
        # Visit and initialize xpaths for the appropriate page
        self.start()

    def open(self, url):

        url = self.base_url + url
        self.driver.get(url)

    def write(self, msg, level='info'):
        self.log_obj.write(msg, level)

    def wait(self, wait_seconds=5):
        time.sleep(wait_seconds)

