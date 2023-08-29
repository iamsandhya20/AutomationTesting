Feature: Produce Search
  Scenario: text is present in the page
    Given Open the browser
    When load the page
    Then verify the text is executed
    And search for 'cars'