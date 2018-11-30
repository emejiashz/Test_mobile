# -*- coding: utf-8 -*-

import unittest,time
from Functions.seleniumFunctions import seleniumFunctions as Selenium,\
    seleniumFunctions
from Functions.Iniciar import Iniciar_app, MLActivity, MLApk, MLappPackage
from Pages.Menu_MercadoLibre_Mobile import Menu_Meli
from Pages.Login_MercadoLibre_Mobile import Login_Meli

class tst_a(unittest.TestCase):

    def setUp(self):
        
        self.driver = Iniciar_app.cap_MOTOG5(self, MLApk, MLappPackage, MLActivity, 'http://127.0.0.1:4723')
        
    def test_007(self):
        
        print('DONE!')
        
        time.sleep(10)
        self.driver.close_app()
  
def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()