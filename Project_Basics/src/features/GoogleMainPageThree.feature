# Created by Mdiaz at 31/10/2018
@Integration
Feature: Test Google Search Box
  Test searches query in google main page

  @TableSearch
  Scenario Outline: We want to look for “KEYWORDS” in google
    Given User open site http://www.google.com
    When I Type <KEYWORDS> in google search box
      Examples:
          | KEYWORDS      |
          | metallica     |
          | Maiden        |
    Then Query results are under 10000
    Then I Close the Driver


  @TableSearch
  Scenario Outline: We want to look for “KEYWORDS” in google
    Given User open site http://www.google.com
    And Type Metallica in google search box
    Then Query results are under 10000
    And The main result contains the <WORDS> in
      Examples:
          | WORDS                            |
          | Metallica                        |
    Then I Close the Driver

  @TableSearch
  Scenario: We want to look for “KEYWORDS” in google
    Given User open site http://www.google.com
    And Type Metallica in google search box
    Then Query results are under 10000
    And The main result contains Metallica
    Then I Close the Driver