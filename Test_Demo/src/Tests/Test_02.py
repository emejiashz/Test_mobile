import unittest
import time
from Functions.Inicializar import Inicializar
from Pages.Popup_Mercari import popup

dia = time.strftime("%Y-%m-%d")  # formato aaaa/mm/dd
hora = time.strftime("%H%M%S")  # formato 24 houras

class ContactAppTestAppium(unittest.TestCase):

    def setUp(self):
        self.driver = Inicializar.IniciarApp(self, 'http://127.0.0.1:4723', 'android', '5.0.1', 'GT-I9500', True)
        time.sleep(5)
    
    def test_ClickPopUpLink(self):
        popUpBtn  = self.driver.find_element_by_id("com.mercariapp.mercari:id/com_appboy_inappmessage_modal_close_button")
        self.assertTrue(popUpBtn.is_displayed())
        popUpBtn.click()
        
        


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactAppTestAppium)
    unittest.TextTestRunner(verbosity=2).run(suite)


