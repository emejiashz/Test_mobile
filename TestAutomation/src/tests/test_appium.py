'''
Created on 13 sept. 2018

@author: Alejandro
'''
import unittest,time
from src.functions.Functions import Functions
from appium import webdriver
from appium.webdriver.mobilecommand import MobileCommand

class tst_a(unittest.TestCase,Functions):

    def setUp(self):
        
        desired_caps = {}
        desired_caps['platformName'] = 'android' 
        desired_caps['platformVersion'] = '6.0' 
        desired_caps['deviceName'] = 'YT911BA6UJ' 
        desired_caps['app'] = 'C:\\AppiumFramework\\APK\\sarahah-1-0-08.apk' 
        desired_caps['NoReset'] = True 
        self.driver = webdriver.Remote('http://127.0.0.1:5100/wd/hub', desired_caps)
        
    
    def test_a(self):
        
        self.esperar_Xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.ImageView" )
        
        self.driver.find_element_by_xpath( "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageButton").click()           
        self.driver.find_element_by_xpath( "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageButton").click()  
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.Button").click()
        self.esperar_Xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView")
        self.driver.hide_keyboard()
        self.driver.find_element_by_id("com.sarahah.android:id/register").click()
        self.driver.find_element_by_id("com.sarahah.android:id/username").send_keys("test001")
        self.driver.hide_keyboard()
        self.capturar_Pantalla()
        self.driver.find_element_by_id("com.sarahah.android:id/name").send_keys("test001")
        self.driver.hide_keyboard()
        self.driver.find_element_by_id("com.sarahah.android:id/email").send_keys("test001@gmail.com")
        self.driver.hide_keyboard()
        self.capturar_Pantalla()
        self.driver.find_element_by_id("com.sarahah.android:id/password").send_keys("123456789")
        self.driver.hide_keyboard()
        self.driver.find_element_by_id("com.sarahah.android:id/conf_password").send_keys("123456789")
        self.driver.hide_keyboard()
        self.driver.find_element_by_id("com.sarahah.android:id/terms_CB").click()
        self.driver.find_element_by_id("com.sarahah.android:id/email_sign_in_button").click() 
        self.driver.close_app()
        
        print('PRUEBA LISTA')
  
def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()