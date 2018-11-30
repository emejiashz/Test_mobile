cd C:\TestFramework\ws\Project_Basics\src\tests
SET PATH=%PATH%;%PYTHONPATH%;

@echo off

echo. ##################### PRUEBAS #####################



C:\TestFramework\python36\python.exe -m pytest set_xml.py 

C:\TestFramework\python36\python.exe -m pytest tst_002.py --alluredir ..\allure-results


pause