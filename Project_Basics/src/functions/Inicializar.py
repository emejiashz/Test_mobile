# -*- coding: utf-8 -*-
   
class Inicializar():
    "hola"
    #BROWSER DE PRUEBAS
    NAVEGADOR = u"ANDROID"
    
    #DIRECTORIO DE LA EVIDENCIA
    Path_Evidencias = u"C:\Evidencias"
    
    #HOJA DE DATOS EXCEL
    Excel= u"..\data\Data.xlsx"

    Model = "ALCATEL_7040N"
    Package = "Mercadolibre"

    def inicializar_package(self):
        if (self.Package == "Mercadolibre"):
            print ('PAQUETE DE APLICACION MERCADOLIBRE')
            self.myApk = 'C:\\AppiumFramework\\APK\\mercadolibre-9-15-8.apk'
            self.appPackage = 'com.mercadolibre'
            self.appActivity = 'activities.SplashActivity'

        if (self.Package == ""):
            print ("Pain and Blood for you")

    def inicializar_mobile_capabilities(self):

        self.inicializar_package()

        if (self.Model == "ALCATEL_7040N"):
            print('PAQUETE DE CAPABILITIES ALCATEL_7040N')
            desired_caps = {}
            desired_caps['platformName'] = 'android'
            desired_caps['platformVersion'] = '4.4.2'
            desired_caps['deviceName'] = '4e9aa907'
            desired_caps['app'] = self.myApk
            desired_caps['appPackage'] = self.appPackage
            desired_caps['appActivity'] = self.appActivity
            desired_caps['NoReset'] = False
            return desired_caps

        if (self.Model == "MOTO_G5_PLUS"):
            print('PAQUETE DE CAPABILITIES MOTO_G5_PLUS')
            desired_caps = {}
            desired_caps['platformName'] = 'android'
            desired_caps['platformVersion'] = '8.1.0'
            desired_caps['deviceName'] = 'ZY322MBC9D'
            desired_caps['app'] = self.myApk
            desired_caps['appPackage'] = self.appPackage
            desired_caps['appActivity'] = self.appActivity
            desired_caps['NoReset'] = True
            return desired_caps

        if (self.Model == "LG_KITE"):
            print('PAQUETE DE CAPABILITIES LG_KITE')
            desired_caps = {}
            desired_caps['platformName'] = 'android'
            desired_caps['platformVersion'] = '8.1'
            desired_caps['deviceName'] = 'ZY322MBC9D'
            desired_caps['app'] = self.myApk
            desired_caps['appPackage'] = self.appPackage
            desired_caps['appActivity'] = self.appActivity
            desired_caps['NoReset'] = True
            return desired_caps



    def cap_SONYM5(self, myApk, appPackage, appActivity, puerto):
        desired_caps = {}
        desired_caps['platformName'] = 'android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = 'LGH221AR50a53209'
        desired_caps['app'] = myApk
        desired_caps['appPackage'] = appPackage
        desired_caps['appActivity'] = appActivity
        desired_caps['NoReset'] = True



    