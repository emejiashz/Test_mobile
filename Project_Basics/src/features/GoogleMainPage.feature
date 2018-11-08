# Created by Mdiaz at 31/10/2018
@Integration
Feature: Test Google Search Box
  Test searches query in google main page

    @ignore
    @SearchBox
  Scenario: We want to look for “RAET” word in google main page and check if amount of results is bigger than 100000
    Given User open Google main site
    And Type RAET in google search box
    Then Query results are under 10000


  @TableSearch
  Scenario: We want to look for “RAET”
    Given User open site http://www.google.com
    When Type <keyword> in google search box
    | keyword      |
    | Raet         |
    | metallica    |

