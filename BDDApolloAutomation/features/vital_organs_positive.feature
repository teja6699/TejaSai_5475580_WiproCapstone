Feature: Apollo Vital Organs Positive Scenarios

  Scenario: Valid Thyroid Test Booking

    Given user launches Apollo application
    When user navigates to lab tests
    And user selects vital organs
    And user opens thyroid card
    And user adds thyroid package
    Then package should be added successfully


  Scenario: Valid Mobile Login

    Given user launches Apollo application
    When user navigates to lab tests
    And user selects vital organs
    And user adds package to cart
    And user enters valid mobile number
    Then OTP screen should open


  Scenario: Successful Slot Selection

    Given user logged into application
    When user selects patient checkbox
    And user clicks select slot
    Then slot selection should succeed