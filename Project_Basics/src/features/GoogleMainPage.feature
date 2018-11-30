# Created by Mdiaz at 31/10/2018
@Integration
Feature: Test Google Search Box
  Test searches query in google main page

  @SearchBox
  Scenario: We want to look for “TestSquad.net” word in google main page and check if amount of results is bigger than 100000
    Given User open Google main site
    And Type TestSquad.net in google search box
    Then Query results are under 10000
    Then I Close the Driver

