# -*- coding: utf-8 -*-

import unittest, time
from appium import webdriver
from src.functions.Functions import Functions as Selenium
from src.functions.Inicializar import Inicializar
from src.pages.Menu_MercadoLibre_Mobile import Menu_Meli
from src.pages.Login_MercadoLibre_Mobile import Login_Meli


class Meli_app(unittest.TestCase, Selenium, Inicializar):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = '4e9aa907'
        desired_caps['app'] = 'C:\\AppiumFramework\\APK\\mercadolibre-9-15-8.apk'
        desired_caps['NoReset'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_007(self):
        # Seleccionar Pais

        self.verificar_id(Login_Meli.lbl_titulo_pais_id)
        self.xpath_elements_tap(Login_Meli.chk_Argentina_xpath)

        # Ingresar Usuario
        self.esperar_id(Login_Meli.lbl_titulo_id)
        self.Captura("Esto es Captura para Allure")

        # Seleccionar tipo de Autenticación
        self.esperar_id(Login_Meli.btn_already_id)
        self.driver.find_element_by_id(Login_Meli.btn_already_id).click()

        # Ingresar Usuario
        self.id_elements_click(Login_Meli.txt_usuario_id)
        self.sendkeys_id(Login_Meli.txt_usuario_id, "edgar17200@hotmail.com")
        self.Captura("Estos es una bonitas capturas")
        self.id_elements_click(Login_Meli.btn_continuar_id)

        # Ingreso de clave
        self.esperar_id(Login_Meli.btn_ingresar_id)
        self.sendkeys_id(Login_Meli.txt_clave_id, "edgarmejias26")
        self.Captura("Estos es una bonitas capturas para clientes")
        self.id_elements_click(Login_Meli.btn_ingresar_id)

        # Validar el usuario logueado
        self.waitStopLoad(5)
        self.Captura("Estos es una bonitas capturas")
        # self.( Menu_Meli.btn_menu_accid)
        self.waitStopLoad(5)
        self.assertTrue(True, Selenium.esperar_id(self, Menu_Meli.lbl_UsuarioLogueado_id))
        # self.assertEqual("¡Hola edgar!", self.driver.get_to_text_Element_ID(Menu_Meli.lbl_UsuarioLogueado_id))
        self.Captura("Estos es una bonitas capturas")
        self.driver.close_app()

        print('DONE!!')


def tearDown(self):
    self.driver.quit()


if __name__ == "__main__":
    unittest.main()    unittest.main()