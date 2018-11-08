# -*- coding: utf-8 -*-

import time, os, shutil, io, allure, openpyxl
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OpcionesChrome
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from src.functions.Inicializar import Inicializar
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
import pytest


diaGlobal= time.strftime("%Y-%m-%d")  # formato aaaa/mm/dd
horaGlobal = time.strftime("%H%M%S")  # formato 24 houras

class Functions():

    def Xpath_Elements(self, XPATH):
        elements = self.driver.find_element_by_xpath(XPATH)
        print ("Xpath_Elements: Se interactuo con el elemento " + XPATH)
        return elements
        
    def ID_Elements(self, ID):
        elements = self.driver.find_element_by_id(ID)
        print ("Xpath_Elements: Se interactuo con el elemento " + ID)
        return elements
    
    def select_elements_xpath(self, xpath):
        select = Select(self.driver.find_element_by_xpath(xpath))
        return select
    
        #USO

#       select by visible text
#       select.select_by_visible_text('Banana')
        
#       select by value 
#       select.select_by_value('1')

    def esperar_Xpath(self, XPATH): #Esperar que un elemento sea visible 
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located((By.XPATH, XPATH)))
            print (u"esperar_Xpath: Se mostrÃ³ el elemento " + XPATH)
            return True

        except TimeoutException:
            print (u"esperar_Xpath: No presente " + XPATH)
            return False
        
        
    
    def esperar_CSS(self, CSS):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, CSS)))

        except TimeoutException:
            print (u"esperar_CSS: No presente " + CSS)
            return False
        
        print (u"esperar_CSS: Se mostrÃ³ el elemento " + CSS)
        return True
    
    ##########################################################################
    ##############       -=_JS     CLICKS _=-              ###################
    ##########################################################################
         
         
    def JS_Click_Xpath(self, xpath):
        try:
            localizador = self.driver.find_element_by_xpath(xpath)
            self.driver.execute_script("arguments[0].click();", localizador)
            print ("JS_Click_Xpath: Se hizo click en: " +  xpath)
            return True
        
        except NoSuchElementException:
            print ("JS_Click_Xpath: No se encontro " +  xpath)
            return False
            
    def JS_Click_CSS(self, css):
        localizador = self.driver.find_element_by_css_selector(css)
        self.driver.execute_script("arguments[0].click();", localizador)
        
    ##########################################################################
    ##############   -=_JS     IR     A _=-                ###################
    ##########################################################################
    def ir_a_xpath(self, elemento):
        try:
            localizador = self.driver.find_element(By.XPATH, elemento)  
            self.driver.execute_script("arguments[0].scrollIntoView();", localizador)
            
        except TimeoutException:
            
            print (u"ir_a_xpath: No presente " + elemento)
            return False
        
        print (u"ir_a_xpath: Se desplazÃ³ al elemento, " + elemento)
        return True
    
    ##########################################################################
    ##############    -=_ACTION CHAINS _=-                ###################
    ##########################################################################
    def mouse_over_xpath(self, xpath):
        element = self.driver.find_element_by_xpath(xpath)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        
    def mouse_over_css(self, css):
        element = self.driver.find_element_by_css_selector(css)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform() 
        
    ##########################################################################
    ##############    -=_VERIFICACION _=-                ###################
    ##########################################################################
    def verificar_xpath(self, xpath): #devuelve true o false
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            print (u"Verificar: Elemento No presente " + xpath)
            return False
        print (u"Verificar: Se visualizo el elemento, "+ xpath)
        return True      
    
    
    def verificar_CSS(self, CSS): #devuelve true o false
        try:
            self.driver.find_element_by_css_selector(CSS)
        except NoSuchElementException:
            print (u"Verificar: Elemento No presente " + CSS)
            return False
        print (u"Verificar: Se visualizo el elemento, "+ CSS)
        return True
    
    def verificarTexto_xpath(self, xpath, TEXTO): #devuelve true o false
        try:
            wait = WebDriverWait(self.driver, 15)
            wait.until(EC.text_to_be_present_in_element((By.XPATH, xpath), TEXTO))
        except TimeoutException:
            print (u"Verificar Texto: Texto No presente " + xpath + " el texto, " + TEXTO)
            return False
        print (u"Verificar Texto: Se visualizÃ³ en, " + xpath + " el texto, " + TEXTO)
        return True
    
    ##############   -=_CAPTURA DE PANTALLA_=-   #############################
    ##########################################################################
    def crear_path(self):
        def hora_Actual():
            hora = time.strftime("%H%M%S")  # formato 24 horas
            return hora

        dia = time.strftime("%d-%m-%Y")  # formato aaaa/mm/dd

        GeneralPath = Inicializar.Path_Evidencias
        DriverTest = Inicializar.NAVEGADOR
        TestCase = self.__class__.__name__
        horaAct = horaGlobal

        path = GeneralPath + dia + "/" + TestCase + "/" + DriverTest + "/" + horaAct + "/"

        if not os.path.exists(path):  # si no existe el directorio lo crea

            os.makedirs(path)

        return path

    def capturar_Pantalla(self):
        def hora_Actual():
            hora = time.strftime("%H%M%S")  # formato 24 horas
            return hora
        
        dia = time.strftime("%d-%m-%Y")  # formato aaaa/mm/dd
        
        GeneralPath = Inicializar.Path_Evidencias
        DriverTest = Inicializar.NAVEGADOR
        TestCase = self.__class__.__name__
        horaAct = horaGlobal
        
        path = GeneralPath + dia + "\\" + TestCase + "\\" + DriverTest + "\\" +  horaAct + "\\"
 
        if not os.path.exists(path): # si no existe el directorio lo crea
 
            os.makedirs(path)
 
        img = path + TestCase + "_(" + str(hora_Actual()) + ")" + ".png"

        self.driver.get_screenshot_as_file(img)
        
        print(img)
         
        return img  
    
    def CapturarPantalla(self, Descripcion):
        path = Functions.crear_path(self)
        TestCase = self.__class__.__name__
        def hora_Actual():
            hora = time.strftime("%H%M%S")  # formato 24 horas
            return hora
        img = path + TestCase + "_(" + str(hora_Actual()) + ")" + ".png"
        self.driver.get_screenshot_as_file(img)
        print(img)
        CAPTURA = Image.open(img, mode="r")
        ImageProcess = io.BytesIO()
        CAPTURA.save(ImageProcess, format= "PNG")
        ImageProcess = ImageProcess.getvalue()
        allure.attach(ImageProcess, Descripcion, attachment_type=allure.attachment_type.PNG)

    def Captura(self, Descripcion, driver):
        path = Functions.crear_path(self)
        TestCase = self.__class__.__name__
        def hora_Actual():
            hora = time.strftime("%H%M%S")  # formato 24 horas
            return hora
        img = path + TestCase + "_(" + str(hora_Actual()) + ")" + ".png"
        print(img)
        self.driver.get_screenshot_as_file(img)
        CAPTURA = Image.open(img, mode="r")
        ImageProcess = io.BytesIO()
        CAPTURA.save(ImageProcess, format= "PNG")
        ImageProcess = ImageProcess.getvalue()
        allure.attach(ImageProcess, Descripcion, attachment_type=allure.attachment_type.PNG)
    
    def waitStopLoad(self, timeLoad=8):
        print ("waitStopLoad: Inicia")
        try:
                totalWait = 0
                while (totalWait < timeLoad):
                    print("Cargando ... intento: " + str(totalWait))
                    time.sleep(1)
                    totalWait = totalWait + 1
        except: 
            print ("waitStopLoad: Carga Finalizada ... ")
            
    def Modificar_XML_Enviroments(self):

        print ("--------------------------------------")
        print ("Estableciendo Datos del Reporte...")
        JOB_NAME = 'VARIABLE DE JENKINS JOB_NAME'
        #os.environ['JOB_NAME']
        NODE_NAME = 'VARIABLE DE JENKINS NODE_NAME' 
        #os.environ['NODE_NAME']
        NAVEGADOR = Inicializar.NAVEGADOR
        print (NODE_NAME)
        print (JOB_NAME)
        print (NAVEGADOR)
        print ("--------------------------------------")

        Enviroment = open('../data/environment.xml', 'w')
        Template = open('../data/environment_Template.xml', 'r')
        
        with Template as f:
            texto = f.read()
            
            texto = texto.replace("JOB_NAME", JOB_NAME)
            texto = texto.replace("NODE_NAME", NODE_NAME)
            texto = texto.replace("NAVEGADOR", NAVEGADOR)
        
        with Enviroment as f:
            f.write(texto)
             
        Enviroment.close()    
        Template.close()

        time.sleep(5) 
        
        if os.path.exists("../allure-results"): # si no existe el directorio lo crea

            shutil.rmtree("../allure-results")

        try:
            os.makedirs("../allure-results")
        except OSError:
            print ("No se pudo generar la carpeta ../allure-results")
        
        shutil.copy("../data/environment.xml","../allure-results")           

#Excel 
    def LeerCelda(self, celda):
        wb = openpyxl.load_workbook(Inicializar.Excel)
        sheet = wb["DataTest"]
        valor= str(sheet[celda].value)
        print (u"------------------------------------")
        print (u"El libro de excel utilizado es de es: " + Inicializar.Excel)
        print (u"El valor de la celda es: " + valor)
        print (u"------------------------------------")
        return valor
    
    def EscribirCelda(self, celda, valor):
        wb = openpyxl.load_workbook(Inicializar.Excel)
        hoja = wb["DataTest"]
        hoja[celda]= valor
        wb.save(Inicializar.Excel)
        print (u"------------------------------------")
        print (u"El libro de excel utilizado es de es: " + Inicializar.Excel)
        print (u"Se escribio en la celda " + str(celda) + u" el valor: " + str (valor))
        print (u"------------------------------------")
        
    ##########################################################################
    ##############   -=_ASSERTION_=-   #############################
    ##########################################################################       
    def Assert_xpath(self, xpath):
        try:
            
            wait = WebDriverWait(self.driver, 2)
            wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            
        except TimeoutException:
            print (u"Assert_xpath: Elemento No presente " + xpath)
            self.assertTrue(False)
            
        print (u"Assert_xpath: Se visualizo el elemento, "+ xpath)
        self.assertTrue(True)      
        
        
    ##########################################################################
    ##############   -=_INICIALIZAR DRIVERS_=-   #############################
    ##########################################################################
##Check
    def abrir_Navegador(self, URL):
        navegador = Inicializar.NAVEGADOR
        print ("----------------")
        print (navegador)
        print ("---------------")
        
        if navegador == ("CHROME"):
            
            options = OpcionesChrome()
            options.add_argument('start-maximized')
            self.driver = webdriver.Chrome(chrome_options=options)
            self.driver.implicitly_wait(10)
            self.dir_navegador = "CHROME"
            self.driver.get(URL)
            return self.driver
        
        if navegador == ("CHROME_headless"):
            
            options = OpcionesChrome()
            options.add_argument('headless')
            options.add_argument('--start-maximized')
            options.add_argument('--lang=es')
            self.driver = webdriver.Chrome(chrome_options=options)
            self.driver.implicitly_wait(10)
            self.dir_navegador = "CHROME Headless"
            self.driver.get(URL)
            return self.driver
        
        if navegador == ("FIREFOX"):
            self.driver = webdriver.Firefox()
            self.dir_navegador = "FIREFOX"
            self.driver.get(URL)
            return self.driver 
        
        elif navegador != ("CHROME_headless") and  navegador != ("CHROME") and navegador != ("FIREFOX") :
            print ("----------------")
            print ("Define el DRIVER")
            print ("----------------")
            pytest.skip("Define el DRIVER")
            exit

    def Tap_Action(self, driver, X, Y):
        self.driver = driver
        TouchAction(driver).tap([(X, Y)]).perform()

    def AccID_elements_tap(self, driver, AccID):
        self.driver = driver
        el = driver.find_element_by_accessibility_id(AccID)
        action = TouchAction(self.driver)
        action.tap(el).perform()

    def ID_elements_tap(self, driver, ID):
        self.driver = driver
        el = driver.find_element_by_id(ID)
        action = TouchAction(self.driver)
        action.tap(el).perform()

    def Xpath_elements_tap(self, driver, xpath):
        self.driver = driver
        el = driver.find_element_by_xpath(xpath)
        action = TouchAction(self.driver)
        action.tap(el).perform()

    def ID_elements_click(self, driver, ID):
        self.driver = driver
        locator = driver.find_element_by_id(ID)
        self.assertTrue(locator.is_displayed())
        locator.click()

    def AccID_elements_click(self, driver, AccID):
        self.driver = driver
        locator = driver.find_element_by_accessibility_id(AccID)
        self.assertTrue(locator.is_displayed())
        locator.click()

    def Xpath_elements_click(self, driver, xpath):
        self.driver = driver
        locator = driver.find_element_by_xpath(xpath)
        self.assertTrue(locator.is_displayed())
        locator.click()

    # -------------------------------------------------------------------------------------------#
    def Esperar_ID(self, driver, ID):  # Esperar que un elemento sea visible
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.visibility_of_element_located((By.ID, ID)))

        except TimeoutException:

            print(u"Esperar_ID: No pesente")
            return False

        print(u"Esperar_ID: Se mostró el elemento " + ID)
        return True

    def Esperar_xpath(self, driver, xpath):  # Esperar que un elemento sea visible
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

        except TimeoutException:

            print(u"Esperar_xpath: No pesente")
            return False

        print(u"Esperar_xpath: Se mostró el elemento " + xpath)
        return True

    # -------------------------------------------------------------------------------------------#
    def Get_to_text_Element_ID(self, driver, ID):
        driver = self.driver
        try:

            texto = driver.find_element(By.ID, ID).text

        except NoSuchElementException:

            print(u"Get_to_text_Element_ID: Elemento no pesente")
            return False

        print(u"Get_to_text_Element_ID: Se visualizo el texto, " + texto)

        return texto

    def Get_to_text_Element_xpath(self, driver, xpath):
        driver = self.driver
        try:

            texto = driver.find_element(By.XPATH, xpath).text

        except NoSuchElementException:

            print(u"Get_to_text_Element_xpath: Elemento no pesente")
            return False

        print(u"Get_to_text_Element_xpath: Se visualizo el texto, " + texto)

        return texto

    def Get_to_text_Element_AccID(self, driver, AccID):
        driver = self.driver
        try:

            texto = driver.find_element_by_accessibility_id(AccID).text

        except NoSuchElementException:

            print(u"Get_to_text_Element_AccID: Elemento no pesente")
            return False

        print(u"Get_to_text_Element_AccID: Se visualizo el texto, " + texto)

        return texto

    # -------------------------------------------------------------------------------------------#

    def sendkeys_id(self, driver, ID, TEXT):
        driver = self.driver
        locator = driver.find_element_by_id(ID)
        locator.clear()
        locator.send_keys(TEXT)

    def sendkeys_xpath(self, driver, xpath, TEXT):
        driver = self.driver
        locator = driver.find_element_by_xpath(xpath)
        locator.clear()
        locator.send_keys(TEXT)

    def sendkeys_AccID(self, driver, AccID, TEXT):
        driver = self.driver
        locator = driver.find_element_by_accessibility_id(AccID)
        locator.clear()
        locator.send_keys(TEXT)

    # -------------------------------------------------------------------------------------------#

    # TouchAction(driver).press(x=885, y=578).move_to(x=-636, y=-30).release().perform()
    def swipe_screen(self, driver, pressX, pressY, MoveX, MoveY):
        driver = self.driver
        screen = TouchAction(driver)
        screen.press(x=int(pressX), y=int(pressY))
        screen.move_to(x=int(MoveX), y=int(MoveY))
        screen.release().perform()
        time.sleep(2)
        print("Se hizo Swipe: " + " x:" + pressX + " Y" + pressY + " MoveX:" + MoveX + " MoveY:" + MoveY)
