# -*- coding: utf-8 -*-
     
import unittest, time, pytest
from appium import webdriver
from src.functions.Functions import Functions as Selenium
from src.functions.Inicializar import Inicializar
from src.pages.Menu_MercadoLibre_Mobile import Menu_Meli
from src.pages.Login_MercadoLibre_Mobile import Login_Meli

class Meli_app(unittest.TestCase, Selenium, Inicializar):

    def setUp(self):

        desired_caps = self.inicializar_mobile_capabilities()
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

    def test_007(self):

        print (u"Seleccionar Pais")

        self.esperar_xpath(Login_Meli.lbl_titulo_pais_xpath)
        self.xpath_elements_tap(Login_Meli.chk_Argentina_xpath)
        self.captura("Esto es Captura para Allure")
        
        print (u"Ingresar Usuario")
        self.esperar_id(Login_Meli.lbl_titulo_id)
        self.captura("Esto es Captura para Allure")
        
        print (u"Seleccionar tipo de Autenticación")
        self.esperar_id(Login_Meli.btn_already_id)
        self.id_elements_tap(Login_Meli.btn_already_id)

        print (u"Ingresar Usuario")
        self.esperar_id(Login_Meli.lbl_titulo_login_id)
        self.sendkeys_id(Login_Meli.txt_usuario_id, "edgar17200@hotmail.com")
        self.captura("Estos es una bonitas capturas")
        self.id_elements_click (Login_Meli.btn_continuar_id)

        print (u"Ingreso de clave")
        self.esperar_id(Login_Meli.btn_ingresar_id)
        self.sendkeys_id(Login_Meli.txt_clave_id, "edgarmejias26")
        self.captura("Estos es una bonitas capturas para clientes")
        self.id_elements_click(Login_Meli.btn_ingresar_id)
        
        print (u"Validar el usuario logueado")
        self.waitStopLoad(3)
        self.captura("Estos es una bonitas capturas")
        self.id_elements_tap( Menu_Meli.btn_menu_accid)
        self.waitStopLoad(3)
        self.assertTrue(True, Selenium.esperar_id(self, Menu_Meli.lbl_UsuarioLogueado_id))
        self.assertEqual("¡Hola edgar!", self.get_to_text_element_id(Menu_Meli.lbl_UsuarioLogueado_id))
        self.captura("Estos es una bonitas capturas")
        self.driver.close_app()
        
        print('DONE!!')

  
def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()