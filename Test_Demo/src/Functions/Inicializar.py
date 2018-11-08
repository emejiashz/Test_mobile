# -*- coding: utf-8 -*-


from appium import webdriver

MLApk = 'C:\\AppiumFramework\\APK\\mercadolibre-9-15-8.apk'
MLappPackage = 'com.mercadolibre'
MLActivity = 'activities.SplashActivity'

class Inicializar():

    def IniciarApp(self, platformName, platformVersion, deviceName, myApk, appPackage, appActivity, noReset, puerto):

        desired_caps = {}
        desired_caps['platformName'] = platformName         #S.O DEL DISPOSITIVO
        desired_caps['platformVersion'] = platformVersion   # VERSION DE S.O 
        desired_caps['deviceName'] = deviceName             #NOMBRE DEL DISPOSITIVO
        #desired_caps['udid'] = udid                        # UID DEL SO
        desired_caps['app'] = myApk                         #DIR DE APK 
        desired_caps['appPackage'] = appPackage
        desired_caps['appActivity'] = appActivity
        desired_caps['noReset'] = noReset
        self.driver = webdriver.Remote(puerto + "/wd/hub", desired_caps)  #S.O DEL DISPOSITIVO
        return self.driver
    