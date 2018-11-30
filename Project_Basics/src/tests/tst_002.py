# -*- coding: utf-8 -*-
import unittest
from src.pages.Trivago import Inicio
from src.functions.Functions import Functions as Selenium
from selenium.webdriver.common.keys import Keys
import allure
import pytest


@allure.feature(u'Busqueda Trivago')
@allure.story(u'002: verify query results for Bahia Blanca in Trivago')
@allure.testcase(u"Caso de Prueba 00001", u'http://my.tms.org/browse/TESTCASE-39')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""The PO gives us the following specification:</br>
We want to look for “RAET” word in google main page and check if amount of results is bigger than 100000  </br>

1- Access to https://www.trivago.com.ar/. </br>
2- Set Bahia Blanca in the Trivago textbox. </br>
3- Verify query results</br>
 </br></br>""")

class tst_002(unittest.TestCase, Selenium):

 
    def setUp(self):
        #ABRIR LA APP
        with allure.step(u'PASO 1: Ingresar a Trivago'):
            self.driver = self.abrir_Navegador("https://www.trivago.com.ar/")
        
        #DATOS DESDE EXCEL
        self.user = self.LeerCelda("D2")
        self.passWord = self.LeerCelda("E2")

    def test_02(self):
        #ESPERAR EL INICIO DE LA APP
        with allure.step(u'PASO 2: Ingresar Bahia Blanca como termino de Busqueda'):
            Validar = self.esperar_Xpath(Inicio.txt_busqueda_xpath)
            if Validar == False:
                self.CapturarPantalla(u"No se inicializo Trivago")
                pytest.skip("No se inicializo Trivago")
            
            self.Xpath_Elements(Inicio.txt_busqueda_xpath).click()
            self.Xpath_Elements(Inicio.txt_busqueda_xpath).send_keys(u"Bahia Blanca")
            self.CapturarPantalla(u"Ingresar Bahia Blanca como termino de Busqueda")

            self.Xpath_Elements(Inicio.txt_busqueda_xpath).send_keys(Keys.ENTER)
            self.esperar_Xpath(Inicio.lbl_resultados_xpath)
            self.CapturarPantalla("Resultados")

            resultados = self.driver.find_elements_by_xpath(Inicio.lbl_resultados_xpath)

            for resultado in resultados:
                print (resultado)
                r = resultado.text
                self.driver.execute_script("arguments[0].scrollIntoView();", resultado)
                self.CapturarPantalla(r)




            
    def tearDown(self):
        with allure.step(u'PASO 3: Salir de la aplicación.'):
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()