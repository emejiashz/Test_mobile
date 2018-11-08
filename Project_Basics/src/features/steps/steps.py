# -*- coding: utf-8 -*-
from typing import Union

from behave import *
import unittest

from behave import model

from src.functions.Functions import Functions as Selenium
from src.pages.Google import Inicio
from selenium.webdriver.common.keys import Keys
import pytest


class StepsDefinitions():
 #   driver: Union[WebDriver, WebDriver]
    use_step_matcher("re")


    @given('User open Google main site')
    def step_impl(self):
        self.url = u"https://www.google.com"
        self.driver =  Selenium.abrir_Navegador(self, u"https://www.google.com")

    @step('Type (.*) in google search box')
    def step_impl(self, RAET):
        Validar = Selenium.esperar_Xpath(self, Inicio.txt_busqueda_xpath)
        if Validar == False:
            Selenium.CapturarPantalla(self, u"No se inicializo google.com")
            pytest.skip("No se inicializo google.com")
            self.driver.quit()


        Selenium.Xpath_Elements(self,Inicio.txt_busqueda_xpath).click()
        Selenium.Xpath_Elements(self,Inicio.txt_busqueda_xpath).send_keys(RAET)
        Selenium.Xpath_Elements(self,Inicio.txt_busqueda_xpath).send_keys(Keys.ENTER)
        Selenium.esperar_Xpath(self,Inicio.txt_resultStats_xpath)

    @Then('Query results are under (.*)')
    def step_impl(self, QResult):
        Selenium.Captura(self, u'Then Query results are under 1000', self.driver)
        Resultados = Selenium.Xpath_Elements(self, Inicio.txt_resultStats_xpath).text
        print(Resultados)
        RAET = Resultados.split(" ")[2]
        print("RAET obtuvo: " + str(RAET) + " Resultados de busqueda")
        Resultado = RAET.replace(",", "")
        unittest.TestCase.assertTrue(int(Resultado) > int(QResult), "Es mayor a 10000")


    @given('User open site (.*)')
    def step_impl(self, URL):
        self.driver =  Selenium.abrir_Navegador(self, URL)

    @then('Type {keywords} in google search box')
    def step_impl(self, text):
        Selenium.Xpath_Elements(self, Inicio.txt_busqueda_xpath).click()
        Selenium.Xpath_Elements(self, Inicio.txt_busqueda_xpath).send_keys(text)
        Selenium.Xpath_Elements(self, Inicio.txt_busqueda_xpath).send_keys(Keys.ENTER)
        Selenium.esperar_Xpath(self, Inicio.txt_resultStats_xpath)