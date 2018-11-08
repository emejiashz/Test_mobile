# -*- coding: utf-8 -*-
import time
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException  
from selenium.webdriver.common.action_chains  import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import os


diaGlobal= time.strftime("%Y-%m-%d")  # formato aaaa/mm/dd
horaGlobal = time.strftime("%H%M%S")  # formato 24 houras


class seleniumFunctions():
    #(572, 1442)
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
        locator  = driver.find_element_by_id(ID)
        self.assertTrue(locator.is_displayed())
        locator.click()
        
    def AccID_elements_click(self, driver, AccID):
        self.driver = driver
        locator  = driver.find_element_by_accessibility_id(AccID)
        self.assertTrue(locator.is_displayed())
        locator.click()
          
    def Xpath_elements_click(self, driver, xpath):
        self.driver = driver   
        locator  = driver.find_element_by_xpath(xpath)
        self.assertTrue(locator.is_displayed())
        locator.click()
    #-------------------------------------------------------------------------------------------#

    # nomenclatura de la evidencia: número_caso_de_prueba + hora [hh:mm:ss]
    
    def capturar_Pantalla(self):  
        def hora_Actual():
            hora = time.strftime("%H%M%S")
            return hora
        
        dia = time.strftime("%d-%m-%Y")
        
        GeneralPath = "C:\\Evidencias\\APPIUM\\" #Directorio de las Capturas#
        DriverTest = "MOBILE"
        TestCase = self.__class__.__name__
        horaAct = str(hora_Actual())
        
        path = GeneralPath + dia + "\\" + TestCase + "\\" + DriverTest + "\\" +  horaAct + "\\"
 
        if not os.path.exists(path): 
            os.makedirs(path)
 
        img = path + TestCase + "_(" + str(hora_Actual()) + ")" + ".png"
         
        self.driver.get_screenshot_as_file(img)
        
        print (img)
         
        return img  
    #-------------------------------------------------------------------------------------------#
    def Esperar_ID(self, driver, ID): #Esperar que un elemento sea visible
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.visibility_of_element_located((By.ID, ID)))
            
        except TimeoutException:
        
            print (u"Esperar_ID: No pesente")
            return False
        
        print (u"Esperar_ID: Se mostró el elemento "+ ID)
        return True
      
    def Esperar_xpath(self, driver, xpath): #Esperar que un elemento sea visible
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            
        except TimeoutException:
        
            print (u"Esperar_xpath: No pesente")
            return False
        
        print (u"Esperar_xpath: Se mostró el elemento "+ xpath)
        return True
    
#-------------------------------------------------------------------------------------------#    
    def Get_to_text_Element_ID(self, driver, ID):  
        driver = self.driver
        try:
            
            texto = driver.find_element(By.ID, ID).text
            
        except NoSuchElementException:
            
            print (u"Get_to_text_Element_ID: Elemento no pesente")
            return False
        
        print (u"Get_to_text_Element_ID: Se visualizo el texto, " + texto)
        
        return texto
    
    def Get_to_text_Element_xpath(self, driver, xpath):  
        driver = self.driver
        try:
            
            texto = driver.find_element(By.XPATH, xpath).text
            
        except NoSuchElementException:
            
            print (u"Get_to_text_Element_xpath: Elemento no pesente")
            return False
        
        print (u"Get_to_text_Element_xpath: Se visualizo el texto, " + texto)
        
        return texto

    def Get_to_text_Element_AccID(self, driver, AccID):  
        driver = self.driver
        try:
            
            texto = driver.find_element_by_accessibility_id(AccID).text
            
        except NoSuchElementException:
            
            print (u"Get_to_text_Element_AccID: Elemento no pesente")
            return False
        
        print (u"Get_to_text_Element_AccID: Se visualizo el texto, " + texto)
        
        return texto
#-------------------------------------------------------------------------------------------#
       
    def sendkeys_id(self, driver, ID, TEXT):
        driver = self.driver 
        locator  = driver.find_element_by_id(ID)
        locator.clear()
        locator.send_keys(TEXT)
        
    def sendkeys_xpath(self, driver, xpath, TEXT):
        driver = self.driver 
        locator  = driver.find_element_by_xpath(xpath)
        locator.clear()
        locator.send_keys(TEXT)    
        
    def sendkeys_AccID(self, driver, AccID, TEXT):
        driver = self.driver 
        locator  = driver.find_element_by_accessibility_id(AccID)
        locator.clear()
        locator.send_keys(TEXT)      
#-------------------------------------------------------------------------------------------#

#TouchAction(driver).press(x=885, y=578).move_to(x=-636, y=-30).release().perform()
    def swipe_screen(self, driver, pressX, pressY, MoveX, MoveY):
        driver = self.driver 
        screen = TouchAction(driver)
        screen.press(x = int(pressX), y = int (pressY))
        screen.move_to(x = int(MoveX), y = int(MoveY))
        screen.release().perform()
        time.sleep(2)
        print ("Se hizo Swipe: " + " x:" + pressX + " Y" + pressY + " MoveX:" + MoveX + " MoveY:" + MoveY)

#-------------------------------------------------------------------------------------------------------#
    
    def ir_a_xpath(self, driver, xpath):
        try:
            localizador = driver.find_element(By.XPATH, xpath)  
            driver.execute_script("arguments[0].scrollIntoView();", localizador)
            
        except TimeoutException:
            
            print (u"ir_a_xpath: No presente")
            return False
        
        print (u"ir_a_xpath: Se desplazó al elemento, "+ xpath)
        return True
    
    def mouse_over_id(self, driver, ID):
        element = driver.find_element_by_id(ID)
        action = ActionChains(driver)
        action.move_to_element(element).perform()

    def mouse_over_xpath(self, driver, xpath):
        element = driver.find_element_by_xpath(xpath)
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        
    def mouse_over_css(self, driver, css):
        element = driver.find_element_by_css_selector(css)
        action = ActionChains(driver)
        action.move_to_element(element).perform()      
    
    def verificarTexto_xpath(self, driver, xpath, TEXTO): #devuelve true o false
        try:
            wait = WebDriverWait(driver, 15)
            wait.until(EC.text_to_be_present_in_element((By.XPATH, xpath), TEXTO))
        except NoSuchElementException:
            print (u"Verificar Texto: Texto no pesente")
            return False
        print (u"Verificar Texto: Se visualizó en, " + xpath + " el texto, " + TEXTO)
        return True
    
    def verificar_xpath(self, driver, xpath): #devuelve true o false
        try:
            
            driver.find_element_by_xpath(xpath)
            
        except NoSuchElementException:
            
            print (u"Verificar: Elemento no pesente")
            return False
        
        print (u"Verificar: Se visualizo el elemento, "+ xpath)
        
        return True
    
    def ver_texto(self, driver, xpath): 
        try:
            
            texto = driver.find_element_by_xpath(xpath).text
            
        except NoSuchElementException:
            
            print (u"Verificar: Elemento no pesente")
            return False
        
        print (u"Verificar: Se visualizo el texto, " + texto + ", en el elemento " + xpath)
        
        return texto
    
    def cerrar_alerta_gettext(self):
        self.accept_next_alert = True
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    
    def select_elements_id(self, driver, ID):
        select = Select(driver.find_element_by_id(ID))
        return select
    
    def select_elements_xpath(self, driver, xpath):
        select = Select(driver.find_element_by_xpath(xpath))
        return select
    
    def select_elements_css(self, driver, css):
        select = Select(driver.find_element_by_css_selector(css))
        return select
    
    #USO

#       select by visible text
#       select.select_by_visible_text('Banana')
        
#       select by value 
#       select.select_by_value('1')

    def Xpath_dpd_elements(self, driver, xpath, opt):
        selx = xpath + "/option["+opt+"]"
        localizador = driver.find_element_by_xpath(selx)
        return localizador
    
    def CSS_dpd_elements(self, driver, css, opt):
        selx = css + " option:nth-child("+opt+")"
        localizador = driver.find_element_by_css_selector(selx)
        return localizador
        
    def Xpath_elements(self, driver, xpath):
        localizador = driver.find_element_by_xpath(xpath)
        return localizador
    
    def CSS_elements(self, driver, css):
        localizador = driver.find_element_by_css_selector(css)
        return localizador
    
    
    def Name_elements(self, driver, name):
        localizador = driver.find_element_by_name(name)
        return localizador
    
    def Link_elements(self, driver, link):
        localizador = driver.find_element_by_partial_link_text(link)
        return localizador
    
    def JS_Click_Xpath(self, driver, xpath):
        localizador = driver.find_element_by_xpath(xpath)
        driver.execute_script("arguments[0].click();", localizador)
    
    def JS_Click_CSS(self, driver, css):
        localizador = driver.find_element_by_css_selector(css)
        driver.execute_script("arguments[0].click();", localizador)
    
    def JS_Click_ID(self, driver, ID):
        localizador = driver.find_element_by_id(ID)
        driver.execute_script("arguments[0].click();", localizador)

    def JS_Click_Link(self, driver, link):
        localizador = driver.find_element_by_partial_link_text(link)
        driver.execute_script("arguments[0].click();", localizador)
    