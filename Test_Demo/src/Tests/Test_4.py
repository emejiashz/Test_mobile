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
        #desired_caps['appPackage'] = 'com.mercariapp.mercari'
        #desired_caps['appActivity'] = 'com.mercari.ramen.LaunchActivity'
        desired_caps['NoReset'] = True
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
        
    def esperar_Registro_titulo(self):
        driver = self.driver
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.visibility_of_element_located((By.ID, "com.mercadolibre:id/home_onboarding_register_title")))
            
        except TimeoutException:
        
            print (u"esperar_Registro_titulo: No pesente")
            return False
        
        print (u"esperar_Registro_titulo: Se mostró el elemento ")
        return True
    
    def text_Registro_Titulo(self):
        driver = self.driver
        try:
            
            texto = driver.find_element(By.ID, "com.mercadolibre:id/home_onboarding_register_title").text
            
        except NoSuchElementException:
            
            print (u"text_Registro_Titulo: Elemento no pesente")
            return False
        
        print (u"text_Registro_Titulo: Se visualizo el texto, " + texto)
        
        return texto

    def text_Registro_subtitulo(self):
        driver = self.driver
        try:
            
            texto = driver.find_element(By.ID, "com.mercadolibre:id/home_onboarding_register_subtitle").text
            
        except NoSuchElementException:
            
            print (u"text_Registro_subtitulo: Elemento no pesente")
            return False
        
        print (u"text_Registro_subtitulo: Se visualizo el texto, " + texto)
        
        return texto   
    
    def esperar_btnFacebook(self):
        driver = self.driver
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.visibility_of_element_located((By.ID, "com.mercadolibre:id/home_onboarding_facebook_register_button")))
            
        except TimeoutException:
        
            print (u"esperar_btnFacebook: No pesente")
            return False
        
        print (u"esperar_btnFacebook: Se mostró el elemento ")
        return True
    
    def text_btnFacebook(self):
        driver = self.driver
        try:
            
            texto = driver.find_element(By.ID, "com.mercadolibre:id/home_onboarding_facebook_register_button").text
            
        except NoSuchElementException:
            
            print (u"text_btnFacebook: Elemento no pesente")
            return False
        
        print (u"text_btnFacebook: Se visualizo el texto, " + texto)
        
        return texto   
    
    def esperar_btnEmail(self):
        driver = self.driver
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.visibility_of_element_located((By.ID, "com.mercadolibre:id/home_onboarding_email_register_button")))
            
        except TimeoutException:
        
            print (u"esperar_btnEmail: No pesente")
            return False
        
        print (u"esperar_btnEmail: Se mostró el elemento ")
        return True
    
    def text_btnEmail(self):
        driver = self.driver
        try:
            
            texto = driver.find_element(By.ID, "com.mercadolibre:id/home_onboarding_email_register_button").text
            
        except NoSuchElementException:
            
            print (u"text_btnEmail: Elemento no pesente")
            return False
        
        print (u"text_btnEmail: Se visualizo el texto, " + texto)
        
        return texto
    
    def text_lblTerminos(self):
        driver = self.driver
        try:
            
            texto = driver.find_element(By.ID, "com.mercadolibre:id/home_onboarding_step_terms_text").text
            
        except NoSuchElementException:
            
            print (u"text_lblTerminos: Elemento no pesente")
            return False
        
        print (u"text_lblTerminos: Se visualizo el texto, " + texto)
        
        return texto
    
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
    
    def test_004(self):
        driver = self.driver
        self.esperar_Inicio()
        
    
        self.swipe()
        self.swipe()
        self.swipe()
        self.esperar_Registro_titulo()
        self.esperar_btnFacebook()
        self.esperar_btnEmail()
        self.text_lblTerminos()
        self.esperar_btnAlready()
        
        self.assertEqual("¿Qué estás esperando?", self.text_Registro_Titulo())
        self.assertEqual("¡Es gratis!", self.text_Registro_subtitulo())
        self.assertEqual("Registrarme con Facebook", self.text_btnFacebook())
        self.assertEqual("Registrarme con mi e-mail", self.text_btnEmail())
        self.assertEqual("Ya tengo cuenta", self.text_btnAlready())
        
        self.capturarPantalla(driver)


        

    def tearDown(self):
        self.driver.quit()
          
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MeliAppium)
    unittest.TextTestRunner(verbosity=2).run(suite)