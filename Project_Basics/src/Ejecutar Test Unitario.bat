cd C:\TestFramework\ws\Project_Basics\src\features
SET PYTHONPATH=%PATH%;%behave_projects%
@echo off

echo. ##################### PRUEBAS #####################

behave -f allure_behave.formatter:AllureFormatter --tags=SearchBox -o ..\allure-results


pause