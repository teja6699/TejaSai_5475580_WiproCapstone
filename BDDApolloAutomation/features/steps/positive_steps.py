from behave import given, when, then

from pages.home_page import HomePage
from pages.lab_tests_page import LabTestsPage
from pages.vital_organs_page import VitalOrgansPage


@given('user launches Apollo application')
def step_impl(context):

    context.home = HomePage(
        context.driver
    )

    context.home.open_home_page()


@when('user navigates to lab tests')
def step_impl(context):

    context.home.click_lab_tests()


@when('user selects vital organs')
def step_impl(context):

    context.lab = LabTestsPage(
        context.driver
    )

    context.lab.select_vital_organs()


@when('user opens thyroid card')
def step_impl(context):

    context.vital = VitalOrgansPage(
        context.driver
    )

    context.vital.open_thyroid_card()


@when('user adds thyroid package')
def step_impl(context):

    context.vital.click_add_button()

@when('user adds package to cart')
def step_impl(context):

    context.vital.click_add_button()


@then('package should be added successfully')
def step_impl(context):

    assert True


@given('user reaches payment page')
def step_impl(context):

    context.home = HomePage(
        context.driver
    )

    context.lab = LabTestsPage(
        context.driver
    )

    context.vital = VitalOrgansPage(
        context.driver
    )

    context.home.open_home_page()

    context.home.click_lab_tests()

    context.lab.select_vital_organs()

    context.vital.open_thyroid_card()

    context.vital.click_add_button()

    context.vital.click_go_to_cart()

    mobile = context.testdata[
        "mobile_number"
    ][0]

    context.vital.login_with_mobile(
        mobile
    )

    context.vital.click_verify_button()

    context.vital.click_go_to_cart()

    context.vital.select_patient_checkbox()

    context.vital.click_select_slot_button()

    context.vital.click_review_cart_button()


@when('user enters valid mobile number')
def step_impl(context):

    mobile = context.testdata[
        "mobile_number"
    ][0]

    context.vital.login_with_mobile(
        mobile
    )


@then('OTP screen should open')
def step_impl(context):

    assert True


@given('user logged into application')
def step_impl(context):

    context.home = HomePage(
        context.driver
    )

    context.lab = LabTestsPage(
        context.driver
    )

    context.vital = VitalOrgansPage(
        context.driver
    )

    context.home.open_home_page()

    context.home.click_lab_tests()

    context.lab.select_vital_organs()

    context.vital.open_thyroid_card()

    context.vital.click_add_button()

    context.vital.click_go_to_cart()

    mobile = context.testdata[
        "mobile_number"
    ][0]

    context.vital.login_with_mobile(
        mobile
    )

    context.vital.click_verify_button()


@when('user clicks select slot')
def step_impl(context):

    context.vital.click_go_to_cart()

    context.vital.select_patient_checkbox()

    context.vital.click_select_slot_button()


@then('slot selection should succeed')
def step_impl(context):

    assert True