from behave import *


@when('user clicks go to cart')
def step_impl(context):

    context.vital.click_go_to_cart()


@when('user logs in with valid mobile number')
def step_impl(context):

    mobile = context.testdata[
        "mobile_number"
    ][0]

    context.vital.login_with_mobile(
        mobile
    )


@when('user verifies OTP manually')
def step_impl(context):

    context.vital.click_verify_button()


@when('user clicks go to cart again')
def step_impl(context):

    context.vital.click_go_to_cart()


@when('user selects patient checkbox')
def step_impl(context):

    context.vital.select_patient_checkbox()


@when('user selects slot')
def step_impl(context):

    context.vital.click_select_slot_button()


@when('user reviews cart')
def step_impl(context):

    context.vital.click_review_cart_button()


@when('user proceeds to payment')
def step_impl(context):

    context.vital.click_proceed_to_pay()


@when('user selects credit debit card')
def step_impl(context):

    context.vital.click_credit_debit_card_section()


@when('user enters card details')
def step_impl(context):

    context.vital.enter_card_details(

        context.testdata["card_name"][0],

        context.testdata["card_number"][0],

        context.testdata["expiry_date"][0],

        context.testdata["cvv"][0]
    )


@then('payment flow should complete successfully')
def step_impl(context):

    context.vital.click_pay_button()

    assert True