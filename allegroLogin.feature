Feature: Login to Allegro

  Background:
    Given I launch Chrome browser
    When I open allegro page
    And close pop up window
    And click sign in button

  Scenario: Login with valid data
    When I enter "testing789@onet.pl" as e-mail
    And enter "Tester123" as password
    And click Zaloguj się
    Then I am logged in

  Scenario Outline: Login with invalid data
    When I enter "<email>" as e-mail
    And enter "<password>" as password
    And click Zaloguj się
    Then Login fails

    Examples:
      | email               | password  |
      | testing689@onet.pl  | Tester123 |
      | testing789@onet.pl  | Tester1   |
      | testingonet.pl      | tester123 |


