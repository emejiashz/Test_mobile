# -*- coding: utf-8 -*-
import unittest
from Functions.seleniumFunctions import seleniumFunctions as Selenium
from Functions.Inicializar import  Inicializar
from Pages.Inicio_Meli import Inicio_Meli



class MeliAppium(unittest.TestCase):
    
    
    def setUp(self):
        self.driver = Inicializar.IniciarApp(self, 'http://127.0.0.1:4725', 'android', '5.0.1', 'GT-I9500', '4d00261bbbe450a3', True)
    
    def test_007(self):
        driver = self.driver
        Inicializar.capturarPantalla(self, driver)
        
        #Swipe Inicio
        Selenium.swipe_screen(self, driver, '934', '566', '-712','-6')
        Inicializar.capturarPantalla(self, driver)
        
        Selenium.swipe_screen(self, driver, '934', '566', '-712','-6')
        Inicializar.capturarPantalla(self, driver)
        
        Selenium.swipe_screen(self, driver, '934', '566', '-712','-6')
        Inicializar.capturarPantalla(self, driver)
        
        Selenium.swipe_screen(self, driver, '934', '566', '-712','-6')
        Inicializar.capturarPantalla(self, driver)
        
        Selenium.ID_elements_click(self, driver, Inicio_Meli.img_Slide_id)
        
        #Seleccionar tipo de Login
        Selenium.Esperar_xpath(self, driver, Inicio_Meli.img_vinos_xpath)
        self.assertTrue(Selenium.Esperar_xpath(self, driver, Inicio_Meli.img_vinos_xpath))


    def tearDown(self):
        self.driver.quit()
          
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MeliAppium)
    unittest.TextTestRunner(verbosity=2).run(suite)