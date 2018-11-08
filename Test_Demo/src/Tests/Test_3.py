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
        
    def Esperar_Inicio(self):
        driver = self.driver
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.visibility_of_element_located((By.ID, "com.mercadolibre:id/home_onboarding_step_title")))
            
        except TimeoutException:
        
            print (u"Esperar_xpath: No pesente")
            return False
        
        print (u"Esperar_xpath: Se mostró el elemento ")
        return True
    
    def text_titulo(self):
        driver = self.driver
        try:
            
            texto = driver.find_element(By.ID, "com.mercadolibre:id/home_onboarding_step_title").text
            
        except NoSuchElementException:
            
            print (u"Verificar: Elemento no pesente")
            return False
        
        print (u"Verificar: Se visualizo el texto, " + texto)
        
        return texto

    def text_subtitulo(self):
        driver = self.driver
        try:
            
            texto = driver.find_element(By.ID, "com.mercadolibre:id/home_onboarding_step_subtitle").text
            
        except NoSuchElementException:
            
            print (u"Verificar: Elemento no pesente")
            return False
        
        print (u"Verificar: Se visualizo el texto, " + texto)
        
        return texto   
        
        
    def test_001(self):
        driver = self.driver
        self.Esperar_Inicio()
        
        self.assertEqual("Libera tus ideas", self.text_titulo())
        self.assertEqual("Estás en el lugar perfecto para encontrar lo que buscas.", self.text_subtitulo())
        
        self.capturarPantalla(driver)
        
    def test_002(self):
        driver = self.driver
        self.Esperar_Inicio()
        self.swipe()
        
        self.assertEqual("Te cuidamos, siempre", self.text_titulo())
        self.assertEqual("Con Mercado Pago, protegemos tu dinero hasta que estés feliz con tu compra. ¡Y tienes hasta 12 cuotas sin interés!", self.text_subtitulo())
        
        self.capturarPantalla(driver)

    def test_003(self):
        driver = self.driver
        self.Esperar_Inicio()
        self.swipe()
        self.swipe()
        
        self.assertEqual("Llegamos a donde estás", self.text_titulo())
        self.assertEqual("A la puerta de tu casa o al otro lado del país, con Mercado Envíos llevamos tu compra a donde nos digas.", self.text_subtitulo())
        
        self.capturarPantalla(driver)


        

    def tearDown(self):
        self.driver.quit()
          
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MeliAppium)
    unittest.TextTestRunner(verbosity=2).run(suite)