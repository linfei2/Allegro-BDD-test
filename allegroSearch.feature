Feature: Search for products on Allegro platform

  Scenario Outline: Search for "głośnik przenośny"
    Given I launch Chrome browser
    When I open allegro page
    And close pop up window
    And I enter "<product_name>" in search field
    And click SZUKAJ button
    Then list of products appears

    Examples:

    | product_name      |
    | głośnik przenośny |
    | glosnik przenosny |
    | gośnik pszenośny  |
    | GŁOŚNIK PRZENOŚNY |