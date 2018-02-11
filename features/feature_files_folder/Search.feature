Feature: Search Instaworks on Google

  @tag_me
  Scenario: Search for instaworks on google
    Given Perform initial browser setup
    When Perform some action on search page "http://www.google.co.in"
    Then All actions should be successful
