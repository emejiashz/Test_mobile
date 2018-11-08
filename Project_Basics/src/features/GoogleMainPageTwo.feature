# Created by Mdiaz at 31/10/2018
@Integration
Feature: Test Google Search Box
  Test searches query in google main page

  @TableSearch
  Scenario: We want to look for “RAET”
    Given User open site http://www.google.com
    Then Type <keywords> in google search box
      | keywords     |
      | Raet         |
      | metallica    |

