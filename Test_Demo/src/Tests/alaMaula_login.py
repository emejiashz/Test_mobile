import unittest
from Functions.seleniumFunctions import seleniumFunctions as Selenium
from Functions.Inicializar import Inicializar
from Pages.Menu_alaMaula_Mobile import Menu_alaMaula
from Pages.Login_alaMaula_Mobile import Login_alaMaula
from Pages.Config_alaMaula_Mobile import Config_alaMaula
from src.Functions.seleniumFunctions import seleniumFunctions

class alaMaula(unittest.TestCase):

    def setUp(self):
        self.driver = Inicializar.IniciarApp(self, 'http://127.0.0.1:4723', 'android', '6.0.0', 'YT911BA6UJ', 
                                             'com.ebay.alamaula', 
                                             'com.ebay.app.common.activities.SplashScreenActivity', 
                                             True)
    def test_001(self, Selenium):
        driver = self.driver

        #Ingresar alaMaula
        self.Esperar_ID(self, driver, Menu_alaMaula.btn_Menu_id)
        
        seleniumFunctions.capturarPantalla(self, driver)
        
        Selenium.ID_elements_tap(self, driver, Menu_alaMaula.btn_Menu_id)
        Selenium.ID_elements_tap(self, driver, Menu_alaMaula.btn_MenuIniciarSesion_id)
        Selenium.Esperar_ID(self, driver, Login_alaMaula.txt_usuario_id)
        Selenium.sendkeys_id(self, driver, Login_alaMaula.txt_usuario_id, "mediaz@cdainfo.com")
        Selenium.sendkeys_id(self, driver, Login_alaMaula.txt_clave_id, "298258233")
        
        seleniumFunctions.capturarPantalla(self, driver)
        
        Selenium.ID_elements_tap(self, driver, Login_alaMaula.btn_IniciarSesion_id)
        
        Selenium.Esperar_ID(self, driver, Menu_alaMaula.btn_Menu_id)
        Selenium.ID_elements_tap(self, driver, Menu_alaMaula.btn_Menu_id)
        
        self.assertTrue("CDA Soluciones", Selenium.Get_to_text_Element_ID(self, driver, Menu_alaMaula.lnk_UserProfileName_id))
        
        self.assertTrue("mediaz@cdainfo.com", Selenium.Get_to_text_Element_ID(self, driver, Menu_alaMaula.lnk_UserProfileEmail_id))
        
        seleniumFunctions.capturarPantalla(self, driver)

    def test_002(self):
        driver = self.driver
        Selenium.Esperar_ID(self, driver, Menu_alaMaula.btn_Menu_id)
        Selenium.ID_elements_tap(self, driver, Menu_alaMaula.btn_Menu_id)
        
        seleniumFunctions.capturarPantalla(self, driver)
        
        Selenium.swipe_screen(self, driver, "751", "1536", "-15", "-660")
        Selenium.Xpath_elements_tap(self, driver, Menu_alaMaula.lnk_configuracion_xpath)
        
        seleniumFunctions.capturarPantalla(self, driver)
        
        Selenium.Esperar_ID(self, driver, Config_alaMaula.lnk_CerrarSesion_id)
        Selenium.ID_elements_tap(self, driver, Config_alaMaula.lnk_CerrarSesion_id)

    def tearDown(self):
        seleniumFunctions.capturarPantalla(self, self.driver)
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(alaMaula)
    unittest.TextTestRunner(verbosity=2).run(suite)