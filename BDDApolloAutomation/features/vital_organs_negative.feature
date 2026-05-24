Feature: Apollo Vital Organs Negative Scenarios

  Scenario: Invalid Mobile Number

    Given user launches Apollo application
    When user enters invalid mobile number
    Then error message should display


  Scenario: Invalid Card Details

    Given user reaches payment page
    When user enters invalid card details
    Then payment should fail