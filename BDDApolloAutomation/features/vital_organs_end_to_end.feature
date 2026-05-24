@e2e
Feature: Apollo Lab Test End To End Booking

  Scenario: Complete Lab Test Booking

    Given user launches Apollo application
    When user navigates to lab tests
    And user selects vital organs
    And user opens thyroid card
    And user adds thyroid package
    And user clicks go to cart
    And user logs in with valid mobile number
    And user verifies OTP manually
    And user clicks go to cart again
    And user selects patient checkbox
    And user selects slot
    And user reviews cart
    And user proceeds to payment
    And user selects credit debit card
    And user enters card details
    Then payment flow should complete successfully