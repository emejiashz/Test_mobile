# -*- coding: utf-8 -*-
import unittest
from Functions.seleniumFunctions import seleniumFunctions as Selenium
from Functions.Inicializar import  Inicializar
from Pages.Menu_MercadoLibre import Menu_Meli
from Pages.Login_MercadoLibre import Login_Meli



class MeliAppium(unittest.TestCase):
    
    
    def setUp(self):
        self.driver = Inicializar.IniciarApp(self, 'http://127.0.0.1:4725', 'android', '5.0.1', 'GT-I9500', '4d00261bbbe450a3', True)
    
    def test_007(self):
        driver = self.driver
        
        #Menu-->Ingresar
        Selenium.Esperar_xpath(self, driver, Menu_Meli.btn_Menu_xpath)
        Selenium.AccID_elements_click(self, driver, Menu_Meli.btn_menu_accid)
        Inicializar.capturarPantalla(self, driver)
        Selenium.ID_elements_click(self, driver, Menu_Meli.lbl_ingresar_id)
        
        #Seleccionar tipo de Login
        Selenium.Esperar_ID(self, driver, Login_Meli.btn_already_id)
        self.assertEqual("¿Aún no tienes cuenta?", Selenium.Get_to_text_Element_ID(self, driver, Login_Meli.lbl_Registro_Titulo))
        
        self.assertEqual(True, Selenium.Esperar_ID(self, driver, Login_Meli.btn_facebook_id))
        self.assertEqual(True, Selenium.Esperar_ID(self, driver, Login_Meli.btn_email_id))
        
        Selenium.ID_elements_click(self, driver, Login_Meli.btn_already_id)
        
        #Ingreso de Usuario
        Selenium.Esperar_ID(self, driver, Login_Meli.lbl_avisoTitulo_id)
        self.assertTrue(True, Login_Meli.lbl_avisoTitulo_id)
        Selenium.ID_elements_click(self, driver, Login_Meli.txt_usuario_id)
        Selenium.sendkeys_id(self, driver, Login_Meli.txt_usuario_id, "devbaires")
        Inicializar.capturarPantalla(self, driver)
        Selenium.ID_elements_click(self, driver, Login_Meli.btn_continuar_id)
        
        #Ingreso de clave
        Selenium.Esperar_ID(self, driver, Login_Meli.btn_ingresar_id)
        Selenium.sendkeys_id(self, driver, Login_Meli.txt_Clave_id, "298258233")
        Selenium.AccID_elements_click(self, driver, Login_Meli.btn_verClave_Accid)
        Selenium.ID_elements_click(self, driver, Login_Meli.btn_ingresar_id)
        
        #Validar el usuario logueado
        Selenium.AccID_elements_click(self, driver, Login_Meli.btn_menu_accid)
        self.assertEqual("¡Hola Mervin!", Selenium.Get_to_text_Element_ID(self, driver, Login_Meli.lbl_UsuarioLogueado_id))
        Inicializar.capturarPantalla(self, driver)
        
        

    def tearDown(self):
        self.driver.quit()
          
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MeliAppium)
    unittest.TextTestRunner(verbosity=2).run(suite)