# -*- coding: utf-8 -*-


from appium import webdriver

# PACKAGE DE APK MERCADO LIBRE 
MLApk = 'C:\\AppiumFramework\\APK\\mercadolibre-9-15-8.apk'
MLappPackage = 'com.mercadolibre'
MLActivity = 'activities.SplashActivity'


class Iniciar_app():
    
    
    #CAPABILITIES ALCATEL 7040N

    def cap_Alcatel(self, myApk, appPackage, appActivity, puerto):
        
        desired_caps = {}
        desired_caps['platformName'] = 'android' 
        desired_caps['platformVersion'] = '4.4.2' 
        desired_caps['deviceName'] = '4e9aa907' 
        desired_caps['app'] = myApk
        desired_caps['appPackage'] = appPackage
        desired_caps['appActivity'] = appActivity
        desired_caps['NoReset'] = True 
        self.driver = webdriver.Remote(puerto + "/wd/hub", desired_caps)
        return self.driver
    
    #CAPABILITIES MOTO G5 PLUS
    
    def cap_MOTOG5(self, myApk, appPackage,appActivity, puerto ): 
   
        desired_caps = {}
        desired_caps['platformName'] = 'android' 
        desired_caps['platformVersion'] = '8.1.0' 
        desired_caps['deviceName'] = 'ZY322MBC9D' 
        desired_caps['app'] = myApk
        desired_caps['appPackage'] = appPackage
        desired_caps['appActivity'] = appActivity
        desired_caps['NoReset'] = True 
        self.driver = webdriver.Remote(puerto + "/wd/hub", desired_caps)  
        return self.driver
    
    #CAPABILITIES SONY XPERIA M5
    
    def cap_SONYM5(self, myApk, appPackage,appActivity, puerto ): 
   
        desired_caps = {}
        desired_caps['platformName'] = 'android' 
        desired_caps['platformVersion'] = '6.0' 
        desired_caps['deviceName'] = 'YT911BA6UJ' 
        desired_caps['app'] = myApk
        desired_caps['appPackage'] = appPackage
        desired_caps['appActivity'] = appActivity
        desired_caps['NoReset'] = True 
        self.driver = webdriver.Remote(puerto + "/wd/hub", desired_caps)  
        return self.driver
    
    #CAPABILITIES LG KITE 
    
    def cap_LGKITE(self, myApk, appPackage,appActivity, puerto ): 
   
        desired_caps = {}
        desired_caps['platformName'] = 'android' 
        desired_caps['platformVersion'] = '4.4.2' 
        desired_caps['deviceName'] = 'LGH221AR50a53209' 
        desired_caps['app'] = myApk
        desired_caps['appPackage'] = appPackage
        desired_caps['appActivity'] = appActivity
        desired_caps['NoReset'] = True 
        self.driver = webdriver.Remote(puerto + "/wd/hub", desired_caps)  
        return self.driver
    
    
    