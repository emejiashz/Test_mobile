# -*- coding: utf-8 -*-
     
import unittest, time
from appium import webdriver
from src.functions.Functions import Functions as Selenium,\
    Functions
from src.functions.Iniciar_app import Iniciar_app,MLActivity,MLApk,MLappPackage
from src.pages.mobile.Menu_MercadoLibre_Mobile import Menu_Meli
from src.pages.mobile.Login_MercadoLibre_Mobile import Login_Meli

class Meli_app(unittest.TestCase):
    
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'android'
        desired_caps['platformVersion'] = '8.1.0'
        desired_caps['deviceName'] = 'ZY322MBC9D'
        desired_caps['app'] = 'C:\\AppiumFramework\\APK\\mercadolibre-9-15-8.apk'
        desired_caps['NoReset'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        
    def test_007(self):
        driver = self.driver
        
        # Ingresar Usuario
        Selenium.Esperar_ID(self, driver, Login_Meli.lbl_titulo_id)
        Functions.capturar_Pantalla2(self)
        
        # Seleccionar tipo de Autenticación
        Selenium.Esperar_ID(self, driver, Login_Meli.btn_already_id)
        driver.find_element_by_id(Login_Meli.btn_already_id).click()
        # Ingresar Usuario
        Selenium.ID_elements_click(self, driver, Login_Meli.txt_usuario_id)
        Selenium.sendkeys_id(self, driver, Login_Meli.txt_usuario_id, "edgar17200@hotmail.com")
        Functions.capturar_Pantalla2(self)
        Selenium.ID_elements_click(self, driver, Login_Meli.btn_continuar_id)

        # Ingreso de clave
        Selenium.Esperar_ID(self, driver, Login_Meli.btn_ingresar_id)
        Selenium.sendkeys_id(self, driver, Login_Meli.txt_clave_id, "edgarmejias26")
        Functions.capturar_Pantalla2(self)
        Selenium.ID_elements_click(self, driver, Login_Meli.btn_ingresar_id)
        
        # Validar el usuario logueado
        time.sleep(5)
        Selenium.AccID_elements_click(self, driver, Menu_Meli.btn_menu_accid)
        time.sleep(5)
        self.assertTrue(True, Selenium.Esperar_ID(self, driver, Menu_Meli.lbl_UsuarioLogueado_id))
        self.assertEqual("¡Hola edgar!", Selenium.Get_to_text_Element_ID(self, driver, Menu_Meli.lbl_UsuarioLogueado_id))
        Functions.capturar_Pantalla2(self)
        driver.close_app()
        
        print('DONE!!')
        
        driver.close_app()
  
def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()