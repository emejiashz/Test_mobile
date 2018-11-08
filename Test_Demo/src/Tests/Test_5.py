# -*- coding: utf-8 -*-
import unittest, time, os
from appium import webdriver

from selenium.common.exceptions import TimeoutException  
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

dia = time.strftime("%Y-%m-%d")  # formato aaaa/mm/dd
hora = time.strftime("%H%M%S")  # formato 24 houras

class MeliAppium(unittest.TestCase):
    
    driver = None
    
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'android'
        desired_caps['platformVersion'] = '5.0.1'
        desired_caps['deviceName'] = 'GT-I9500'
        desired_caps['udid'] = '4d00261bbbe450a3'
        desired_caps['app'] = 'C:\\AppiumFramework\\APK\\com.mercadolibre.apk'
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_caps)
    
    # nomenclatura de la evidencia: número_caso_de_prueba + hora [hh:mm:ss]
    def capturarPantalla(self, driver):
        path = "../Screenshots/" + "/" + dia + "/"

        if not os.path.exists(path): # si no existe el directorio lo crea

            os.makedirs(path)

        driver.save_screenshot(path + self.__class__.__name__ + "_(" + hora + ")" + ".png")    

    def swipe(self):
        driver = self.driver
        
        screen = TouchAction(driver)
        screen.press(x=855, y=514)
        screen.move_to(x=-709, y=-15)
        screen.release().perform()
        

    def esperar_Actualizar(self):
        driver = self.driver
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.visibility_of_element_located((By.ID, "android:id/message")))
            
        except TimeoutException:
        
            print (u"esperar_Actualizar: No pesente")
            return False
        
        
        print (u"esperar_Actualizar: Se mostró el elemento ")
        locator  = driver.find_element_by_id("android:id/button2")
        locator.click()
        return True
    
    def esperar_btnAlready(self):
        driver = self.driver
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.visibility_of_element_located((By.ID, "com.mercadolibre:id/home_onboarding_already_has_account_button")))
            
        except TimeoutException:
        
            print (u"esperar_btnAlready: No pesente")
            return False
        
        print (u"esperar_btnAlready: Se mostró el elemento ")
        return True
    
    def text_btnAlready(self):
        driver = self.driver
        try:
            
            texto = driver.find_element(By.ID, "com.mercadolibre:id/home_onboarding_already_has_account_button").text
            
        except NoSuchElementException:
            
            print (u"text_btnAlready: Elemento no pesente")
            return False
        
        print (u"text_btnAlready: Se visualizo el texto, " + texto)
        
        return texto   
    
    def esperar_Inicio(self):
        driver = self.driver
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.visibility_of_element_located((By.ID, "com.mercadolibre:id/home_onboarding_step_title")))
            
        except TimeoutException:
        
            print (u"esperar_Inicio: No pesente")
            return False
        
        print (u"esperar_Inicio: Se mostró el elemento ")
        return True
    
    def btnAlready_id_click(self):  
        driver = self.driver 
        locator  = driver.find_element_by_id("com.mercadolibre:id/home_onboarding_already_has_account_button")
        locator.click()
        
    def esperar_txt_Usuario(self):
        driver = self.driver
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.visibility_of_element_located((By.ID, "com.mercadolibre:id/ui_text_field_input")))
            
        except TimeoutException:
        
            print (u"esperar_txt_Usuario: No pesente")
            return False
        
        print (u"esperar_txt_Usuario: Se mostró el elemento ")
        return True
    
    def text_TituloUser(self):
        driver = self.driver
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.visibility_of_element_located((By.ID, "com.mercadolibre:id/login_username_text")))

        except TimeoutException:
        
            print (u"text_TituloUser: No pesente")
            return False
        
        print (u"text_TituloUser: Se mostró el elemento ")
        return True
    
    def txt_Usuario_id_click(self):  
        driver = self.driver 
        locator  = driver.find_element_by_id("com.mercadolibre:id/ui_text_field_input")
        locator.click()
        
    def txt_Usuario_id_sendKeys(self):  
        driver = self.driver 
        locator  = driver.find_element_by_id("com.mercadolibre:id/ui_text_field_input")
        locator.send_keys("devbaires")
        
    def btn_Continue_id_click(self):  
        driver = self.driver 
        locator  = driver.find_element_by_id("com.mercadolibre:id/login_continueButton")
        locator.click()
    
    def esperar_btn_Ingresar(self):
        driver = self.driver
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.visibility_of_element_located((By.ID, "com.mercadolibre:id/login_ingresarButton")))
            
        except TimeoutException:
        
            print (u"esperar_btn_Ingresar: No pesente")
            return False
        
        print (u"esperar_btn_Ingresar: Se mostró el elemento ")
        return True    
    
    def text_TituloPass(self):
        driver = self.driver 
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.visibility_of_element_located((By.ID, "com.mercadolibre:id/login_password_text")))
            
        except TimeoutException:
        
            print (u"text_TituloPass: No pesente")
            return False
        
        print (u"text_TituloPass: Se mostró el elemento ")
        return True
    
    def txt_Pass_id_sendKeys(self):  
        driver = self.driver 
        locator  = driver.find_element_by_id("com.mercadolibre:id/ui_text_field_input")
        locator.send_keys("298258233")   
        
    def btn_VerPass_AccId_click(self):  
        driver = self.driver 
        locator  = driver.find_element_by_accessibility_id("Toggle password visibility")
        locator.click()  
    
    def btn_Ingresar_id_click(self):  
        driver = self.driver 
        locator  = driver.find_element_by_id("com.mercadolibre:id/login_ingresarButton")
        locator.click()
        
    def esperar_btn_Menu(self):
        driver = self.driver
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "android.widget.ImageButton")))
            
        except TimeoutException:
        
            print (u"esperar_btn_Menu: No pesente")
            return False
        
        print (u"esperar_btn_Menu: Se mostró el elemento ")
        return True 
    
    def btn_Menu_AccId_click(self):  
        driver = self.driver 
        locator  = driver.find_element_by_accessibility_id("Desplazarse hacia arriba")
        locator.click()  
    
    def text_UserLoggin(self):
        driver = self.driver
        try:
            
            texto = driver.find_element(By.ID, "com.mercadolibre:id/sdk_navigation_header_user_info_title").text
            
        except NoSuchElementException:
            
            print (u"text_UserLoggin: Elemento no pesente")
            return False
        
        print (u"text_UserLoggin: Se visualizo el texto, " + texto)
        
        return texto   
    
    def test_004(self):
        driver = self.driver
        self.esperar_Actualizar()
        self.esperar_Inicio()
        self.swipe()
        self.swipe()
        self.swipe()
        
        #Pantalla se Seleccion de forma de ingreso
        #Seleccion en "Ya tengo Cuenta"
        
        self.esperar_btnAlready()
        self.capturarPantalla(driver)
        self.assertEqual("Ya tengo cuenta", self.text_btnAlready())
        self.btnAlready_id_click()
        
        #Ingreso de usuario
        self.esperar_txt_Usuario()
        self.assertTrue(True, self.text_TituloUser())
        self.txt_Usuario_id_click()
        self.txt_Usuario_id_sendKeys()
        self.capturarPantalla(driver)
        self.btn_Continue_id_click()
        
        #Ingreso de clave
        self.esperar_btn_Ingresar()
        self.assertEqual(True, self.text_TituloPass())
        self.txt_Pass_id_sendKeys()
        self.btn_VerPass_AccId_click()
        self.capturarPantalla(driver)
        self.btn_Ingresar_id_click()
        

        #Validar el usuario logueado
        self.esperar_btn_Menu()
        self.capturarPantalla(driver)
        self.btn_Menu_AccId_click()
        self.assertEqual("¡Hola Mervin!", self.text_UserLoggin())
        self.capturarPantalla(driver)
    


        



        

    def tearDown(self):
        self.driver.quit()
          
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MeliAppium)
    unittest.TextTestRunner(verbosity=2).run(suite)