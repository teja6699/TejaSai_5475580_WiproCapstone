from behave import *


@when('user enters invalid mobile number')
def step_impl(context):

    print("Invalid mobile entered")


@then('error message should display')
def step_impl(context):

    assert True


@when('user enters invalid card details')
def step_impl(context):

    print("Invalid card details entered")


@then('payment should fail')
def step_impl(context):

    assert True