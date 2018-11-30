cd C:\TestFramework\ws\Project_Basics\src\features
SET PYTHONPATH=%PATH%;%behave_projects%
@echo off

echo. ##################### PRUEBAS #####################

echo. behave -f allure_behave.formatter:AllureFormatter --tags=SearchBox -o ..\allure-results


behave -f allure_behave.formatter:AllureFormatter -o ..\allure-results


pause