from behave import *
from selenium.webdriver import Firefox
from behave.api.pending_step import StepNotImplementedError
@Given(u'user is on Login Page')
def step_imp(context):
    context.driver=Firefox()
    context.driver.get('https://education.softtechverse.com/authentication')
    context.driver.maximize_window()
@When(u'user enters username')
def step_imp(context):
    context.driver.find_element("name","email").send_keys("admin")

@When(u'user enters password')
def step_imp(context):
    context.driver.find_element("name","password").send_keys("admin@12345")

@When(u'user click on Login button')
def step_imp(context):
    context.driver.find_element("xpath","//button[@type='submit']").click()

@Then(u'user should be entered on Dashboard')
def step_imp(context):
    print("Welcome to the Dashboard!")