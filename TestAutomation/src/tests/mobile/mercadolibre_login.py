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

        # Ingresar a Mercado Libre
        Selenium.Esperar_ID(Login_Meli.lbl_titulo_id)
        Selenium.AccID_elements_click(self, driver, Menu_Meli.btn_menu_accid)
        seleniumFunctions.capturarPantalla(self, driver)
        Selenium.ID_elements_click(self, driver, Menu_Meli.lnk_IngresarMercadoLibre_id)

        # Seleccionar tipo de Autenticación
        Selenium.Esperar_ID(self, driver, Login_Meli.btn_already_id)

        Selenium.ID_elements_click(self, driver, Login_Meli.btn_already_id)

        # Ingresar Usuario
        Selenium.Esperar_ID(self, driver, Login_Meli.txt_usuario_id)
        Selenium.ID_elements_click(self, driver, Login_Meli.txt_usuario_id)
        Selenium.sendkeys_id(self, driver, Login_Meli.txt_usuario_id, "CDAARGENTINA")
        seleniumFunctions.capturarPantalla(self, driver)
        Selenium.ID_elements_click(self, driver, Login_Meli.btn_continuar_id)

        # Ingreso de clave
        Selenium.Esperar_ID(self, driver, Login_Meli.btn_ingresar_id)
        Selenium.sendkeys_id(self, driver, Login_Meli.txt_clave_id, "298258233")
        Selenium.ID_elements_click(self, driver, Login_Meli.btn_verClave_id)
        Selenium.ID_elements_click(self, driver, Login_Meli.btn_ingresar_id)
        
        #captcha
        time.sleep(5)
        Selenium.ID_elements_click(self, driver, Login_Meli.chk_Captcha_id)
        time.sleep(5)
        Selenium.Xpath_elements_click(self, driver, Login_Meli.btn_ingresarCaptcha_xpath)

        # Validar el usuario logueado
        time.sleep(5)
        Selenium.AccID_elements_click(self, driver, Menu_Meli.btn_menu_accid)
        time.sleep(5)
        self.assertTrue(True, Selenium.Esperar_ID(self, driver, Menu_Meli.lbl_UsuarioLogueado_id))
        Selenium.ID_elements_click(self, driver, Menu_Meli.lnk_MiCuenta_id)
        Selenium.swipe_screen(self, driver, "751", "1536", "-15", "-660")
        Selenium.ID_elements_click(self, driver, Menu_Meli.lnk_Salir_id)
        Selenium.ID_elements_click(self, driver, Menu_Meli.btn_Confirmar_id)
        Selenium.AccID_elements_click(self, driver, Menu_Meli.btn_menu_accid)
        self.assertEqual("¡Bienvenido!", Selenium.Get_to_text_Element_ID(self, driver, Menu_Meli.lbl_UsuarioLogueado_id))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(tMeliAppium)
    unittest.TextTestRunner(verbosity=2).run(suite)