import unittest, time
from appium import webdriver


class ContactAppTestAppium(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'android'
        desired_caps['platformVersion'] = '5.0.1'
        desired_caps['deviceName'] = 'GT-I9500'
        desired_caps['app'] = 'C:\\AppiumFramework\APK\\ar.com.santander.rio.mbanking.apk'
        desired_caps['NoReset'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(5)
        
    def test_ClickRefreshLink(self):
        refreshButton  = self.driver.find_element_by_id("ar.com.santander.rio.mbanking:id/messageAlert")
        self.assertTrue(refreshButton.is_displayed())
        refreshButton.click()
        

        ## Right now we are just verify the displayed message on the Phone
        ## You can right code to handle that toast message and Verify that message

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactAppTestAppium)
    unittest.TextTestRunner(verbosity=2).run(suite)


