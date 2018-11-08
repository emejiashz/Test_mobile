# -*- coding: utf-8 -*-
     
import unittest, time
from Functions.seleniumFunctions import seleniumFunctions as Selenium,\
    seleniumFunctions
from Functions.Iniciar import Iniciar_app, MLActivity, MLApk,MLappPackage
from Pages.Menu_MercadoLibre_Mobile import Menu_Meli
from Pages.Login_MercadoLibre_Mobile import Login_Meli

class tMeliAppium(unittest.TestCase):

    def setUp(self):
        
        self.driver = Iniciar_app.cap_MOTOG5(self, MLApk, MLappPackage, MLActivity, 'http://127.0.0.1:4723')
        
    def test_007(self):
        driver = self.driver
        
        # Ingresar Usuario
        Selenium.Esperar_ID(self, driver, Login_Meli.lbl_titulo_id)
        seleniumFunctions.capturar_Pantalla(self)
        
        # Seleccionar tipo de Autenticación
        Selenium.Esperar_ID(self, driver, Login_Meli.btn_already_id)
        driver.find_element_by_id(Login_Meli.btn_already_id).click()
        # Ingresar Usuario
        Selenium.ID_elements_click(self, driver, Login_Meli.txt_usuario_id)
        Selenium.sendkeys_id(self, driver, Login_Meli.txt_usuario_id, "edgar17200@hotmail.com")
        seleniumFunctions.capturar_Pantalla(self)
        Selenium.ID_elements_click(self, driver, Login_Meli.btn_continuar_id)

        # Ingreso de clave
        Selenium.Esperar_ID(self, driver, Login_Meli.btn_ingresar_id)
        Selenium.sendkeys_id(self, driver, Login_Meli.txt_clave_id, "edgarmejias26")
        seleniumFunctions.capturar_Pantalla(self)
        Selenium.ID_elements_click(self, driver, Login_Meli.btn_ingresar_id)
        
        # Validar el usuario logueado
        time.sleep(5)
        Selenium.AccID_elements_click(self, driver, Menu_Meli.btn_menu_accid)
        time.sleep(5)
        self.assertTrue(True, Selenium.Esperar_ID(self, driver, Menu_Meli.lbl_UsuarioLogueado_id))
        self.assertEqual("¡Hola edgar!", Selenium.Get_to_text_Element_ID(self, driver, Menu_Meli.lbl_UsuarioLogueado_id))
        seleniumFunctions.capturar_Pantalla(self)
        driver.close_app()
        
        print('DONE!!')
        
        driver.close_app()
  
def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()